/**
 * Created by brandon on 07/03/16.
 */


jQuery(document).ready(function() {
    $("#sortable_titulares").sortable({
        connectWith: ['#sortable_banca'],
        update: function () {
                $('#results_of_personal_information').html($('#sortable_titulares').sortable('toArray')+"<br/>");

        }
    });
    $("#sortable_banca").sortable({
        connectWith: ['#sortable_titulares'],
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