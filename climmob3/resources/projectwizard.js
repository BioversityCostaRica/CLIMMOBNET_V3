/**
 * Created by brandon on 26/10/16.
 */

$( document ).ready(function()
{
    $(function() {
          $('#default').stepy({
              backLabel: 'Previous',
              block: true,
              nextLabel: 'Next',
              titleClick: true,
              titleTarget: '.stepy-tab'
          });
      });
});