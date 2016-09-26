/**
 * Created by brandon on 04/05/16.
 */

$(document).ready(function()
{
	$('#SearchInTable').keyup(function()
	{
		searchTable($(this).val());
	});
});

function  showAddTecnologyAlias()
{
    $('#txt_add_alias').val('')

    $('#AddTechnologyAlias').modal('show')
}

function showModifyTechnologyalias  (technology_name, id)
{
    $('#txt_update_id').val(id)
    $('#txt_update_name').val(technology_name)

    $('#modifyTechnologyalias').modal('show');
}

function showDeleteTechnologyalias(id)
{
    $('#txt_delete_id').val(id)

    $('#deleteTechnologyalias').modal('show');
};

function searchTable(searching)
{
    var table = $('#tabletechnologiesalias');
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