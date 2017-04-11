# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CellStationDevice(Document):
	def after_insert(self):
		if self.device_id:
			doc = frappe.get_doc({
				"doctype": "Stock Item History",
				"inout": 'IN',
				"item_type": self.device_type_value,
				"item": self.device_id,
				"position_type": "Cell Station",
				"position": self.parent
			}).insert()

	def on_update(self):
		org_id = self.get("device_id")
		if org_id and org_id != self.device_id:
			doc = frappe.get_doc({
				"doctype": "Stock Item History",
				"inout": 'OUT',
				"item_type": self.device_type_value,
				"item": org_id,
				"position_type": "Cell Station",
				"position": self.parent
			}).insert()
		if self.device_id:
			doc = frappe.get_doc({
				"doctype": "Stock Item History",
				"inout": 'IN',
				"item_type": self.device_type_value,
				"item": self.device_id,
				"position_type": "Cell Station",
				"position": self.parent
			}).insert()

	def on_trash(self):
		if self.device_id:
			doc = frappe.get_doc({
				"doctype": "Stock Item History",
				"inout": 'OUT',
				"item_type": self.device_type_value,
				"item": self.device_id,
				"position_type": "Cell Station",
				"position": self.parent
			}).insert()