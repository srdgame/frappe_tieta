# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CellStation(Document):

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