/**
 * Created by brandon on 01/07/16.
 */


jQuery(document).ready(function() {

    $('#SearchInTable').keyup(function()
	{
		searchTable($(this).val());
	});

    $("#sortable_panel").sortable({
        update: function () {
            $('#btncancelgroup').css('display','block');
            $('#btnsaveordergroup').css('display', 'block');
            $('#addnewgroup').prop('disabled', true);
            $('.btnaddquestion').prop('disabled', true);
            $('#txt_groups').val($('#sortable_panel').sortable('toArray'));
            //$('#accordion_group_1').removeClass("in");


            /*------------------prueba de bloqueo de grupos*/
            var part = $('#txt_groups').val().split(",");
            var total = part.length;

            for (var par = 0; par < total; par++) {
                var element = part[par];
                var id = element.split("_");
                id = id[1];
                $("#groupsortable_" + id).sortable('disable');
            }

        }
    });

    $('#txt_groups').val($('#sortable_panel').sortable('toArray'));

    var part = $('#txt_groups').val().split(",");
    var total = part.length;

    for (var par = 0; par < total; par++) {
        var element = part[par];
        var id = element.split("_");
        id = id[1];
        $("#groupsortable_" + id).sortable({
            update: function () {
                //$('#btnsaveordergroup').css('display','block');
                $('#addnewgroup').prop('disabled', true);
                $('.btnaddquestion').prop('disabled', true);
                $('#sortable_panel').sortable('disable');
                id = $(this).attr("id").split("_");
                $('#btnsaveorderquestions_' + id[1]).css('display', 'block');
                $('#btncancelquestions_' + id[1]).css('display', 'block');
                $('#txtquestion_' + id[1]).val($("#groupsortable_" + id[1]).sortable('toArray'));


                /*------------------prueba de bloqueo de grupos*/
                var part2 = $('#txt_groups').val().split(",");
                var total2 = part2.length;

                for (var par2 = 0; par2 < total2; par2++) {
                    var element2 = part2[par2];
                    var id2 = element2.split("_");
                    id2 = id2[1];
                    if (id[1] != id2) {
                        $("#groupsortable_" + id2).sortable('disable');
                    }
                }
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

$('#formview').click(function()
{
    $('#iframepreview').attr('src', $('#iframepreview').attr('src'));
    $('#FlatTree4').css('display','none')
    $('#iframepreview').css('display','block');
});

$('#treeview').click(function()
{
    $('#iframepreview').css('display','none');
    $('#FlatTree4').css('display','block')

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

$('.group').on('hide.bs.collapse', function (e)
{
    part = e.target.id.split('_');
    if(part[1]=="group")
    {
        var result = $('#txt_accordion_open').val().indexOf(e.target.id+",");
        if(result!=-1)
            $('#txt_accordion_open').val($('#txt_accordion_open').val().replace(e.target.id+",",""))
    }
});

$('.question').on('hide.bs.collapse', function (e)
{
    part = e.target.id.split('_');
    if(part[1]=="question")
    {
        var result = $('#txt_accordion_open').val().indexOf(e.target.id+",");
        if(result!=-1)
            $('#txt_accordion_open').val($('#txt_accordion_open').val().replace(e.target.id+",",""))
    }
});

$('.group').on('show.bs.collapse', function (e)
{
    part = e.target.id.split('_');
    if(part[1]=="group")
    {
        var result = $('#txt_accordion_open').val().indexOf(e.target.id+",");

        if(result==-1)
            $('#txt_accordion_open').val($('#txt_accordion_open').val()+e.target.id+",")
   }
});

$('.question').on('show.bs.collapse', function (e)
{
    part = e.target.id.split('_');
    if(part[1]=="question")
    {
        var result = $('#txt_accordion_open').val().indexOf(e.target.id+",");

        if(result==-1)
            $('#txt_accordion_open').val($('#txt_accordion_open').val()+e.target.id+",")
    }

});
function panel_collapse(id)
{
    var result = $('#txt_accordion_open').val().indexOf(id+",");

    if(result != -1)
    {
        $('#txt_accordion_open').val($('#txt_accordion_open').val().replace(id+",",""));
    }
    else
    {
        $('#txt_accordion_open').val($('#txt_accordion_open').val()+id+",");
    }
    //$('#txt_accordion_open').val($('#txt_accordion_open').val()+id+",")
}

function AddGroup()
{
    $('#txt_group_name').val('');
    $('#txt_group_desc').val('');
    $('#txt_accordion_openaddgroup').val($('#txt_accordion_open').val());
    $('#txt_groupsaddgroup').val($('#txt_groups').val());
    $('#AddGroup').modal('show');
}

function moveQuestion(groupname,groupid,questionid,questiondesc)
{
    $("#cmbgroups").find("option[value='"+groupid+"']").remove();
    $('#move_questiondesc').html("<b>"+questiondesc+"</b>");
    $('#move_groupid').val(groupid);
    $('#move_questionid').val(questionid);
    $('#move_groupname').html("<b>"+groupname+"</b>");
    $('#txt_accordion_openmovequestion').val($('#txt_accordion_open').val());
    $('#txt_groupsmovequestion').val($('#txt_groups').val());
    $('#MoveQuestion').modal('show');
}

function DeleteGroup(id)
{
    $('#dlt_group_en').css('display','block');
    $('#dlt_question_en').css('display','none');
    $('#dlt_group').css('display','block');
    $('#dlt_question').css('display','none');
    $('#delete_group_id').val(id);
    $('#delete_question_id').val("");
    $('#txt_accordion_opendelete').val($('#txt_accordion_open').val());
    $('#txt_groupsdelete').val($('#txt_groups').val());
    $('#deleteElement').modal('show');
}

function DeleteQuestion(idgroup,idquestion)
{
    $('#dlt_group_en').css('display','none');
    $('#dlt_question_en').css('display','block');
    $('#dlt_group').css('display','none');
    $('#dlt_question').css('display','block');
    $('#delete_group_id').val(idgroup);
    $('#delete_question_id').val(idquestion);
    $('#txt_accordion_opendelete').val($('#txt_accordion_open').val());
    $('#txt_groupsdelete').val($('#txt_groups').val());
    $('#deleteElement').modal('show');
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

    $('#txt_section_user').val(section_user);
    $('#txt_section_project').val(section_project);
    $('#txt_section_id').val(section_id);
    $('#group_name').html('<h3>'+group_id+'</h3>');
    $('#txt_accordion_openaddquestion').val($('#txt_accordion_open').val());
    $('#txt_groupsaddquestion').val($('#txt_groups').val());
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
        $("#txt_id_questions").val($("#txt_id_questions").val()+$(id).val()+",");
    }
    else
    {
        var values= $("#txt_id_questions").val();

        $("#txt_id_questions").val(values.replace($(id).val()+",",""));
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