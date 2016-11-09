/**
 * Created by brandon on 29/06/16.
 */

$( document ).ready(function()
{
    $("[name='modify_ckb_acceptother']").bootstrapSwitch();
    $("[name='modify_ckb_registrationrequired']").bootstrapSwitch();
    $("[name='modify_ckb_assessmentrequired']").bootstrapSwitch();
    $("[name='modify_ckb_required_value']").bootstrapSwitch();
    $('#ModifyQuestionsE').modal('show');
});