/**
 * Created by lluis on 04/11/16.
 */
$(document).ready(function()
{
	$('#inputSearch').keyup(function()
	{
		searchTable($(this).val());
	});
    $('#searchBP').click(function()
	{
		searchTable($('#inputSearch').val());
	});
    $('#loading-btn').click(function () {

        $.ajax({
    url: "",
    context: document.body,
    success: function(s,x){
        $(this).html(s);
    }
});



    })
});


function searchTable(searching)
{
    var table = $('#searchP');
	table.find('tr').each(function(index, row)
	{
		var allCells = $(row).find('a');

		if(allCells.length > 0)
		{
			var found = false;
			allCells.each(function(index, td)
			{
                if($(td).attr("id")) {
                    var regExp = new RegExp(searching, 'i');

                    if (regExp.test($(td).text())) {
                        found = true;
                        return false;
                    }
                }
			});
			if(found == true)$(row).show();else $(row).hide();
		}
	});
}