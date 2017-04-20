// Copyright (c) 2017, Dirk Chang and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cell Station', {
	setup: function (frm) {
		frm.fields_dict['address'].grid.get_field("province").get_query = function (doc, cdt, cdn) {
			return {
				query:"cloud.cloud.doctype.region.region.query_child_region",
				filters: {"type": "Province"}
			};
		};
		frm.fields_dict['address'].grid.get_field("city").get_query = function (doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				query:"cloud.cloud.doctype.region.region.query_child_region",
				filters: {"type": "City", "parent": d.province}
			};
		};
		frm.fields_dict['address'].grid.get_field("county").get_query = function (doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				query:"cloud.cloud.doctype.region.region.query_child_region",
				filters: {"type": "County", "parent": d.city}
			};
		};
		frm.fields_dict['address'].grid.get_field("town").get_query = function (doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				query:"cloud.cloud.doctype.region.region.query_child_region",
				filters: {"type": "Town", "parent": d.county}
			};
		};
		frm.fields_dict['address'].grid.cannot_add_rows = true;

		frm.fields_dict['devices'].grid.get_field("device_id").get_query = function (doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			if (d.device_type_value == 'Stock Item') {
				return {
					filters: {
						"name": d.device_item
					}
				};
			}
			return {
				filters: {
					"item_code": d.device_item
				}
			};
		};
	},
	refresh: function (frm) {
	},
	onload_post_render: function(frm) {
		var grid = frm.fields_dict["devices"].grid;
		grid.add_custom_button(__('Add Device Items'), function() {
			frappe.call({
				type: "GET",
				method: 'frappe.client.get_list',
				args: {
					doctype: "Cell Station Device Type",
					filters: {
						"docstatus": 1
					},
					fields: ["name", "type_item", "type_doc"]
				},
				callback: function (r) {
					var devices = frm.doc.devices;
					if (r.message) {
						$.each(r.message, function (i, d) {
							if (! $.map(devices || [], function(dev) { if(dev.device_type == d.name){ return dev } })[0]) {
								var row = frappe.model.add_child(cur_frm.doc, "Cell StationDevice", "devices");
								row.device_type = d.name;
								row.device_item = d.type_item;
								row.device_type_value = d.type_doc;
							}
						});
					}
					refresh_field("devices");
				}
			});
		});
		grid.custom_buttons[__('Add Device Items')].removeClass("btn-default");
		grid.custom_buttons[__('Add Device Items')].addClass("btn-warning");
	},
	update_address: function(frm, row) {
		frappe.call({
			type: "GET",
			method: "cloud.cloud.doctype.region_address.region_address.get_address_text",
			args: row,
			callback: function (r, rt) {
				if (r.message) {
					frm.set_value("address_text", r.message)
				}
			}
		});
	}
});

frappe.ui.form.on('Cell StationDevice', {
	device_type: function(doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.call({
			type: "GET",
			method: "frappe.client.get",
			args: {
				doctype: "Cell Station Device Type",
				name: d.device_type,
				filters: {
					docstatus: 1
				}
			},
			callback: function(r, rt) {
				if(r.message) {
					frappe.model.set_value(cdt, cdn, "device_item", r.message.type_item);
					frappe.model.set_value(cdt, cdn, "device_type_value", r.message.type_doc);
				}
			}
		});
	}
});


frappe.ui.form.on('Region Address', {
	province: function (doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.model.set_value(cdt, cdn, "city", "");
		frappe.model.set_value(cdt, cdn, "county", "");
		frappe.model.set_value(cdt, cdn, "town", "");
		cur_frm.events.update_address(cur_frm, d);
	},
	city: function (doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.model.set_value(cdt, cdn, "county", "");
		frappe.model.set_value(cdt, cdn, "town", "");
		cur_frm.events.update_address(cur_frm, d);
	},
	county: function (doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		frappe.model.set_value(cdt, cdn, "town", "");
		cur_frm.events.update_address(cur_frm, d);
	},
	town: function (doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		cur_frm.events.update_address(cur_frm, d);
	},
	address: function (doc, cdt, cdn) {
		var d = locals[cdt][cdn];
		cur_frm.events.update_address(cur_frm, d);
	}
});