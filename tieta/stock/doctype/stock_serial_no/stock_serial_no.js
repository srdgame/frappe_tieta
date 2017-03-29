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
		if (ss_item_code != frm.doc.item_code) {
			ss_item_code = frm.doc.item_code;
			frappe.call({
				method: 'tieta.stock.doctype.stock_item_attribute.stock_item_attribute.stock_item_attribute_query',
				args: {
					"type": "serial",
					"item_code": ss_item_code
				},
				callback: function (r) {
					frm.set_value("attributes" ,"");
					if (r.message) {
						$.each(r.message, function(i, d) {
							var row = frappe.model.add_child(cur_frm.doc, "Stock Batch NoAttribute", "attributes");
							row.attribute = d.attribute;
						});
					}
					refresh_field("attributes");
				}
			});
		}
	}
});

frappe.ui.form.on("Stock Serial No", "item_code", function(frm) {
	alert(frm.doc.item_code);
});