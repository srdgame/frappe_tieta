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

frappe.ui.form.on("Stock Serial No", "item_code", function(frm) {
	frappe.call({
		type: "GET",
		method:'frappe.desk.search.search_link',
		args: {
			"doctype": "Stock Item Attribute",
			"txt": "",
			"filters": {
				"type": "serial",
				"item_code": frm.doc.item_code
			}
		},
		callback: function (r) {
			alert(r.message);
			frm.set_value("attributes" ,"");
			if (r.message) {
				$.each(r.message, function(i, d) {
					alert( d.attribute);
					var row = frappe.model.add_child(cur_frm.doc, "Stock Batch NoAttribute", "attributes");
					row.attribute = d.attribute;
				});
			}
			refresh_field("attributes");
		}
	});
});
