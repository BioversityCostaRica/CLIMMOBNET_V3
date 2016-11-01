/**
 * Created by brandon on 26/05/16.
 */

$(document).ready(function()
{
	$('#SearchInTable').keyup(function()
	{
		searchTable($(this).val());
	});
});

function searchTable(searching)
{
    var table = $('#sortable_technologiesalias_excluded');
	table.find('li').each(function(index, row)
	{
		var allCells = $(row).find('b');

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

jQuery(document).ready(function() {
    $("#sortable_technologiesalias_included").sortable({
        connectWith: ['#sortable_technologiesalias_excluded'],
        update: function () {
            $('#txt_technologiesalias_included').val($('#sortable_technologiesalias_included').sortable('toArray'));
            $('#txt_technologiesalias_excluded').val($('#sortable_technologiesalias_excluded').sortable('toArray'));

			$('#btn_back').attr('disabled', true);
			$('#addnewaliastechnology').prop('disabled',true)

        }
    });
    $("#sortable_technologiesalias_excluded").sortable({
        connectWith: ['#sortable_technologiesalias_included'],
    });
})

function showAddAlias()
{
    $('#AddTechnologyAliasExtra').modal('show')
}