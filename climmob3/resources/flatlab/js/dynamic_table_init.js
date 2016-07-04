var Vimg;
var title_tags;
var title_investigator;
var title_email;
var info_tags;
var info_investigator;
var info_email;
var title_icon_country;
var location_icon_country;
var title_icon_tech;
var location_icon_tech;
var title_icon_languaje;
var location_icon_languaje;
var title_icon_enumerator;
var location_icon_enumerator;
var title_icon_question;
var location_icon_question;
var countries_in_proyect;
var msg_countries;
var technologies_in_proyect;
var msg_technologies;
var enumerator_in_proyect;
var msg_enumerator;

function fnFormatDetails ( oTable, nTr )
{
    var aData = oTable.fnGetData( nTr );
    var sOut = '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">';
    sOut    += '<tr>' +
        '           <td >'+title_investigator+':</td>' +
        '           <td >'+info_investigator+'</td>' +
        '           <td>'+title_icon_tech +':</td>'+
        '           <td>';
                            var parts = technologies_in_proyect.split('~');

                            if(parts.length>1)
                            {
                                for (var x = 0; x < parts.length - 1; x++)
                                {
                                    sOut    += '<span class="label label-info " style="font-size: 12px">'+parts[x]+'</span>&nbsp&nbsp&nbsp'
                                }
                            }
                            else
                            {
                                sOut += '<span class="label label-danger" style="font-size: 12px">    ' + msg_technologies + '</span>&nbsp&nbsp&nbsp';
                            }
    sOut    +='     <button class="btn btn-info btn-xs"    title="'+title_icon_tech      +'" onclick="location.href=\''+location_icon_tech+'\'"      ><i class="fa fa-pagelines" ></i></button>' +
        '           </td>'+
        '       </tr>';
    sOut    += '    <tr><td >'+title_email+':</td>' +
        '           <td >'+info_email+'</td>' +
        '           <td>'+title_icon_languaje+': </td>' +
        '           <td><button class="btn btn-warning btn-xs" title="'+title_icon_languaje  +'" onclick=""                                          ><i class="fa fa-eye"       ></i></button>&nbsp&nbsp&nbsp</td>' +
        '       </tr>';


     sOut    += '    <tr><td>'+title_tags+':</td>' +
        '           <td>';
                            var parts = info_tags.split('~');

                            for(var x=0; x<parts.length; x++)
                            {
                               sOut    += '<span class="label label-primary " style="font-size: 12px">'+parts[x]+'</span>&nbsp&nbsp&nbsp'
                            }
    sOut    +='     </td>' +
        '           <td>'+title_icon_enumerator+':</td>' +
        '           <td>';
                            var parts = enumerator_in_proyect.split('~');

                            if(parts[0]!=0 || parts[1]!=0)
                            {
                                sOut += '<span class="label label-success fa fa-user" style="font-size: 12px">    ' + parts[0] + '</span>&nbsp&nbsp&nbsp<span class="label label-danger fa fa-user-md" style="font-size: 12px">    ' + parts[1] + '</span>';
                            }
                            else
                            {
                                sOut += '<span class="label label-danger" style="font-size: 12px">    ' + msg_enumerator + '</span>';
                            }
    sOut    +='     &nbsp&nbsp&nbsp<button class="btn btn-success btn-xs" title="'+title_icon_enumerator+'" onclick="location.href=\''+location_icon_enumerator+'\'"><i class="fa fa-group"     ></i></button>' +
        '           </td></tr>';

    sOut    += '<tr>' +
        '           <td>'+title_icon_country+': </td>' +
        '           <td>';

                            var parts = countries_in_proyect.split('~');

                            if(parts.length>1)
                            {
                                for (var x = 0; x < parts.length - 1; x++)
                                {
                                    data = parts[x].split('[-]')
                                    sOut += '<img style="float: left; margin-right: 5px" width="22px" height="13px" title="'+data[1]+'" class="logo img-responsive" src="' + Vimg + 'country-flags/' + data[0] + '.png" alt="country">'
                                }
                            }
                            else
                            {
                                sOut += '<span class="label label-danger" style="font-size: 12px;">    ' + msg_countries + '</span>&nbsp&nbsp&nbsp';
                            }

    sOut    +='     <button class="btn btn-primary btn-xs" title="'+title_icon_country   +'" onclick="location.href=\''+location_icon_country+'\'"   ><i class="fa fa-globe"     ></i></button>' +
        '           </td>' +
        '           <td>'+title_icon_question+':</td>' +
        '           <td><button class="btn btn-default btn-xs" title="'+title_icon_question   +'" onclick="location.href=\''+location_icon_question+'\'"><i class="fa fa-comments-o"></i></button>&nbsp&nbsp&nbsp</td>' +
        '       </tr>';





    sOut    += '</table>';

    return sOut;
}

$(document).ready(function() {

    $('#dynamic-table').dataTable( {
        "aaSorting": [[ 4, "desc" ]]
    } );

    /*
     * Insert a 'details' column to the table
     */
    var nCloneTh = document.createElement( 'th' );
    var nCloneTd = document.createElement( 'td' );
    nCloneTd.innerHTML = '<img src="img/details_open.png">';
    nCloneTd.className = "center";

    $('#hidden-table-info thead tr').each( function () {
        this.insertBefore( nCloneTh, this.childNodes[0] );
    } );

    /*$('#hidden-table-info tbody tr').each( function () {
        this.insertBefore(  nCloneTd.cloneNode( true ), this.childNodes[0] );
    } );*/

    /*
     * Initialse DataTables, with no sorting on the 'details' column
     */
    var oTable = $('#hidden-table-info').dataTable( {
        "aoColumnDefs": [
            { "bSortable": false, "aTargets": [ 0 ] }
        ],
        "aaSorting": [[1, 'asc']]
    });

    /* Add event listener for opening and closing details
     * Note that the indicator for showing which row is open is not controlled by DataTables,
     * rather it is done here
     */
    $(document).on('click','#hidden-table-info tbody td img',function () {
        var nTr = $(this).parents('tr')[0];
        if ( oTable.fnIsOpen(nTr) )
        {
            /* This row is already open - close it */
            this.src = Vimg+'img/details_open.png';
            oTable.fnClose( nTr );
        }
        else
        {
            /* Open this row */
            this.src = Vimg+'img/details_close.png';
            oTable.fnOpen( nTr, fnFormatDetails(oTable, nTr), 'details' );
        }
    } );
} );

function details(img,titletags,titleinvestigator,titleemail,infotags,infoinvestigator,infoemail,titleiconcountry,locationiconcountry,titleicontech,locationicontech,titleiconlanguaje,locationiconlanguaje,titleiconenumerator,locationiconenumerator,titleiconquestion,locationiconquestion,countries,msgcountries,technologies,msgtechnologies,enumerator,msgenumerator)
{
    Vimg                    = img;
    title_tags              = titletags;
    title_investigator      = titleinvestigator;
    title_email             = titleemail;
    info_tags               = infotags;
    info_investigator       = infoinvestigator;
    info_email              = infoemail;
    title_icon_country      = titleiconcountry;
    location_icon_country   = locationiconcountry;
    title_icon_tech         = titleicontech;
    location_icon_tech      = locationicontech;
    title_icon_languaje     = titleiconlanguaje;
    location_icon_languaje  = locationiconlanguaje;
    title_icon_enumerator   = titleiconenumerator;
    location_icon_enumerator= locationiconenumerator;
    title_icon_question     = titleiconquestion;
    location_icon_question  = locationiconquestion;
    countries_in_proyect    = countries
    msg_countries           = msgcountries
    technologies_in_proyect  = technologies
    msg_technologies        = msgtechnologies
    enumerator_in_proyect   = enumerator
    msg_enumerator          = msgenumerator
}