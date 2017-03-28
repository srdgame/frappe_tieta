# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Region(Document):
	pass


def query_province(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name, description from `tabRegion`
		where type = 'Province'
		and %s like %s order by name limit %s, %s""" %
		(searchfield, "%s", "%s", "%s"),
		("%%%s%%" % txt, start, page_len), as_list=1)


def query_city(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name, description from `tabRegion`
		where type = 'City' and region_parent = %s
		and %s like %s order by name limit %s, %s""" %
		("%s", searchfield, "%s", "%s", "%s"),
		(filters["province"], "%%%s%%" % txt, start, page_len), as_list=1)


def query_town(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name, description from `tabRegion`
		where type = 'Town' and region_parent = %s
		and %s like %s order by name limit %s, %s""" %
		("%s", searchfield, "%s", "%s", "%s"),
		(filters["city"], "%%%s%%" % txt, start, page_len), as_list=1)