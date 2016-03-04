/**
 * Created by brandon on 04/03/16.
 */


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