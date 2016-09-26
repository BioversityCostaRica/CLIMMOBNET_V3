/**
 * Created by brandon on 04/03/16.
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
    var table = $('#tabletechnologies');
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

function  showAddTecnology()
{
    $('#txt_add_pro').val('')

    $('#AddTechnology').modal('show')
}

function showModifyTechnology(technology_name, id)
{
    $('#txt_update_id').val(id)
    $('#txt_update_name').val(technology_name)

    $('#modifyTechnology').modal('show');
}

function showDeleteTechnology(id)
{
    $('#txt_delete_id').val(id)

    $('#deleteTechnology').modal('show');
};

