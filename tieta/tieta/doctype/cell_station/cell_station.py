# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CellStation(Document):
	def validate(self):
		self.province_name = frappe.get_value("Region", self.province, "region_name")
		self.city_name = frappe.get_value("Region", self.city, "region_name")
		self.town_name = frappe.get_value("Region", self.town, "region_name")

	def after_insert(self):
		data = {
			"naming_series": "CELL-",
			"project": self.project,
			"site_name": self.station_name,
			"address": self.address,
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
		frappe.delete_doc("Cloud Project Site", self.site, ignore_permissions=True)