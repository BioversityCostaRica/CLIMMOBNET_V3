/**
 * Created by brandon on 17/11/16.
 */

$(document).ready(function ()
{

});

function changeProject(id,cookie)
{
    var d = new Date();
    d.setTime(d.getTime() + (365*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = "_PROJECT_ ="+cookie+";" + expires;
    $("#"+id).click()
}



var originalLeave = $.fn.popover.Constructor.prototype.leave;
$.fn.popover.Constructor.prototype.leave = function(obj){
  var self = obj instanceof this.constructor ?
    obj : $(obj.currentTarget)[this.type](this.getDelegateOptions()).data('bs.' + this.type)
  var container, timeout;

  originalLeave.call(this, obj);

  if(obj.currentTarget) {
    container = $(obj.currentTarget).siblings('.popover')
    timeout = self.timeout;
    container.one('mouseenter', function(){
      //We entered the actual popover – call off the dogs
      clearTimeout(timeout);
      //Let's monitor popover content instead
      container.one('mouseleave', function(){
        $.fn.popover.Constructor.prototype.leave.call(self, self);
      });
    })
  }
};


$('.popovers').popover(
    {
        html:true,
        trigger: 'click hover',
        placement: 'auto',
        delay: {show: 50, hide: 100}
    });


/*var Script = function () {

    //morris chart

    $(function () {
      // data stolen from http://howmanyleft.co.uk/vehicle/jaguar_'e'_type


      Morris.Donut({
        element: "hero-donut",
        data: [
          {label: "Jam", value: 25 },
          {label: "Frosted", value: 40 },
          {label: "Custard", value: 25 },
          {label: "Sugar", value: 10 }
        ],
          colors: ["#41cac0", "#49e2d7", "#34a39b"],
        formatter: function (y) { return y + "%" }
      });

    });

}();*/