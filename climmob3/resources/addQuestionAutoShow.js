/**
 * Created by brandon on 28/06/16.
 */

$(document).ready(function()
{
    $("[name='ckb_acceptother']").bootstrapSwitch();
    $("[name='ckb_registrationrequired']").bootstrapSwitch();
    $("[name='ckb_assessmentrequired']").bootstrapSwitch();
    $('#AddQuestionsE').modal("show");
})