/**
 * Created by brandon on 26/05/16.
 */


jQuery(document).ready(function() {
    $("#sortable_technologiesalias_included").sortable({
        connectWith: ['#sortable_technologiesalias_excluded'],
        update: function () {
            $('#txt_technologiesalias_included').val($('#sortable_technologiesalias_included').sortable('toArray'));

            $('#txt_technologiesalias_excluded').val($('#sortable_technologiesalias_excluded').sortable('toArray'));

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