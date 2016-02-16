var Script = function () {
$(function() {
  
  var d1 = [];
  for (var i = 0; i < 14; i += 0.5) {
    d1.push([i, Math.sin(i)]);
  }
  
  var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];
  
  var d3 = [];
  for (var i = 0; i < 14; i += 0.5) {
    d3.push([i, Math.cos(i)]);
  }
  
  var d4 = [];
  for (var i = 0; i < 14; i += 0.1) {
    d4.push([i, Math.sqrt(i * 10)]);
  }
  
  var d5 = [];
  for (var i = 0; i < 14; i += 0.5) {
    d5.push([i, Math.sqrt(i)]);
  }
  
  var d6 = [];
  for (var i = 0; i < 14; i += 0.5 + Math.random()) {
    d6.push([i, Math.sqrt(2*i + Math.sin(i) + 5)]);
  }
  
  $.plot("#chart-2", [{
    data: d1,
    lines: { show: true, fill: true }
  }, {
    data: d2,
    bars: { show: true }
  }, {
    data: d3,
    points: { show: true }
  }, {
    data: d4,
    lines: { show: true }
  }, {
    data: d5,
    lines: { show: true },
    points: { show: true }
  }, {
    data: d6,
    lines: { show: true, steps: true }
  }]);
  
  // Add the Flot version string to the footer
  
  $("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
});

$(function() {
  
  var data = [];
        var series = Math.floor(Math.random()*10)+1;
        for( var i = 0; i<series; i++)
        {
            data[i] = { label: "Series"+(i+1), data: Math.floor(Math.random()*100)+1 }
        }
  $.plot($("#chart-5"), data,
            {
                series: {
                    pie: {
                        show: true
                    }
                },
                legend: {
                    show: false
                }
            });
  
});
  
}();