/**
 * Created by brandon on 09/05/16.
 */


function addCountry()
{
    $('#txt_cn')
    $('#txt_cnty_cod').val("")
    $('#AddCountry').modal('show')

}

function showModifyContactCountry(cnty_cod, cnty_contact)
{
    $('#upd_cnty_cod').val(cnty_cod)
    $('#txt_upd_cnty_contact').val(cnty_contact)
    $('#ModifyContactCountry').modal('show')
}

function showDeleteCountry(cnty_cod)
{
    $('#delete_cnty_cod').val(cnty_cod)
    $('#DeleteCountry').modal('show')
}