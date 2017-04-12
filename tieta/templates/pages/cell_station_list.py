# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def get_context(context):
	if frappe.session.user == 'Guest':
		frappe.local.flags.redirect_location = "/login"
		raise frappe.Redirect

	user_roles = frappe.get_roles(frappe.session.user)
	if 'TieTa User' not in user_roles:
		raise frappe.PermissionError

	txt = frappe.form_dict.txt or ""
	rgn = frappe.form_dict.rgn or "RGN000001"
	rgn_type = frappe.form_dict.rgn_type or "province"
	start = frappe.form_dict.start or 0
	page_length = frappe.form_dict.page_length or 20
	order_by = frappe.form_dict.order_by or "modified desc"

	context.no_cache = 1
	context.show_sidebar = True

	projects = None
	if frappe.session.user != 'Administrator':
		projects = [d.project for d in frappe.get_doc('Cell Station Admin', frappe.session.user).projects]
	else:
		projects = [d[0] for d in frappe.db.get_values('Cloud Project', {"enabled":1}, 'name')]

	context.title = _("Cell Station List")
	rgn_key = 'region_address.' + rgn_type
	context.cell_list = frappe.db.sql('''select distinct station.*
		from `tabCell Station` station, `tabRegion Address` region_address
		where
			station.name = region_address.parent
			and {3} = %(rgn)s and station.project in {4}
			and station.station_name like %(txt)s order by station.{0}
			limit {1}, {2}
		'''.format(order_by, start, page_length, rgn_key, "('"+"','".join(projects)+"')"),
			{'rgn' : rgn, 'txt' : "%%%s%%" % txt},
			as_dict=True,
			update={'doctype' : 'Cell Station'})
