# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from iot.hdb import iot_device_tree


def get_context(context):
	if frappe.session.user == 'Guest':
		frappe.local.flags.redirect_location = "/login"
		raise frappe.Redirect

	name = frappe.form_dict.name

	context.no_cache = 1
	context.show_sidebar = False

	context.title = _("Cell Station")
	doc = frappe.get_doc("Cell Station", name)
	symlink_type = frappe.db.get_single_value('Cell Station Settings', 'symlink_device_type')

	sn = None
	for dev in doc.devices:
		if dev.device_type == symlink_type:
			sn = dev.device_id
	if sn:
		context.vsn = iot_device_tree(sn)
		context.sn = sn
	'''
	context.sn = '2-26003-161220-00002'
	context.vsn = ['2-26003-161220-00002_C2_B2']
	'''

	context.doc = doc
