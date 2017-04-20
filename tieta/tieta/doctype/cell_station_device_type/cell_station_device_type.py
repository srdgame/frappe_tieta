# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CellStationDeviceType(Document):
	def validate(self):
		self.type_doc = 'Stock Item'
		doc = frappe.get_doc('Stock Item', self.type_item)
		if doc.has_batch_no:
			self.type_doc = 'Stock Batch No'
		if doc.has_serial_no:
			self.type_doc = 'Stock Serial No'


def query_types(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name, type_doc from `tabCell Station Device Type`
		where docstatus = 1
		and %s like %s order by name limit %s, %s""" %
		(searchfield, "%s", "%s", "%s"),
		("%%%s%%" % txt, start, page_len), as_list=1)