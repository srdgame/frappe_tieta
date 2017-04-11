# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CellStation(Document):
	def __in_station(self, device_type, device_id, device_type_name):
		doc = frappe.get_doc({
			"doctype": "Stock Item History",
			"inout": 'IN',
			"item_type": device_type,
			"item": device_id,
			"position_type": "Cell Station",
			"position": self.name,
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
				self.__out_station(d.device_type_value, d.device_id, dev.device_type)


	def after_insert(self):
		data = {
			"naming_series": "CELL-",
			"project": self.project,
			"site_name": self.station_name,
			"longitude": self.longitude,
			"latitude": self.latitude,
		}
		data.update({
			"doctype": "Cloud Project Site"
		})
		doc = frappe.get_doc(data)
		doc = doc.insert(ignore_permissions=True)
		self.site = doc.name
		self.save()

	def on_trash(self):
		if frappe.session.user != 'Administrator':
			frappe.delete_doc("Cloud Project Site", self.site, ignore_permissions=True)

	def on_update(self):
		site = frappe.get_doc("Cloud Project Site", self.site)
		site.set("project", self.project)
		site.set("address", self.address_text)
		site.set("site_name", self.station_name)
		site.set("longitude", self.longitude)
		site.set("latitude", self.latitude)
		site.save(ignore_permissions=True)