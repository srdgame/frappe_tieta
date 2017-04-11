# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document


class StockEntry(Document):
	def validate(self):
		if self.purpose == 'Material Transfer' and not self.source_warehouse:
			throw(_("Source Warehouse is required"))
		for item in self.items:
			doc = frappe.get_doc("Stock Serial No", item.serial_no)
			if not doc:
				throw(_("Serial NO is not validate! {0}").format(item.serial_no))
			if doc.warehouse and doc.warehouse != self.source_warehouse:
				throw(_("Serial NO {0} is not in Warehouse {1} but in {2}").format(
					item.serial_no, self.source_warehouse, doc.warehouse))

	def on_submit(self):
		for item in self.items:
			doc = frappe.get_doc("Stock Serial No", item.serial_no)
			if not doc:
				throw(_("Serial NO is not validate! {0}").format(item.serial_no))
			if doc.warehouse and doc.warehouse != self.source_warehouse:
				throw(_("Serial NO {0} is not in Warehouse {1} but in {2}").format(
					item.serial_no, self.source_warehouse, doc.warehouse))
			doc.warehouse = self.warehouse
			doc.save()

	def on_cancel(self):
		for item in self.items:
			doc = frappe.get_doc("Stock Serial No", item.serial_no)
			if not doc:
				throw(_("Serial NO is not validate! {0}").format(item.serial_no))
			if doc.warehouse != self.warehouse:
				throw(_("Serial NO {0} is not in Warehouse {1}").format(
					item.serial_no, doc.warehouse))
			doc.warehouse = self.source_warehouse
			doc.save()