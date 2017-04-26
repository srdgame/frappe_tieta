# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
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

	def on_trash(self):
		for dev in self.devices:
			self.__out_station(dev.device_type_value, dev.device_id, dev.device_type)


@frappe.whitelist()
def search_station(txt="", rgn=None, rgn_type="province", start=0, page_length=20, order_by="modified desc"):
	user_roles = frappe.get_roles(frappe.session.user)
	if 'TieTa User' not in user_roles:
		raise frappe.PermissionError

	from cloud.cloud.doctype.cloud_project.cloud_project import list_user_projects
	projects = list_user_projects(frappe.session.user)
	if not rgn:
		return frappe.db.sql('''select * from `tabCell Station` station
			where station.project in {3}
			order by station.{0} limit {1}, {2}
			'''.format(order_by, start, page_length, "('" + "','".join(projects) + "')"),
				{},
				as_dict=True,
				update={'doctype': 'Cell Station'})

	rgn_key = 'region_address.' + rgn_type

	return frappe.db.sql('''select distinct station.*
		from `tabCell Station` station, `tabRegion Address` region_address
		where
			station.name = region_address.parent
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
