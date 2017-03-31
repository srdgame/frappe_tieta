# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CellStationDeviceType(Document):
	pass


def query_types(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name, type_doc from `tabRegion`
		where docstatus = 1
		and %s like %s order by name limit %s, %s""" %
		(searchfield, "%s", "%s", "%s"),
		("%%%s%%" % txt, start, page_len), as_list=1)