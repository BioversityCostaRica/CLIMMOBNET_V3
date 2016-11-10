/**
 * Created by brandon on 27/06/16.
 */

$(document).ready(function()
{
	$('#SearchInTable').keyup(function()
	{
		searchTable($(this).val());
	});
});

jQuery('.tm-inputadd').tagsManager
(
    {
        output:'#txt_select',
        tagsContainer:'#space_option',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-add'
    }
);

jQuery('.tm-inputaddE').tagsManager
(
    {
        output:'#txt_selectE',
        tagsContainer:'#space_optionE',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-add'
    }
);

jQuery('.modify_tm-input').tagsManager
(
    {
        output:'#modify_txt_select',
        tagsContainer:'#modify_space_option',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-edit'
    }
);

jQuery('.modify_tm-inputE').tagsManager
(
    {
        output:'#modify_txt_selectE',
        tagsContainer:'#modify_space_optionE',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-edit'
    }
);

function showAddQuestions()
{
    $("#txt_notes").val('')
    $("#txt_description").val('')
    $('#txt_indication').val('')
    $('#cmbtype').val('')
    $('#div_select').css('display','none')
    $('#div_characteristic').css('display','none')
    $('#div_others').css('display','none')
    $("[name='ckb_acceptother']").bootstrapSwitch('state',false);
    $("[name='ckb_registrationrequired']").bootstrapSwitch('state',false);
    $("[name='ckb_assessmentrequired']").bootstrapSwitch('state',false);
    $("[name='ckb_required_value']").bootstrapSwitch('state',false);
    $('#AddQuestions').modal('show')
}


function showModifyQuestion(id,notes,descripcion,indication, type, other,registration,assessment,options,question_posstm,question_negstm,question_twoitems,question_requiredvalue)
{
    $("#modify_txt_id").val(id);
    $("#modify_txt_notes").val(notes)
    $("#modify_txt_description").val(descripcion)
    $('#modify_txt_indication').val(indication)
    $('#modify_cmbtype').val(type)
    $('#modify_txt_twoitems').val(question_twoitems)
    $('#modify_txt_triadric_best').val(question_posstm)
    $('#modify_txt_triadric_worse').val(question_negstm)

    if (type==9)
    {
        $('#modify_div_submissions').css('display','none')
        $('#modify_div_characteristic').css('display','block')
    }
    else
    {
        $('#modify_div_submissions').css('display','block')
        $('#modify_div_characteristic').css('display','none')
    }

    if(type==5 || type==6)
    {
        jQuery('.modify_tm-input').tagsManager('empty');

        var different_options = options.split('~')

        for (var i=0; i<= different_options.length-1; i++)
        {
            jQuery('.modify_tm-input').tagsManager('pushTag', different_options[i])
        }
        $('#modify_div_select').css('display', 'block')
        $("#modify_div_others").css('display','block');
        $('#div_submissions').css('display','block')
    }
    else
    {
        jQuery('.modify_tm-input').tagsManager('empty');
        $('#modify_div_select').css('display', 'none')
        $("#modify_div_others").css('display','none');
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

    if (question_requiredvalue == 1)
        $("[name='modify_ckb_required_value']").bootstrapSwitch('state',true);
    else
        $("[name='modify_ckb_required_value']").bootstrapSwitch('state',false);

    $('#ModifyQuestions').modal('show')
}

function showDeleteQuestion(questionid)
{
    $('#delete_question_id').val(questionid)
    $('#deleteQuestion').modal('show')
}
//////////////////////////////////////////////////////////////
$('#cmbtype').change(function()
{

    if($('#cmbtype').val() == 5  || $('#cmbtype').val() ==6)
    {
        jQuery('.tm-inputadd').tagsManager('empty');
        $('#div_select').css('display', 'block')
        $('#div_others').css('display', 'block')
    }
    else
    {
        $('#div_select').css('display', 'none')
        $('#div_others').css('display', 'none')
    }

    if($('#cmbtype').val() == 9) {
        $('#div_submissions').css('display','none')
        $('#div_characteristic').css('display', 'block')
    }
    else {
        $('#div_submissions').css('display','block')
        $('#div_characteristic').css('display', 'none')
    }
})

$('#cmbtypeE').change(function() {

    if ($('#cmbtypeE').val() == 5 || $('#cmbtypeE').val() == 6)
    {
        jQuery('.tm-inputaddE').tagsManager('empty');
        $('#div_selectE').css('display', 'block')
        $('#div_othersE').css('display', 'block')
    }
    else
    {
        jQuery('.tm-inputaddE').tagsManager('empty');
        $('#div_selectE').css('display', 'none')
        $('#div_othersE').css('display', 'none')
    }

    if($('#cmbtypeE').val() == 9)
    {
        $('#div_submissionsE').css('display','none')
        $('#div_characteristicE').css('display','block')
    }
    else
    {
        $('#div_submissionsE').css('display','block')
        $('#div_characteristicE').css('display','none')
    }
})

$('input[name="ckb_registrationrequired"]').on('switchChange.bootstrapSwitch', function(event, state) {
        if($(this).is(':checked')) {
            $("[name='ckb_assessmentrequired']").bootstrapSwitch('state', false);
            $("[name='ckb_required_value']").bootstrapSwitch('state', true);
        }
});

$('input[name="ckb_assessmentrequired"]').on('switchChange.bootstrapSwitch', function(event, state) {
        if($(this).is(':checked')) {
            $("[name='ckb_registrationrequired']").bootstrapSwitch('state', false);
            $("[name='ckb_required_value']").bootstrapSwitch('state', true);
        }
});
/////////////////////////////////////////////////////////
$('#modify_cmbtype').change(function()
{

    if($('#modify_cmbtype').val() == 5 || $('#modify_cmbtype').val() ==6)
    {
        jQuery('.modify_tm-input').tagsManager('empty');
        $('#modify_div_select').css('display', 'block')
        $('#modify_div_others').css('display', 'block')
    }
    else
    {
        $('#modify_div_select').css('display', 'none')
        $('#modify_div_others').css('display', 'none')
    }

    if($('#modify_cmbtype').val() == 9) {
        $('#modify_div_submissions').css('display','none')
        $('#modify_div_characteristic').css('display', 'block')
    }
    else {
        $('#modify_div_submissions').css('display','block')
        $('#modify_div_characteristic').css('display', 'none')
    }


})

$('#modify_cmbtypeE').change(function()
{

    if($('#modify_cmbtypeE').val() == 5 || $('#modify_cmbtypeE').val() ==6)
    {
        jQuery('.modify_tm-inputE').tagsManager('empty');
        $('#modify_div_selectE').css('display', 'block')
        $('#modify_div_othersE').css('display', 'block')
    }else
    {
        jQuery('.modify_tm-inputE').tagsManager('empty');
        $('#modify_div_selectE').css('display', 'none')
        $('#modify_div_othersE').css('display', 'none')
    }
    
    if($('#modify_cmbtypeE').val() == 9) {
        $('#modify_div_submissionsE').css('display', 'none')
        $('#modify_div_characteristicE').css('display', 'block')
    }
    else {
        $('#modify_div_submissionsE').css('display', 'block')
        $('#modify_div_characteristicE').css('display', 'none')
    }

})

$('input[name="modify_ckb_registrationrequired"]').on('switchChange.bootstrapSwitch', function(event, state) {
        if($(this).is(':checked')) {
            $("[name='modify_ckb_assessmentrequired']").bootstrapSwitch('state', false);
            $("[name='modify_ckb_required_value']").bootstrapSwitch('state',true);
        }
});

$('input[name="modify_ckb_assessmentrequired"]').on('switchChange.bootstrapSwitch', function(event, state) {
        if($(this).is(':checked')) {
            $("[name='modify_ckb_registrationrequired']").bootstrapSwitch('state', false);
            $("[name='modify_ckb_required_value']").bootstrapSwitch('state',true);
        }
});


function searchTable(searching)
{
    var table = $('#tabletechnologies');
	table.find('td').each(function(index, row)
	{
		var allCells = $(row).find('td');

		if(allCells.length > 0)
		{
			var found = false;
			allCells.each(function(index, td)
			{
				var regExp = new RegExp(searching, 'i');

				if(regExp.test($(td).text()))
				{
					found = true;
					return false;
				}
			});
			if(found == true)$(row).show();else $(row).hide();
		}
	});
}