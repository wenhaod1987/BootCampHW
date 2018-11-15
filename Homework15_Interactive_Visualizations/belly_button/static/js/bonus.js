function buildGauge(data){
	
	var level = data*180/9;

	// Trig to calc meter point
	var degrees = 180 - level,
	     radius = .5;
	var radians = degrees * Math.PI / 180;
	var x = radius * Math.cos(radians);
	var y = radius * Math.sin(radians);

	
	var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
	     pathX = String(x),
	     space = ' ',
	     pathY = String(y),
	     pathEnd = ' Z';
	var path = mainPath.concat(pathX,space,pathY,pathEnd);

	var data1 = [{ type: 'scatter',
	   x: [0], y:[0],
	    marker: {size: 28, color:'850000'},
	    showlegend: false},
	  { values: [1, 1, 1, 1, 1, 1, 1,1,1,9],
	  rotation: 90,
	  text: ['8-9', '7-8', '6-7', '5-6',
	            '4-5', '3-4', '2-3','1-2','0-1',''],
	  textinfo: 'text',
	  textposition:'inside',
	  marker: {colors:['rgba(14, 127, 0, .5)', 'rgba(54, 138, 18, .5)',
	  					'rgba(110, 154, 22, .5)',
	                         'rgba(170, 202, 42, .5)', 'rgba(193, 205 87, .5)',
	                         'rgba(202, 209, 105, .5)',
	                         'rgba(210, 206, 145, .5)', 'rgba(222, 218, 198, .5)',
	                         'rgba(230, 230, 210, .5)',
	                         'rgba(255, 255, 255, 0)']},
	  hole: .5,
	  type: 'pie',
	  showlegend: false
	}];

	var layout = {
	  shapes:[{
	      type: 'path',
	      path: path,
	      fillcolor: '850000',
	      line: {
	        color: '850000'
	      }
	    }],
	  title: "<b>Belly Button Washing Frequency</b><br>Scrubs per Week",
	  //subtitle:"Scrubs per Week",

	  height: 550,
	  width: 550,
	  xaxis: {zeroline:false, showticklabels:false,
	             showgrid: false, range: [-1, 1]},
	  yaxis: {zeroline:false, showticklabels:false,
	             showgrid: false, range: [-1, 1]}
	};

	Plotly.newPlot('gauge', data1, layout);
	}
