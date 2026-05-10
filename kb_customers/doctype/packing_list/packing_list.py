# -*- coding: utf-8 -*-
# Copyright (c) 2023, Your Name and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class PackingList(Document):
	def get_items_from_sales_invoice(self):
		if self.no_sales_invoice:
			sales_invoice = frappe.get_doc("Sales Invoice", self.no_sales_invoice)
			if sales_invoice.docstatus == 1:  # Submitted
				self.items = []
				for item in sales_invoice.items:
					self.append("items", {
						"nama_item": item.item_name,
						"description_item": item.description,
						"qty": item.qty,
						"unit": item.uom,
						"berat_item": item.weight_per_unit * item.qty if item.weight_per_unit else 0
					})
			else:
				frappe.throw(_("Sales Invoice must be submitted"))
		else:
			frappe.throw(_("Please select a Sales Invoice"))