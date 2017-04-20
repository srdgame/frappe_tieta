// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stock Entry', {
	setup: function(frm) {
		frm.fields_dict['items'].grid.get_field("serial_no").get_query = function (doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				filters: {
					"item_code": d.item_type
				}
			};
		};
		frm.fields_dict['items'].grid.get_field("batch_no").get_query = function (doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				filters: {
					"item_code": d.item_type
				}
			};
		};
		frm.fields_dict['order_id'].get_query = function() {
			return {
				filters: {
					"docstatus": 1
				}
			}
		};
	},
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Stock Entry", "warehouse", function(frm) {
	frappe.call({
		method: "frappe.client.get_value",
		args: {
			doctype: "Stock Warehouse",
			fieldname: "company",
			filters: { name: frm.doc.warehouse },
		},
		callback: function(r, rt) {
			if(r.message) {
				frm.set_value("company", r.message.company);
			}
		}
	});
});

frappe.ui.form.on('Stock EntryItem', {
	item_type: function(doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Stock Item",
				name: d.item_type,
				filters: {
					docstatus: 1
				}
			},
			callback: function(r, rt) {
				if(r.message) {
					frappe.model.set_value(cdt, cdn, "item_name", r.message.item_name);
					frappe.model.set_value(cdt, cdn, "uom", r.message.stock_uom);
				}
			}
		});
	}
});
