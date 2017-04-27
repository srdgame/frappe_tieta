# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from tieta.tieta.doctype.cell_station.cell_station import search_station


def get_context(context):
	if frappe.session.user == 'Guest':
		frappe.local.flags.redirect_location = "/login"
		raise frappe.Redirect

	context.no_cache = 1
	context.show_sidebar = False

	context.title = _("Cell Station List")
	context.cell_list = search_station(**frappe.form_dict)