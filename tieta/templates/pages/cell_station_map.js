frappe.ready(function() {
	var map = new BMap.Map("baiduMap");
	map.centerAndZoom(new BMap.Point(116.3252, 40.045103), 5);
	map.enableScrollWheelZoom();

	var opts = {
		width : 250,     // 信息窗口宽度
		height: 120,     // 信息窗口高度
		//title : "设备信息" , // 信息窗口标题
		enableMessage:true//设置允许信息窗发送短息
	};
	function addClickHandler(content,marker){
		marker.addEventListener("click",function(e){
			openInfo(content,e)}
		);
	}
	function openInfo(content,e){
		var p = e.target;
		var point = new BMap.Point(p.getPosition().lng, p.getPosition().lat);
		var infoWindow = new BMap.InfoWindow(content,opts);  // 创建信息窗口对象
		map.openInfoWindow(infoWindow,point); //开启信息窗口
	}

	frappe.call({
		type: "GET",
		method: "tieta.tieta.doctype.cell_station.cell_station.list_station_map",
		callback: function(r) {
			if(!r.exc) {
				if(r._server_messages)
					frappe.msgprint(r._server_messages);
				else {
					var markers = [];
					var stations = r.message;
					for (var cs in stations) {
						pt = new BMap.Point(stations[cs].longitude, stations[cs].latitude);
						var myIcon = new BMap.Icon("/files/access-point.png", new BMap.Size(32,32));
						var marker = new BMap.Marker(pt,{icon:myIcon});
						var content = "<a href='/iot_stations/" + stations[cs].sn + "'>" +
							"<h4 style='margin:0 0 5px 0;padding:0.2em 0'>" +
							stations[cs].cs_name + "</h4></a>" +
							"<p> Status : " + stations[cs].csice_status + "</p>" +
							"<p> Last Updated : " + stations[cs].last_updated + "</p>";

						addClickHandler(content, marker);
						markers.push(marker);
					}
					//最简单的用法，生成一个marker数组，然后调用markerClusterer类即可。
					var markerClusterer = new BMapLib.MarkerClusterer(map, {markers: markers});
				}
			} else {
				if(r._server_messages)
					frappe.msgprint(r._server_messages);
				else
					frappe.msgprint(r.message);
			}
		}
	});
});