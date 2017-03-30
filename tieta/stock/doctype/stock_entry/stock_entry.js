// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stock Entry', {
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
