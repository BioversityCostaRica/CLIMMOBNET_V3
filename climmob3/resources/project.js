/**
 * Created by cquiros on 29/02/16.
 */
jQuery(document).ready(function() {

    ClimMobMaps.init();

    $('#hidden-table-info_length').css('display', 'none');
    $('#hidden-table-info_filter').css('display', 'none');

    $('#SearchInTable').keyup(function()
	{
		searchTable($(this).val());
	});

    /*var Sliders = function ()
    {

        // range min
        $("#slider-range-min").slider({
            range: "min",
            value: 3,
            min: 2,
            max: 6,
            slide: function (event, ui) {
                $("#slider-range-min-amount").text("$" + ui.value);
            }
        });

    }();*/

})

jQuery('.tm-inputadd').tagsManager
(
    {
        output:'#newproject_tag',
        tagsContainer:'#space_tags',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-add'
    }
);

jQuery('.tm-inputadd2').tagsManager
(
    {
        output:'#newproject_tagE',
        tagsContainer:'#space_tagsE',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-add'
    }
);

jQuery('.tm-inputupt').tagsManager
(
    {
        output:'#updproject_tag',
        tagsContainer: '#space_tagsM',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-edit'
    }
);

jQuery('.tm-inputupt2').tagsManager
(
    {
        output:'#updproject_tagE',
        tagsContainer: '#space_tagsME',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-edit'
    }
);

function showAddProject()
{
    $('#newproject_code').val('')
    $('#newproject_name').val('')
    $('#newproject_description').val('')
    $('#tags').val('')
    jQuery('.tm-inputadd').tagsManager('empty');
    $('#newproject_principal_investigator').val('')
    $('#newproject_mail_address').val('')


    $('#addNewProject').modal('show');

};


function showModifyProject(code,name,description,tags,principal_investigator,mail_address,number_obs, number_com, latitude,longitude)
{
    $('#updproject_code').val(code);
    $('#updproject_name').val(name);
    $('#updproject_description').val(description);

    var different_tags = tags.split('~');
    var number_of_options = different_tags.length-1;
    $('#tags1').val('')
    jQuery('.tm-inputupt').tagsManager('empty');

    for (var i=0; i<= number_of_options; i++)
    {
        jQuery('.tm-inputupt').tagsManager('pushTag',different_tags[i])
    }

    $('#updproject_principal_investigator').val(principal_investigator);
    $('#updproject_mail_address').val(mail_address);
    $('#updproject_numobs').val(number_obs);
    $('#updproject_numcom').val(number_com);
    $('#updproject_lat').val(latitude);
    $('#updproject_lon').val(longitude);
    ClimMobMaps3.init();

    $('#modifyProject').modal('show');
}

function showDeleteProject(code)
{
    document.getElementById('delproject_code').value=code;
    $('#deleteProject').modal('show');
}

function searchTable(searching)
{
    var table = $('#hidden-table-info');
	table.find('tr').each(function(index, row)
	{
		var allCells = $(row).find('td');

		if(allCells.length > 0)
		{
			var found = false;
			allCells.each(function(index, td)
			{
				var regExp = new RegExp(searching, 'i');

				if(regExp.test($(td).text()))
				{
					found = true;
					return false;
				}
			});
			if(found == true)$(row).show();else $(row).hide();
		}
	});
}

var ClimMobMaps = function () {

    return {
        //main function to initiate map samples
        init: function ()
        {

            punto = new google.maps.LatLng(9.904713513651277, -83.68527918704831);

            var myOptions =
            {
                zoom: 1, center: punto, mapTypeId: google.maps.MapTypeId.ROADMAP
            };

            var map = new google.maps.Map(document.getElementById("gmap_marker"),  myOptions);

            var marker = new google.maps.Marker(
            {
                position:punto,
                draggable: true,
                map: map
            });

            google.maps.event.addListener(marker, 'drag', function()
            {
                $("#newproject_lat").val(marker.getPosition().lat());
                $("#newproject_lon").val(marker.getPosition().lng());
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

var ClimMobMaps3 = function () {



    return {
        //main function to initiate map samples
        init: function ()
        {

            lat= $("#updproject_lat").val();
            lon= $("#updproject_lon").val();

            punto = new google.maps.LatLng(lat,lon);

            var myOptions =
            {
                zoom: 1, center: punto, mapTypeId: google.maps.MapTypeId.ROADMAP
            };

            var map = new google.maps.Map(document.getElementById("gmap_marker3"),  myOptions);

            var marker = new google.maps.Marker(
            {
                position:punto,
                draggable: true,
                map: map
            });

            google.maps.event.addListener(marker, 'drag', function()
            {
                $("#updproject_lat").val(marker.getPosition().lat());
                $("#updproject_lon").val(marker.getPosition().lng());
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

function justNumbers(e)
{
	var keynum = window.event ? window.event.keyCode : e.which;
	if ((keynum == 8) || (keynum == 46))
		return true;

		return /\d/.test(String.fromCharCode(keynum));

}