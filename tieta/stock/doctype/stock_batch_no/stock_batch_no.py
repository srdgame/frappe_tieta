# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StockBatchNo(Document):
	pass


def stock_batch_no_query(doctype, txt, searchfield, start, page_len, filters):
	if not filters.has_key("item_code"):
		return ""

	item_code = filters["item_code"]
	return frappe.db.sql("""select name, attribute from `tabStock Batch No`
		where item_code = %s and docstatus = 2
		and %s like %s order by name limit %s, %s""" %
		("%s", searchfield, "%s", "%s", "%s"),
		(item_code, "%%%s%%" % txt, start, page_len), as_list=1)
