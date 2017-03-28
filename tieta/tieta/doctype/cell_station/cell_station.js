// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cell Station', {
	setup: function(frm) {
		frm.fields_dict['province'].get_query  = function(){
			return {
				query:"tieta.tieta.doctype.region.region.query_province",
			};
		};
		frm.fields_dict['city'].get_query  = function(){
			return {
				query:"tieta.tieta.doctype.region.region.query_city",
				filters: {"province": frm.doc.province}
			};
		};
		frm.fields_dict['county'].get_query  = function(){
			return {
				query:"tieta.tieta.doctype.region.region.query_county",
				filters: {"city": frm.doc.city}
			};
		};
		frm.fields_dict['town'].get_query  = function(){
			return {
				query:"tieta.tieta.doctype.region.region.query_town",
				filters: {"county": frm.doc.city}
			};
		};
	},
	refresh: function(frm) {

	}
});
