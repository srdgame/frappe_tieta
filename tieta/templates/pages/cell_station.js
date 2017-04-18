/**
 * Created by 维康 on 2017/4/1.
 */

var tags = '{"tags":[{"name":"Us01","desc":"\u5355\u4f53\u7535\u538b01"},{"name":"Us02","desc":"\u5355\u4f53\u7535\u538b02"},{"name":"Us03","desc":"\u5355\u4f53\u7535\u538b03"},{"name":"Us04","desc":"\u5355\u4f53\u7535\u538b04"},{"name":"Us05","desc":"\u5355\u4f53\u7535\u538b05"},{"name":"Us06","desc":"\u5355\u4f53\u7535\u538b06"},{"name":"Us07","desc":"\u5355\u4f53\u7535\u538b07"},{"name":"Us08","desc":"\u5355\u4f53\u7535\u538b08"},{"name":"Us09","desc":"\u5355\u4f53\u7535\u538b09"},{"name":"Us10","desc":"\u5355\u4f53\u7535\u538b10"},{"name":"Us11","desc":"\u5355\u4f53\u7535\u538b11"},{"name":"Us12","desc":"\u5355\u4f53\u7535\u538b12"},{"name":"Us13","desc":"\u5355\u4f53\u7535\u538b13"},{"name":"Us14","desc":"\u5355\u4f53\u7535\u538b14"},{"name":"Us15","desc":"\u5355\u4f53\u7535\u538b15"},{"name":"Us16","desc":"\u5355\u4f53\u7535\u538b16"},{"name":"Ts01","desc":"\u5355\u4f53\u6e29\u5ea601"},{"name":"Ts02","desc":"\u5355\u4f53\u6e29\u5ea602"},{"name":"Ts03","desc":"\u5355\u4f53\u6e29\u5ea603"},{"name":"Ts04","desc":"\u5355\u4f53\u6e29\u5ea604"},{"name":"Ts05","desc":"\u5355\u4f53\u6e29\u5ea605"},{"name":"Ts06","desc":"\u5355\u4f53\u6e29\u5ea606"},{"name":"Ts07","desc":"\u5355\u4f53\u6e29\u5ea607"},{"name":"Ts08","desc":"\u5355\u4f53\u6e29\u5ea608"},{"name":"Tenv","desc":"\u73af\u5883\u6e29\u5ea6"},{"name":"Usmax","desc":"\u5355\u4f53\u7535\u538b\u6700\u5927\u503c"},{"name":"Usmin","desc":"\u5355\u4f53\u7535\u538b\u6700\u5c0f\u503c"},{"name":"Tshi","desc":"\u5355\u4f53\u6e29\u5ea6\u6700\u9ad8\u503c"},{"name":"Tslo","desc":"\u5355\u4f53\u6e29\u5ea6\u6700\u4f4e\u503c"},{"name":"UB","desc":"\u7535\u6c60\u7ec4\u7535\u538b"},{"name":"UBL","desc":"\u6bcd\u7ebf\u7535\u538b"},{"name":"Icc","desc":"\u5145\u7535\u7535\u6d41"},{"name":"Ifd","desc":"\u653e\u7535\u7535\u6d41"},{"name":"SOC","desc":"\u5269\u4f59\u5bb9\u91cf%"},{"name":"CMax","desc":"\u989d\u5b9a\u5bb9\u91cfAh"},{"name":"CLeft","desc":"\u5269\u4f59\u5bb9\u91cf"},{"name":"BNo","desc":"\u7535\u6c60\u7ec4\u53f7"}]}'
var tags_json= JSON.parse(tags).tags;
var symlink_tags = '{"tags":[{"tid":21,"name":"status","desc":"\u72b6\u6001"},{"tid":21,"name":"transpdatas","desc":"\u53d8\u5316\u6570\u636e"},{"tid":21,"name":"transprt","desc":"\u5b9e\u65f6\u4f20\u8f93"},{"tid":21,"name":"transpcc","desc":"\u65ad\u7f13\u4f20\u8f93"},{"tid":21,"name":"transflowup","desc":"\u4e0a\u884c\u6d41\u91cf"},{"tid":21,"name":"transflowdn","desc":"\u4e0b\u884c\u6d41\u91cf"},{"tid":10,"name":"AlmAIL1CTR","desc":"\u6a21\u62df\u91cf\u4e00\u7ea7\u62a5\u8b66\u8ba1\u6570\u5668"},{"tid":10,"name":"AlmAIL2CTR","desc":"\u6a21\u62df\u91cf\u4e8c\u7ea7\u62a5\u8b66\u8ba1\u6570\u5668"},{"tid":10,"name":"AlmDICTR","desc":"\u6570\u5b57\u91cf\u62a5\u8b66\u8ba1\u6570\u5668"},{"tid":10,"name":"AlmXHCTR","desc":"\u4fe1\u53f7\u91cf\u62a5\u8b66\u8ba1\u6570\u5668"},{"tid":10,"name":"CpuScanCnt","desc":"\u5185\u6838\u8ba1\u6570\u5668"},{"tid":10,"name":"CalRPFIDCnt","desc":"RapidFID\u8ba1\u6570\u5668"},{"tid":10,"name":"CalFSDCnt","desc":"FSD\u8ba1\u6570\u5668"},{"tid":10,"name":"CalFSBCnt","desc":"FSB\u8ba1\u6570\u5668"},{"tid":10,"name":"CalSOECnt","desc":"SOE\u8ba1\u6570\u5668"},{"tid":10,"name":"RMClientCnt","desc":"\u5728\u7ebf\u5ba2\u6237\u7aef\u6570\u91cf"},{"tid":10,"name":"DeviceSN","desc":"\u8bbe\u5907\u5e8f\u5217\u53f7"},{"tid":10,"name":"CpuLoad","desc":"CPU\u4f7f\u7528\u7387"},{"tid":10,"name":"SysUptime","desc":"\u8bbe\u5907\u5f00\u673a\u65f6\u95f4"},{"tid":10,"name":"SysTotalRam","desc":"\u7cfb\u7edf\u5185\u5b58\u603b\u91cf"},{"tid":10,"name":"SysFreeRam","desc":"\u7cfb\u7edf\u5269\u4f59\u5185\u5b58"},{"tid":10,"name":"SDCardFree","desc":"SD\u5361\u5269\u4f59\u5bb9\u91cf"},{"tid":10,"name":"SWRModule","desc":"SWR\u72b6\u6001\u901a\u9053"},{"tid":10,"name":"DMCtrl","desc":"\u8fdc\u7a0b\u7ef4\u62a4\u63a7\u5236"},{"tid":10,"name":"Config","desc":"\u8fdc\u7a0b\u914d\u7f6e\u63a5\u53e3"},{"tid":10,"name":"SWRBlob","desc":"SWR\u7ef4\u62a4\u63a5\u53e3"},{"tid":10,"name":"SWRCells","desc":"SWR\u63a7\u5236\u6388\u6743\u624b\u673a\u5217\u8868"},{"tid":10,"name":"LicInfo","desc":"\u8bbe\u5907\u6388\u6743\u4fe1\u606f"},{"tid":10,"name":"LisDecode","desc":"\u6388\u6743\u89e3\u7801\u901a\u9053"},{"tid":10,"name":"pcid","desc":"\u8bbe\u5907\u6807\u8bc6"},{"tid":10,"name":"RDDForbid","desc":"\u70ed\u5907\u5197\u4f59\u505c\u8fd0"},{"tid":10,"name":"RDDMode","desc":"\u8fd0\u884c\u6a21\u5f0f"},{"tid":10,"name":"BSPos","desc":"\u57fa\u7ad9\u5b9a\u4f4d"},{"tid":10,"name":"CSQ","desc":"\u65e0\u7ebf\u4fe1\u53f7\u5f3a\u5ea6"},{"tid":10,"name":"IMEI","desc":"\u65e0\u7ebf\u4e32\u53f7"},{"tid":11,"name":"C2.IoCtrl","desc":"\u901a\u9053 \u63a7\u5236\u91cf"},{"tid":11,"name":"C2.IoStatus","desc":"\u901a\u9053 \u901a\u8baf\u72b6\u6001"},{"tid":11,"name":"C2.IoGprsStatus","desc":"\u901a\u9053 GRPS\u901a\u8baf\u72b6\u6001"},{"tid":11,"name":"C2.IoValid","desc":"\u901a\u9053 \u8fd0\u884c\u72b6\u6001"},{"tid":11,"name":"C2.IoPortMR","desc":"\u901a\u9053 \u4e3b\u5907\u7aef\u53e3\u72b6\u6001"},{"tid":11,"name":"C2.IoPortStatus","desc":"\u901a\u9053 \u7aef\u53e3\u72b6\u6001"},{"tid":11,"name":"C2.IoSndBytes","desc":"\u901a\u9053 \u7aef\u53e3\u53d1\u9001\u5b57\u8282\u8ba1\u6570"},{"tid":11,"name":"C2.IoRevBytes","desc":"\u901a\u9053 \u7aef\u53e3\u63a5\u6536\u5b57\u8282\u8ba1\u6570"},{"tid":11,"name":"C2.IoSndPacks","desc":"\u901a\u9053 \u53d1\u9001\u5305\u6570"},{"tid":11,"name":"C2.IoRevPacks","desc":"\u901a\u9053 \u63a5\u6536\u5305\u6570"},{"tid":11,"name":"C2.IoCommSusPer","desc":"\u901a\u9053 \u901a\u8baf\u6210\u529f\u7387"},{"tid":11,"name":"C2.B2.IoCtrl","desc":"\u901a\u9053\u8bbe\u5907 \u63a7\u5236\u91cf"},{"tid":11,"name":"C2.B2.IoStatus","desc":"\u901a\u9053\u8bbe\u5907 \u72b6\u6001"},{"tid":11,"name":"C2.B2.IoValid","desc":"\u901a\u9053\u8bbe\u5907 \u8fd0\u884c\u72b6\u6001"},{"tid":11,"name":"C2.B2.IoSendPacks","desc":"\u901a\u9053\u8bbe\u5907 \u53d1\u9001\u5305\u6570"},{"tid":11,"name":"C2.B2.IoRevPacks","desc":"\u901a\u9053\u8bbe\u5907 \u63a5\u6536\u5305\u6570"},{"tid":11,"name":"C2.B2.IoCommSusPer","desc":"\u901a\u9053\u8bbe\u5907 \u901a\u8baf\u6210\u529f\u7387"}]}'
var symlink_tags_json= JSON.parse(symlink_tags).tags;

function creat_taglist(tags) {
	
	//console.log(tags_json);
	
	var divstring1 = '<div class="col-xs-12 col-sm-6"><div class="col-xs-6 col-sm-6">'
	var divstring2 = '：</div><div class="col-xs-6 col-sm-6"><span id="'
	var divstring3 = '">未初始化</span></div></div>'
	
	for (var i=0;i<tags_json.length;i++)
	{
		var divstring = divstring1 + tags_json[i].desc + divstring2 + tags_json[i].name + divstring3;
		//$("#tree").html(divstring);  
		 $(divstring).appendTo("#taglist");
	
	}
	
		for (var i=0;i<symlink_tags_json.length;i++)
	{
		var divstring = divstring1 + symlink_tags_json[i].desc + divstring2 + symlink_tags_json[i].name + divstring3;
		//$("#tree").html(divstring);  
		 $(divstring).appendTo("#symlink");
	
	}
}


function update_Battery() {

	    frappe.call({
	    	type: "GET",
	    	method: 'iot.hdb.iot_device_data',
	    	//btn: $(".btn-test"),
	    	args: {
	    		'sn': '{{ sn }}',
	    		'vsn': '{{ vsn[0] }}',
	    		'filters': {
	    			
	    		},
	    		'fieldname': [
	    		]
	    	},
	    	callback: function(r) {
	    		//console.log(r.message.UB.PV);	    		
	    		//var ubval = $("#ub").text();
	    		//console.log(ubval);	    		
				    for (var i=0;i<tags_json.length;i++)
				{
					var dd = '#' + tags_json[i].name;
					$(dd).html(r.message[tags_json[i].name].PV);
				}
				    		
	    	}
	    });
    
	    frappe.call({
	    	type: "GET",
	    	method: 'iot.hdb.iot_device_data',
	    	//btn: $(".btn-test"),
	    	args: {
	    		'sn': '{{ sn }}',
	    		'vsn': '{{ sn }}',
	    		'filters': {
	    			
	    		},
	    		'fieldname': [
	    		]
	    	},
	    	callback: function(r) {
	    		//console.log(r.message);	
	    		//console.log(r.message['C2.B2.IoCommSusPer']);	
				    for (var i=0;i<symlink_tags_json.length;i++)
				{
					var dd = '#' + symlink_tags_json[i].name;
					//console.log(symlink_tags_json[i].name);
					//console.log(r.message[symlink_tags_json[i].name]);
					//console.log(r.message[symlink_tags_json[i].name].PV);
					$(dd).html(r.message[symlink_tags_json[i].name].PV);
				}
				    		
	    	}
	    });
	    
}



frappe.ready(function() {
	creat_taglist(tags);
	update_Battery();
    vt = setInterval("update_Battery()",2000);	



	//先 var unixTimestamp = new Date(Unix timestamp * 1000) 然后 commonTime = unixTimestamp.toLocaleString()
	//var unixTimestamp = new Date(1492447060 * 1000);
	//var commonTime = unixTimestamp.toLocaleString();
	//console.log(commonTime);
	
})
