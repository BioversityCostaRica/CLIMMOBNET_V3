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

function showModifyEnumerator(user_name, name, status)
{

    $('#txt_modify_user_name').val('')
    $('#txt_modify_name').val('')
    $('#txt_modify_password').val('')
    $('#txt_modify_password_new').val('')

    $('#txt_modify_user_name').val(user_name)
    $('#txt_modify_name').val(name)

    //alert(status)
    if(status==0)
    {
        $("[name='ckb_modify_status']").bootstrapSwitch('state',false);
        $('#ckb_modify_status').removeAttr('checked');
    }
    else
    {
        $("[name='ckb_modify_status']").bootstrapSwitch('state',true);
        $('#ckb_modify_status').attr('checked', 'checked');
    }

    $('#ModifyEnumerator').modal('show')

}

function showDeleteEnumerator(user_name)
{
    $('#txt_delete_user_name').val(user_name)

    $('#DeleteEnumerator').modal('show')
}