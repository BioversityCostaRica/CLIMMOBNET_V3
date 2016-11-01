/**
 * Created by brandon on 07/03/16.
 */


jQuery(document).ready(function() {
    $("#sortable_technologies_included").sortable({
        connectWith: ['#sortable_technologies_excluded'],
        update: function () {
            $('#txt_technologies_included').val($('#sortable_technologies_included').sortable('toArray'));
            $('#txt_technologies_excluded').val($('#sortable_technologies_excluded').sortable('toArray'));

            var amount_of_including = $('#txt_technologies_included').val().split(",")
            if(amount_of_including.length==4)
            {
                $('#ErrorSortable').css('display','block');
                $("#sortable_technologies_excluded").sortable("cancel");
                $('#txt_technologies_included').val($('#sortable_technologies_included').sortable('toArray'));
                $('#txt_technologies_excluded').val($('#sortable_technologies_excluded').sortable('toArray'));
            }
            else
            {
                $('#ErrorSortable').css('display','none');
            }

            $('#btn_back').attr('disabled', true);


        }
    });
    $("#sortable_technologies_excluded").sortable({
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