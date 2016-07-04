/**
 * Created by brandon on 01/07/16.
 */


jQuery(document).ready(function() {
    $("#sortable_technologies_included").sortable({
        connectWith: ['#varas'],
        update: function () {
            $('#txt_technologies_included').val($('#sortable_technologies_included').sortable('toArray'));

        }
    });

     $("#varas").sortable({
        connectWith: ['#sortable_technologies_included'],
    });
})

$(function() {
          $('#default').stepy({
              backLabel: 'Previous',
              block: true,
              nextLabel: 'Next',
              titleClick: true,
              titleTarget: 'undefined'
          });
      });

function AddGroup()
{
    if($('#txt_new_group').val()!='')
    {
        $('#group_list li').each(function (i)
        {
            var id=$(this).attr('id');
            $('#'+id).removeClass("active")

            id = id.replace('menu_','')
            $('#'+id).css('display','none')
        });

        var id = $('#txt_new_group').val().replace(/ /g, "_")
        $('#group_list').append('<li id="menu_' + id + '" onclick="click_in_group(\'menu_' + id + '\')"><a ><i class="fa  fa-tags"></i> <span>'+$('#txt_new_group').val()+'</span><i class="fa fa-times pull-right"></i></a></li>')
        $("#menu_"+id).addClass("active")


        $('#groups_content').append('<div id="' + id + '" class="sortable_class"><div id="sortable_technologies_included" style="padding: 5px"><div class="panel panel-danger"><div class="panel-heading"> <h4 class="panel-title"> <a href="#accordion1_1" data-parent="#accordion1" data-toggle="collapse" class="accordion-toggle"> Punto GPS de la finca </a> </h4></div> <div class="panel-collapse collapse  in" id="accordion1_1"> <div class="panel-body">Esta pregunta es super importante para poder mapear las distintas fincas </div> </div> </div> </div></div>')
        $('#txt_new_group').val('')

        $("#"+id).sortable({
        connectWith: ['#sortable_technologies_included'],
        });

        $("#sortable_technologies_included").sortable( "option", "connectWith", "#"+id );




    }
}

function click_in_group(id)
{
    $('#group_list li').each(function (i)
    {
        var id=$(this).attr('id');
        $('#'+id).removeClass("active")

        id = id.replace('menu_','')
        $('#'+id).css('display','none')
    });

    $("#"+id).addClass("active")

    id = id.replace('menu_','')
    $('#'+id).css('display','block')

}