/**
 * Created by brandon on 09/05/16.
 */


$('.tablecountry').click(function()
{
    var id_selected = $(this).attr('id')

    $('#flag').html('<img class="logo img-responsive" alt="country" src="http://0.0.0.0:6548/static/country-flags/'+id_selected+'.png ">')
    $('#txt_cnty_cod').val(id_selected)
    $('#AddCountry').modal('show')

});

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