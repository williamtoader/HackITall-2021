let app_chart_method = {
	update: null
}
let load_app_chart = function (dataStr) {
	var barCount = 60;
	var initialDateStr = '01 Apr 2017 00:00 Z';

	var ctx = document.getElementById('chart').getContext('2d');
	ctx.canvas.width = 1000;
	ctx.canvas.height = 250;

	var chart = new Chart(ctx, {
		type: 'candlestick',
		data: {
			datasets: [{
				label: 'Grafic',
				data: JSON.parse(dataStr)
			}]
		}
	});


	

	function getRandomData(dateStr, count) {
		var date = luxon.DateTime.fromISO(dateStr);
		var data = [];
		
		return data;
	}

	app_chart_method.update = function (dataStr) {
		var dataset = chart.config.data.datasets[0];

		// candlestick vs ohlc
		
		dataset.type = "candlestick";

		// linear vs log
		
		chart.config.options.scales.y.type = "linear";

		// color
		//var colorScheme = document.getElementById('color-scheme').value;
		if ('neon' === 'neon') {
			dataset.color = {
				up: '#01ff01',
				down: '#fe0000',
				unchanged: '#999',
			};
		} else {
			delete dataset.color;
		}



		// mixed charts

		var mixed = 'false';
		if (mixed === 'true') {
			chart.config.data.datasets = [
				{
					label: 'CHRT - Chart.js Corporation',
					data: barData
				},
				{
					label: 'Close price',
					type: 'line',
					data: lineData()
				}
			]
		}
		else {
			chart.config.data.datasets = [
				{
					label: 'Grafic',
					data: JSON.parse(dataStr)
				}
			]
		}

		chart.update();
	};

}