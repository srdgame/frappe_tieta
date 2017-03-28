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
