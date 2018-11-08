var timerId;
var statusList
var TIME_REFRESH = 1500 // ms
var STATUS = {
		"1" : "idle",
		"2" : "blank",
		"3" : "testing",
		"4" : "fail",
		"5" : "pass",
	}

$(document).ready(function() {

	var i = 1
	for (var z = 1; z <= 2; z++) {
		$("#channels").append(
				'<div id="channel' + z
						+ '" class="col-md-6"></div>')
		$('#channel' + z)
				.append(
						'<div class="row" align="center">CHANNEL '
								+ z
								+ '</div><hr /><div class="row"><ul id="channel_ul'
								+ z
								+ '" class="bs-glyphicons"></ul></div>')
		for (var x = 0; x < 64; x++) {
			$('#channel_ul' + z)
					.append(
							'<li class="dut_cell active lightview" href="#chartscontainer">'
								+ '<span class="glyphicon-class">'
									+ i
								+ '</span>'
								+ '<div class="progress">'
									+ '<div id="'+ i + '"class="progress-bar dut_label" style="width: 100%">'
								+ 	'</div>' 
								+ '</div>'
							+ '</li>')
			i++;
		}
	}

	//
	// build highcharts form option
	//
	options = {
		chart : {
			renderTo : '',
			height : 300,
			zoomType: 'x'
		},
		credits: {
            enabled: false
        },
		title : {
			text : '',
			x : -20
		// center
		},
		subtitle : {
			text : '',
			x : -20
		},
		xAxis:{
			title : {
				text : 'time(s)',
				align : 'high'
			},
			tickInterval: 1,
			categories : [],
			labels: {
                rotation: -45,
                align: 'right',
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                },
                step: 'auto'
            }
		},
		yAxis : {
			title : {
				text : ''
			},
			min: 0,
			plotLines : [ {
				value : 0,
				width : 1,
				color : '#808080'
			} ]
		},
		tooltip : {
		},
		legend : {
//			layout : 'vertical',
//			align : 'right',
//			verticalAlign : 'middle',
//			borderWidth : 0
			enabled: false
		},
		series : []
	};

	$("#container1", "#container2").empty();

	$(".dut_cell").click(function(){
		time = []
		vcap = []
		temp = []
		el = $(this);
		dut_num = parseInt(el.children('span.glyphicon-class').text())
		$.ajax({
			type : "get",
			url : "/chart_data",
			data : {"id":dut_num},
			timeout : 30000,
			dataType : "json",
			success : function(data) {
				time = data.time
				vcap = data.vcap
				temp = data.temp
				current_cyc = data.cycle
				options.xAxis.categories = time
				
				//
				//	Construct VCAP chart
				//
				optionsV = options
				optionsV.chart.renderTo = "container1"
				optionsV.title.text = 'VCAP of DUT-'+ dut_num
				optionsV.subtitle.text = "CYCLE: "+ current_cyc
				optionsV.yAxis.title.text = "VCAP (V)"
				optionsV.tooltip ={formatter: function() {
//		            return '<b>'+ this.series.name +'</b><br/>'+
				    return this.x +': '+ this.y +' V';
						}
					}
				
				
				seriesV = {
						name : "CYCLE: "+ current_cyc,
						data : vcap
					}
				displaychart = new Highcharts.Chart(optionsV);
				displaychart.addSeries(seriesV);
				//
				//	Construct TEMP chart
				//
				optionsT = options
				optionsT.chart.renderTo = "container2"
				optionsT.yAxis.title.text = "Temprature (°C)"
				optionsT.title.text = 'Temprature of DUT-'+ dut_num
				optionsT.subtitle.text = "CYCLE: "+ current_cyc
				optionsT.tooltip ={formatter: function() {
//		            return '<b>'+ this.series.name +'</b><br/>'+
				    return this.x +': '+ this.y +' °C';
						}
					}
				seriesT = {
					name : "CYCLE: "+ current_cyc,
					data : temp
				}
				displaychart = new Highcharts.Chart(optionsT);
				displaychart.addSeries(seriesT);
				//
				//	Redraw
				//
				displaychart.redraw();
			},
			error : function() {
				window.clearInterval(timerId);
				alert("Request Error");
			}
		});
	});
	
	//
	// toggle real-time status of single dut when mouse on
	//

	$("div.dut_label").mouseout(function() {
		var el = $(this)
		el.popover('destroy')
	});

	$("div.dut_label").mouseover(function() {
		var el = $(this)
		el.popover("destroy")
		info =  "model : " + el.attr("model") + "<br/>"
				+ "SN : " + el.attr("sn") + "<br/>"
				+ "cycle : " + el.attr("cycle") + "<br/>"
				+ "status : " + STATUS[el.attr("status")] +"<br/>"
				+ "HWVER : " + el.attr("hwver") + "<br/>"
				+ "FWVER : " + el.attr("fwver") + "<br/>"
				+ "VCAP : " + el.attr("vcap") + "<br/>"
				+ "TEMP : " + el.attr("temp") + "<br/>"
		if(el.attr("status")=="1" ||el.attr("status")=="3" || el.attr("status")== "4" || el.attr("status")== "5"){
			el.popover({
				container: 'body',
				title : "DUT: " + el.attr("id"),
				content : info,
				html : true,
				placement : "auto right",
				delay : {
					show : 0,
					hide : 0,
				}
			}).popover('show');
		}
	});
	
	var ajax_flag = 1
	
	//
	//	refresh DUTs test status
	//
	$(function() {
		timerId = window.setInterval(refresh, TIME_REFRESH);
	});
	
	function refresh() {
		if(ajax_flag == 1){
			refreshStatus();
		}
		else{
			return
		}
	}
	
	function refreshStatus() {
		ajax_flag = 0
		$.ajax({
			type : "get",
			url : "/newstatus",
			timeout : 30000,
			dataType : "json",
			success : function(data) {
				statusList = data
				$.each(statusList, function(itemNo, item) {
					label_id = item.ID
					status = item.STATUS
					$('div.dut_label#' + label_id).attr({
						"status" : status
					})
					vcap = item.VCAP
					temp = item.TEMP
					$('div.dut_label#' + label_id).attr({
						"model" : item.MODEL,
						"sn" : item.SN,
						"status" : item.STATUS,
						"cycle" :item.CYCLE,
						"hwver" : item.HWVER,
						"fwver" : item.FWVER,
						"vcap"	: vcap,
						"temp"	: temp,
						})
				})
				$.each($("div.dut_label"),function() {
					el = $(this)
					status = el.attr("status")
					switch (status) {
					case "1":
						el.parent("div").addClass("progress-striped active");
						el.removeClass("progress-bar-success progress-bar-info progress-bar-warning progress-bar-danger");
						el.css("background-color", "");
						el.addClass("progress-bar-info");
						el.css("width", "100%");
						el.text(STATUS["1"]);
						break;
					case "2":
						el.parent("div").removeClass("progress-striped active");
						el.css("width", "100%");
						el.css("background-color", "grey");
						el.text(STATUS["2"]);
						el.removeClass("progress-bar-success progress-bar-info progress-bar-warning progress-bar-danger");
						break;
					case "3":
						el.parent("div").addClass("progress-striped active");
						el.removeClass("progress-bar-success progress-bar-info progress-bar-warning progress-bar-danger");
						el.css("background-color", "");
						el.addClass("progress-bar-warning");
						el.css("width", "100%");
						el.text(STATUS["3"]);
						break;
					case "4":
						el.parent("div").addClass("progress-striped active");
						el.removeClass("progress-bar-success progress-bar-info progress-bar-warning progress-bar-danger");
						el.css("background-color", "");
						el.addClass("progress-bar-danger");
						el.css("width", "100%");
						el.text(STATUS["4"]);
						break;
					case "5":
						el.parent("div").addClass("progress-striped active");
						el.removeClass("progress-bar-success progress-bar-info progress-bar-warning progress-bar-danger");
						el.css("background-color", "");
						el.addClass("progress-bar-success");
						el.css("width", "100%");
						el.text(STATUS["5"]);
						break;
					}
				});
				ajax_flag = 1;
			},
			error : function() {
				window.clearInterval(timerId);
				alert("Request Error");
			}
		});
		
	}
});
