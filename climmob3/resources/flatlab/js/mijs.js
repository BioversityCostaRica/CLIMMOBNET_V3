

    /*jQuery(document).ready(function() {
          $("#sortable_titulares").sortable({
              update : function(event, ui) {
                 $('#resultado').html(ui.item.parent().sortable('toArray')+"<br/>");
              }});

        $("#sortable_banca").sortable({
              update : function(event, ui) {
                 $('#resultado').html(ui.item.parent().sortable('toArray')+"<br/>");
              }});
      });*/
jQuery(document).ready(function() {
    $("#sortable_titulares").sortable({
        connectWith: ['#sortable_banca'],
        update: function () {
                $('#resultado').html($('#sortable_titulares').sortable('toArray')+"<br/>");

        }
    });
    $("#sortable_banca").sortable({
        connectWith: ['#sortable_titulares'],
    });

})

