/**
 * Created by cch on 17-4-17.
 */
frappe.ready(function() {
	{% for d in vsn %}
		var args = {
			sn: "{{ sn }}",
			vsn: "{{ d }}",
		}
		frappe.call({
			type: "GET",
			method: "iot.hdb.iot_device_data",
			args: args,
			callback: function (r) {
				if (!r.exc) {
					if (r._server_messages)
						frappe.msgprint(r._server_messages);
					else {
						$('#{{ d }}').bootstrapTable({
						columns: [{
							field: 'name',
							title: 'Name'
						}, {
							field: 'desc',
							title: 'Desc'
						}, {
							field: 'PV',
							title: 'Value'
						}],
						data: r.message});
					}
				}
			}
		});

	{% endfor %}
});