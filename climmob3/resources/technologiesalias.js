/**
 * Created by brandon on 04/05/16.
 */


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