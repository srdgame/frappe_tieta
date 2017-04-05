# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StockDeliveryOrder(Document):
	def on_cancel(self):
		if self.order_source_type == 'Tickets Ticket':
			doc = frappe.get_doc('Tickets Ticket', self.order_source_id)
			doc.run_method("on_delivery_order_cancel")

	def on_commit(self):
		if self.order_source_type == 'Tickets Ticket':
			doc = frappe.get_doc('Tickets Ticket', self.order_source_id)
			doc.run_method("on_delivery_order_commit", self)