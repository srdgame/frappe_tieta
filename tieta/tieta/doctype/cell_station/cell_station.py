# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document


class CellStation(Document):
	def __get_uom(self, device_type):
		item_code = frappe.get_value('Cell Station Device Type', device_type, 'type_item')
		return frappe.get_value("Stock Item", item_code, "stock_uom")

	def __in_station(self, device_type, device_id, device_type_name):
		doc = frappe.get_doc({
			"doctype": "Stock Item History",
			"inout": 'IN',
			"item_type": device_type,
			"item": device_id,
			"position_type": "Cell Station",
			"position": self.name,
			"qty": 1,
			"uom": self.__get_uom(device_type_name),
			"remark": device_type_name
		}).insert()

	def __out_station(self, device_type, device_id, device_type_name):
		doc = frappe.get_doc({
			"doctype": "Stock Item History",
			"inout": 'OUT',
			"item_type": device_type,
			"item": device_id,
			"position_type": "Cell Station",
			"position": self.name,
			"qty": 1,
			"uom": self.__get_uom(device_type_name),
			"remark": device_type_name
		}).insert()

	def before_save(self):
		if self.is_new():
			return

		names = frappe.get_list("Cell StationDevice",
								filters={"parent": self.name},
								fields=["name", "device_id", "device_type_value", "device_type"])
		devices = [d[0] for d in frappe.db.get_values("Cell StationDevice", {"parent": self.name}, "device_id")]
		keep_list = []
		for dev in self.devices:
			name = frappe.db.get_value("Cell StationDevice",
						{"parent": self.name, "device_id": dev.device_id, "device_type": dev.device_type})
			if not name:
				self.__in_station(dev.device_type_value, dev.device_id, dev.device_type)
			else:
				keep_list.append(name)

		for d in frappe.get_list("Cell StationDevice",
								filters={"parent": self.name},
								fields=["name", "device_id", "device_type_value", "device_type"]):
			if d.name not in keep_list:
				self.__out_station(d.device_type_value, d.device_id, d.device_type)

	def after_insert(self):
		for dev in self.devices:
			self.__in_station(dev.device_type_value, dev.device_id, dev.device_type)

	def on_trash(self):
		for dev in self.devices:
			self.__out_station(dev.device_type_value, dev.device_id, dev.device_type)

	def clear_device_history(self):
		if 'Administrator' != frappe.session.user:
			throw(_("You are not Administrator, so cannot clear device history of cell station"))
		hlist = [d[0] for d in frappe.db.get_values("Stock Item History", {"position": self.name}, "name")]
		for h in hlist:
			frappe.delete_doc("Stock Item History", h)


@frappe.whitelist()
def search_station(txt="", rgn=None, rgn_type="province", start=0, page_length=20, order_by="modified desc"):
	user_roles = frappe.get_roles(frappe.session.user)
	if 'TieTa User' not in user_roles:
		raise frappe.PermissionError

	from cloud.cloud.doctype.cloud_project.cloud_project import list_user_projects
	projects = list_user_projects(frappe.session.user)
	if not rgn:
		return frappe.db.sql('''select * from `tabCell Station` station
			where station.enabled = 1 and station.project in {3}
			order by station.{0} limit {1}, {2}
			'''.format(order_by, start, page_length, "('" + "','".join(projects) + "')"),
				{},
				as_dict=True,
				update={'doctype': 'Cell Station'})

	rgn_key = 'region_address.' + rgn_type

	return frappe.db.sql('''select distinct station.*
		from `tabCell Station` station, `tabRegion Address` region_address
		where station.enabled = 1
			and station.name = region_address.parent
			and {3} = %(rgn)s and station.project in {4}
			and station.station_name like %(txt)s order by station.{0}
			limit {1}, {2}
		'''.format(order_by, start, page_length, rgn_key, "('"+"','".join(projects)+"')"),
			{'rgn' : rgn, 'txt' : "%%%s%%" % txt},
			as_dict=True,
			update={'doctype' : 'Cell Station'})


@frappe.whitelist()
def list_station_map():
	return search_station(start=0, page_length=10000)

@frappe.whitelist()
def list_station_info(rgn=None, rgn_type="province", code=None, station_name=None, symlink_sn=None, status=None, page_length=10000):
	_stations = search_station(rgn=rgn, rgn_type=rgn_type, start=0, page_length=page_length)
	new_stations = []
	for d in _stations:
		doc = frappe.get_doc("Cell Station", d.name)
		symlink_type = frappe.db.get_single_value('Cell Station Settings', 'symlink_device_type')
		symlink_status = None
		symLinksn = None
		for dev in doc.devices:
			if dev.device_type == symlink_type:
				symLinksn = dev.device_id
				if symLinksn:
					try:
						symlink_status = frappe.get_doc("IOT Device", symLinksn).device_status
						break
					except Exception, e:
						frappe.logger(__name__).error(e)
						traceback.print_exc()
					finally:
						frappe.logger(__name__).error(_("Device {0} does not exits!").format(symLinksn))
				else:
					symlink_status = 'UNKNOWN'
					symLinksn = 'UNKNOWN'
		d.status = symlink_status
		d.symlink_sn = symLinksn
		_filter = {}
		if code:
			_filter["code"] = code
		if station_name:
			_filter["station_name"] = station_name
		if symlink_sn:
			_filter["symlink_sn"] = symlink_sn
		if status:
			_filter["status"] = status
		if _filter:
			mz = True
			for (k, v) in _filter.items():
				if v.upper() in getattr(d, k).upper():
					continue
				else:
					mz = False
					break
			if mz:
				new_stations.append(d)
		else:
			new_stations.append(d)

	return new_stations