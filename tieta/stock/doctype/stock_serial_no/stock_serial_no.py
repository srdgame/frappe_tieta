# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StockSerialNo(Document):
	def on_update(self):
		org_warehouse = self.get("warehouse")
		warehouse = self.warehouse
		if org_warehouse and org_warehouse != warehouse:
			doc = frappe.get_doc({
				"doctype": "Stock Item History",
				"inout": 'OUT',
				"item_type": "Stock Serial No",
				"item": self.name,
				"position_type": "Stock Warehouse",
				"position": org_warehouse
			}).insert()
		if warehouse:
			doc = frappe.get_doc({
				"doctype": "Stock Item History",
				"inout": 'IN',
				"item_type": "Stock Serial No",
				"item": self.name,
				"position_type": "Stock Warehouse",
				"position": warehouse
			}).insert()


def stock_serial_no_query(doctype, txt, searchfield, start, page_len, filters):
	if not filters:
		return frappe.db.sql("""select name, warehouse from `tabStock Serial No`
			where docstatus = 1
			and %s like %s order by name limit %s, %s""" %
			(searchfield, "%s", "%s", "%s"),
			("%%%s%%" % txt, start, page_len), as_list=1)

	item_code = filters["item_code"] or ''
	return frappe.db.sql("""select name, warehouse from `tabStock Serial No`
		where item_code = %s and docstatus = 1
		and %s like %s order by name limit %s, %s""" %
		("%s", searchfield, "%s", "%s", "%s"),
		(item_code, "%%%s%%" % txt, start, page_len), as_list=1)