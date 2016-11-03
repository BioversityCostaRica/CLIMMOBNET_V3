/**
 * Created by brandon on 05/05/16.
 */

$( document ).ready(function()
{
    ClimMobMaps2.init();
    $('#addNewProjectE').modal('show');

});

var ClimMobMaps2 = function () {
    var lat=9.904713513651277;
    var lon=-83.68527918704831;
    if ($("#newproject_latE").val() != '')
    {
        lat= $("#newproject_latE").val();
        lon= $("#newproject_lonE").val();
    }
    return {
        //main function to initiate map samples
        init: function ()
        {

            punto = new google.maps.LatLng(lat, lon);

            var myOptions =
            {
                zoom: 1, center: punto, mapTypeId: google.maps.MapTypeId.ROADMAP
            };

            var map = new google.maps.Map(document.getElementById("gmap_markerE"),  myOptions);

            var marker = new google.maps.Marker(
            {
                position:punto,
                draggable: true,
                map: map
            });

            google.maps.event.addListener(marker, 'drag', function()
            {
                $("#newproject_latE").val(marker.getPosition().lat());
                $("#newproject_lonE").val(marker.getPosition().lng());
            });

            $('.nav-tabs a').on('shown.bs.tab',
                function ()
                {
                  google.maps.event.trigger(map, 'resize');
                  map.setCenter(new google.maps.LatLng(0, 0));
                }
            );
        }

    };

}();