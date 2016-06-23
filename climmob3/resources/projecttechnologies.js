/**
 * Created by brandon on 07/03/16.
 */


jQuery(document).ready(function() {
    $("#sortable_technologies_included").sortable({
        connectWith: ['#sortable_technologies_excluded'],
        update: function () {
            $('#txt_technologies_included').val($('#sortable_technologies_included').sortable('toArray'));
            $('#txt_technologies_excluded').val($('#sortable_technologies_excluded').sortable('toArray'));

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