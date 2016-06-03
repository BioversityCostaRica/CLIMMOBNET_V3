/**
 * Created by brandon on 31/05/16.
 */

function showAddEnumerator()
{
    $('#txt_add_enumerator_user_name').val('');
    $('#txt_add_enumerator_name').val('')
    $('#txt_add_enumerator_password').val('')
    $('#AddEnumerator').modal('show')
}

function showModifyEnumerator(user_name, name, password, status)
{

    $('#txt_modify_user_name').val('')
    $('#txt_modify_name').val('')
    $('#txt_modify_password').val('')
    $('#txt_modify_status').val('')

    $('#txt_modify_user_name').val(user_name)
    $('#txt_modify_name').val(name)
    $('#txt_modify_password').val(password)
    $('#txt_modify_status').val(status)

    $('#ModifyEnumerator').modal('show')

}

function showDeleteEnumerator(user_name)
{
    $('#txt_delete_user_name').val(user_name)

    $('#DeleteEnumerator').modal('show')
}