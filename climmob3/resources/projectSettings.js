/**
 * Created by brandon on 07/03/17.
 */

$( document ).ready(function()
{

    $("#menu_settings li").click(function () {
        clear();

        nombre = $(this).attr("name")
        $('#'+nombre).css('display','block');
        $('li[name="'+nombre+'"]').addClass("active");

        var d = new Date();
        d.setTime(d.getTime() + (365*24*60*60*1000));
        var expires = "expires="+ d.toUTCString();
        document.cookie = "_MENUSETTINGS_ ="+nombre+";" + expires;

    });

    $('.section_accordion').on('show.bs.collapse', function (e)
    {
        part = e.target.id;
        //alert(part);
        var d = new Date();
        d.setTime(d.getTime() + (365*24*60*60*1000));
        var expires = "expires="+ d.toUTCString();
        document.cookie = "_SETTINGS_ ="+part+";" + expires;

    });

    $('.section_accordion').on('hide.bs.collapse', function (e)
    {
        part = e.target.id;
        var ca = document.cookie.split(';');
        for(var i = 0; i < ca.length; i++) {
            var distintosCookies = ca[i];

            var cookie = distintosCookies.split('=');

               if(cookie[0]==" _SETTINGS_")
               {
                   if(part ==cookie[1])
                   {
                       var d = new Date();
                        d.setTime(d.getTime() + (365*24*60*60*1000));
                        var expires = "expires="+ d.toUTCString();
                        document.cookie = "_SETTINGS_ =;" + expires;
                   }
               }



        }

    });

    function clear()
    {
        $('#snp_countries').css('display','none');
        $('#snp_tecnologies').css('display','none');
        $('#snp_languajes').css('display','none');
        $('#snp_enumerators').css('display','none');
        $('#snp_registration').css('display','none');

        $('li[name="snp_countries"]').removeClass("active");
        $('li[name="snp_tecnologies"]').removeClass("active");
        $('li[name="snp_languajes"]').removeClass("active");
        $('li[name="snp_enumerators"]').removeClass("active");
        $('li[name="snp_registration"]').removeClass("active");

    }
})

