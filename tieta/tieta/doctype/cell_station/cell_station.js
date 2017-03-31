// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cell Station', {
	setup: function (frm) {
		frm.fields_dict['province'].get_query = function () {
			return {
				query: "tieta.tieta.doctype.region.region.query_province",
			};
		};
		frm.fields_dict['city'].get_query = function () {
			return {
				query: "tieta.tieta.doctype.region.region.query_city",
				filters: {"province": frm.doc.province}
			};
		};
		frm.fields_dict['county'].get_query = function () {
			return {
				query: "tieta.tieta.doctype.region.region.query_county",
				filters: {"city": frm.doc.city}
			};
		};
		frm.fields_dict['town'].get_query = function () {
			return {
				query: "tieta.tieta.doctype.region.region.query_town",
				filters: {"county": frm.doc.county}
			};
		};
	},
	refresh: function (frm) {

	},
});

frappe.ui.form.on('Cell StationDevice', {
	refresh: function(frm) {
		frm.add_custom_button(__("Add List Type"), function(){});
	},
	device_type: function(doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.call({
			method: "frappe.client.get_value",
			args: {
				doctype: "Cell Station Device Type",
				fieldname: "type_doc",
				filters: {
					name: d.device_type,
					docstatus: 1,
				},
			},
			callback: function(r, rt) {
				if(r.message) {
					frappe.model.set_value(cdt, cdn, "device_type_value", r.message.type_doc);
					frappe.model.set_value(cdt, cdn, "device_name", d.device_type);
				}
			}
		});
	}
});


