// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stock Serial No', {
	setup: function(frm) {
		frm.fields_dict['attributes'].grid.get_field("attribute").get_query  = function(){
			return {
				filters: {
					"type": "serial",
					"item_code": frm.doc.item_code
				}
			};
		};
	},
	refresh: function(frm) {

	}
});
