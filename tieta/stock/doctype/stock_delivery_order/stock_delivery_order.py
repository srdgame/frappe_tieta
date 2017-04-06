# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document
from frappe.desk.form import assign_to


class StockDeliveryOrder(Document):
	def on_cancel(self):
		if self.order_source_type == 'Tickets Ticket':
			doc = frappe.get_doc('Tickets Ticket', self.order_source_id)
			doc.run_method("on_delivery_order_cancel")

	def on_submit(self):
		if not self.warehouse:
			throw(_("Ware house is required!!"))
		if self.order_source_type == 'Tickets Ticket':
			doc = frappe.get_doc('Tickets Ticket', self.order_source_id)
			doc.run_method("on_delivery_order_commit", self)
			try:
				assign_to.add({
					'assign_to': self.owner,
					'doctype': self.doctype,
					'name': self.name,
					'description': _("Delivery Order approved!"),
					'date': self.planned_date,
					'priority': 'High',
					'notify': 0
				})
			except assign_to.DuplicateToDoError:
				frappe.message_log.pop()
				pass