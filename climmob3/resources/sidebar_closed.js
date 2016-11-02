/**
 * Created by lluis on 01/11/16.
 */

$( document ).ready(function()
{
   $('.fa-bars').last().trigger("click");

    $('.fa-bars').change(function() {
        $("container").removeClass("sidebar-closed")
    });

});