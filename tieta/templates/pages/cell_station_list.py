# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def get_context(context):
	txt = frappe.form_dict.txt or ""
	rgn = frappe.form_dict.rgn or "RGN000001"
	rgn_type = frappe.form_dict.rgn_type or "province"
	start = frappe.form_dict.start or 0
	page_length = frappe.form_dict.page_length or 20
	order_by = frappe.form_dict.order_by or "modified desc"

	context.no_cache = 1
	context.show_sidebar = True

	context.title = _("Cell Station List")
	rgn_key = 'region_address.' + rgn_type
	context.cell_list = frappe.db.sql('''select distinct station.*
		from `tabCell Station` station, `tabRegion Address` region_address
		where
			station.name = region_address.parent
			and {3} = %(rgn)s
			and station.station_name like %(txt)s order by station.{0}
			limit {1}, {2}
		'''.format(order_by, start, page_length, rgn_key),
			{'rgn' : rgn, 'txt' : "%%%s%%" % txt},
			as_dict=True,
			update={'doctype' : 'Cell Station'})
