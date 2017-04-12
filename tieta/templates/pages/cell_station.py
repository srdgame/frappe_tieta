# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from iot.hdb import iot_device_tree

def get_context(context):
	name = frappe.form_dict.name

	context.no_cache = 1
	context.show_sidebar = True

	context.title = _("Cell Station")
	doc = frappe.get_doc("Cell Station", name)
	sn = None
	for dev in doc.devices:
		if dev.device_type == 'SymLink':
			sn = dev.device_id
	if sn:
		context.vsn = iot_device_tree(sn)
		context.sn = sn

	context.doc = doc
