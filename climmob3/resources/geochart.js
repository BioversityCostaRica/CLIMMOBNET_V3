
$('.maps').each(function() {

    //google.charts.load('upcoming', {'packages':['geochart', "corechart"]});
    //google.charts.setOnLoadCallback(drawRegionsMap);
drawRegionsMap();
    function drawRegionsMap() {
        var val = $('.maps').attr('data-count');

        var coord=val.split(';')

        map = new google.maps.Map(document.getElementById('regions_div'), {
            center: {lat: parseFloat(coord[0]), lng: parseFloat(coord[1])},
            zoom: 8,
            mapTypeId: 'satellite',
            panControl:false,
            zoomControl:true,
            mapTypeControl:false,
            scaleControl:false,
            streetViewControl:false,
            overviewMapControl:false,
            rotateControl:false
        });

        var marker = new google.maps.Marker({
            position: {lat: parseFloat(coord[0]), lng: parseFloat(coord[1])},
            map: map,
            title: 'Hello World!',
            icon:'static/img/icon.png'


          });

        var contentString = '<div>'+
                              '<table>'+
                              '  <td>'+
                               '   <tr>'+
                                '    <th>'+
                                 '     <strong>Name : </strong>Allan Coto'+
                                  '  </th>'+
                                  '</tr>'+
                                  '<tr>'+
                                   ' <th>'+
                                    '  <strong>Country : </strong>Costa Rica'+
                                    '</th>'+
                                  '</tr>'+
                                  '<tr>'+
                                  '  <th>'+
                                   '   <strong>Items : </strong>65'+
                                   ' </th>'+
                                  '</tr>'+
                                '</td>'+
                              '</table>'+
                            '</div>';


        var infowindow = new google.maps.InfoWindow({content: contentString});

        marker.addListener('click', function() {infowindow.open(map, marker);});

        google.maps.event.addListener(map, "click", function(event) {infowindow.close();});



    }

});



