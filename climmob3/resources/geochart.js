
$('.maps').each(function() {

    google.charts.load('upcoming', {'packages':['geochart', "corechart"]});
    google.charts.setOnLoadCallback(drawRegionsMap);

    function drawRegionsMap() {
        var val = $('.maps').attr('data-count');
        val=val.split(";");
        var reg = val[0];
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Country');
        var rows = new Array()
        for (var i=1;i< val.length;i++){

            rows.push([val[i]]);
        }
        data.addRows(rows);
        var options = {
            legend: "none",
            //colorAxis: {colors: ['#e7711c', '#4374e0', "red"]} ,
            region:reg,
            defaultColor: '#EC971F',


        };

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);

    }

});



