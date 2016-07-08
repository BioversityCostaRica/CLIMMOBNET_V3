/**
 * Created by brandon on 01/07/16.
 */


jQuery(document).ready(function() {

    $("#sortable_panel").sortable({
        update: function ()
        {
            $('#btnsaveordergroup').css('display','block')
            $('#addnewgroup').css('display','none');
            $('.btnaddquestion').prop('disabled',true)
            $('#txt_groups').val($('#sortable_panel').sortable('toArray'));
        }
    });

    $('#txt_groups').val($('#sortable_panel').sortable('toArray'));

    var part = $('#txt_groups').val().split(",")
    var total = part.length

    for (var par=0; par<total;par++)
    {
        var element = part[par];
        var id = element.split("_")
        id =id[1]
        $("#groupsortable_"+id).sortable({
            update: function ()
            {
                id = $(this).attr("id").split("_")
                $('#txt_question_'+id[1]).val($("#groupsortable_"+id[1]).sortable('toArray'));
            }
        });
    }
    /*$('.colorpicker-default').colorpicker({
        format: 'hex'
    });*/

    /*$(function() {
        $('.colorpicker-default').colorpicker().on('changeColor', function(e)
        {
            $('#btnsaveordergroup').css('display','block')
            $('#addnewgroup').css('display','none');
            $('.btnaddquestion').prop('disabled',true)
            $('#txt_groups').val($('#sortable_panel').sortable('toArray'));
            var id=$(this).attr("id")
            partes = id.split("_")
            $('#group_'+partes[1]+' .panel-heading').css('background-color',e.color.toHex());
        });
    });*/


})




function AddGroup()
{
    $('#txt_group_name').val('')
    $('#txt_group_desc').val('')
    $('#AddGroup').modal('show');

}
/*
var number=0
function createGroup()
{
    var color=''
    if(number==0)
        color='warning'
    else
        if(number==1)
            color='danger'
        else
            if(number==2)
                color='info'
            else
                if(number==3)
                    color='primary'

    var id = $('#txt_group_name').val().replace(/ /g, "_")
    $('#sortable_panel').append('<div class="panel panel-'+color+'" id="group_'+id+'"><div class="panel-heading"><h4 class="panel-title"><a href="#accordion_group_'+id+'"  data-toggle="collapse" class="accordion-toggle">'+$('#txt_group_name').val()+'</a> </h4> </div><div class="panel-collapse collapse" id="accordion_group_'+id+'"> <div class="panel-body"></div></div> </div>')
    $('#AddGroup').modal('hide')
    number++
    if(number>3)
        number=0
}*/

function AddQuestion(group_id,section_user,section_project,section_id)
{

    $('#txt_section_user').val(section_user)
    $('#txt_section_project').val(section_project)
    $('#txt_section_id').val(section_id)
    $('#group_name').html('<h3>'+group_id+'</h3>');
    $('#AddQuestion').modal('show')
}

function AddQuestionToGroup(many_questions)
{
    for (var iden=0; iden<=many_questions; iden++)
    {
        if($('#checkbox_questions_'+iden).is(':checked'))
        {
            alert($('#checkbox_questions_'+iden).val());
        }
    }
}

function addQuestionToText(id)
{
    if($(id).is(':checked'))
    {

        $("#txt_id_questions").val($("#txt_id_questions").val()+$(id).val()+",")
    }
    else
    {
        var values= $("#txt_id_questions").val();

        $("#txt_id_questions").val(values.replace($(id).val()+",",""))
    }
}
/*

$(function() {
          $('#default').stepy({
              backLabel: 'Previous',
              block: true,
              nextLabel: 'Next',
              titleClick: true,
              titleTarget: 'undefined'
          });
      });

*/