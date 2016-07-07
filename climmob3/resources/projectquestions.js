/**
 * Created by brandon on 01/07/16.
 */


jQuery(document).ready(function() {
    $("#sortable_panel").sortable({
        update: function () {
            $('#btnsaveordergroup').css('display','block')
            $('#addnewgroup').css('display','none');
            $('.btnaddquestion').prop('disabled',true)
            $('#txt_groups').val($('#sortable_panel').sortable('toArray'));

        }
    });

    $("#group2").sortable({
        update: function () {
            $('#txt_group2').val($('#group2').sortable('toArray'));

        }
    });

    /*$('.colorpicker-default').colorpicker({
        format: 'hex'
    });*/

    $(function() {
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
    });


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

function AddQuestion(group_id)
{
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