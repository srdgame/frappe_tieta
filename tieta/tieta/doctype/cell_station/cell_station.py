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
		self.county_name = frappe.get_value("Region", self.county, "region_name")
		self.town_name = frappe.get_value("Region", self.town, "region_name")

	def __formate_address(self):
		return " ".join([self.province_name, self.city_name, self.county_name, self.town_name, self.address])

	def after_insert(self):
		data = {
			"naming_series": "CELL-",
			"project": self.project,
			"site_name": self.station_name,
			"address": self.__formate_address(),
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
		self.set("site", None)
		self.save()
		frappe.delete_doc("Cloud Project Site", self.site, ignore_permissions=True)

	def on_update(self):
		site = frappe.get_doc("Cloud Project Site", self.site)
		site.set("project", self.project)
		site.set("address", self.__formate_address())
		site.set("site_name", self.station_name)
		site.set("longitude", self.longitude)
		site.set("latitude", self.latitude)
		site.save(ignore_permissions=True)