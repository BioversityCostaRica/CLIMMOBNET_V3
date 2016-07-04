/**
 * Created by brandon on 27/06/16.
 */

function showAddQuestions()
{
    $("#txt_notes").val('')
    $("#txt_description").val('')
    $('#txt_indication').val('')
    $('#cmbtype').val('')
    $("[name='ckb_acceptother']").bootstrapSwitch('state',false);
    $("[name='ckb_registrationrequired']").bootstrapSwitch('state',false);
    $("[name='ckb_assessmentrequired']").bootstrapSwitch('state',false);
    $('#AddQuestions').modal('show')
}


function showModifyQuestion(id,notes,descripcion,indication, type, other,registration,assessment)
{
    $("#modify_txt_id").val(id);
    $("#modify_txt_notes").val(notes)
    $("#modify_txt_description").val(descripcion)
    $('#modify_txt_indication').val(indication)
    $('#modify_cmbtype').val(type)

    if(type==5 || type==6)
    {
        $("#modify_div_others").css('display','block');
    }

    if (other ==1)
        $("[name='modify_ckb_acceptother']").bootstrapSwitch('state', true);
    else
        $("[name='modify_ckb_acceptother']").bootstrapSwitch('state',false);

    if(registration == 1)
        $("[name='modify_ckb_registrationrequired']").bootstrapSwitch('state',true);
    else
        $("[name='modify_ckb_registrationrequired']").bootstrapSwitch('state',false);

    if (assessment == 1)
        $("[name='modify_ckb_assessmentrequired']").bootstrapSwitch('state',true);
    else
        $("[name='modify_ckb_assessmentrequired']").bootstrapSwitch('state',false);

    $('#ModifyQuestions').modal('show')
}

$('#cmbtype').change(function()
{

    if($('#cmbtype').val() == 5 || $('#cmbtype').val() ==6)
    {
        $('#div_others').css('display','block')
    }
    else
    {
        $('#div_others').css('display','none')
    }
})

$('#cmbtypeE').change(function()
{

    if($('#cmbtypeE').val() == 5 || $('#cmbtypeE').val() ==6)
    {
        $('#div_othersE').css('display','block')
    }
    else
    {
        $('#div_othersE').css('display','none')
    }
})

/////////////////////////////////////////////////////////
$('#modify_cmbtype').change(function()
{

    if($('#modify_cmbtype').val() == 5 || $('#modify_cmbtype').val() ==6)
    {
        $('#modify_div_others').css('display','block')
    }
    else
    {
        $('#modify_div_others').css('display','none')
    }
})

$('#modify_cmbtypeE').change(function()
{

    if($('#modify_cmbtypeE').val() == 5 || $('#modify_cmbtypeE').val() ==6)
    {
        $('#modify_div_othersE').css('display','block')
    }
    else
    {
        $('#modify_div_othersE').css('display','none')
    }
})