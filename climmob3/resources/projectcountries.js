/**
 * Created by brandon on 09/05/16.
 */


function addCountry(id,imagepath,countryname)
{
    var id_selected = id
    $('#countryname').html('<b>'+countryname+'</b>')
    $('#flag').html('<img class="logo img-responsive" alt="country" src="'+imagepath+'">')
    $('#txt_cnty_cod').val(id_selected)
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