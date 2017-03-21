/**
 * Created by lluis on 10/11/16.
 */
var des;
var path;

/*function fnFormatDetails ( oTable, nTr,para )
{
    var aData = oTable.fnGetData( nTr );
    var sOut = '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">';
    sOut += '<tr><td>Rendering engine:</td><td>'+aData[1]+' '+aData[4]+'</td></tr>';
    sOut += '<tr><td>Link to source:</td><td>'+para+'</td></tr>';
    sOut += '<tr><td>Extra info:</td><td>And any further details here (img etc)</td></tr>';
    sOut += '</table>';

    return sOut;
}*/
function fnFormatDetails ( oTable, nTr)
{
    //var aData = oTable.fnGetData( nTr );
    var sOut = des;

    return sOut;
}
var oTable
$(document).ready(function() {

     $('.multiple2').multipleSelect({
            width:'100%',
            selectAll:false
        });



    $('#dynamic-table').dataTable( {
        "aaSorting": [[ 4, "desc" ]]
    } );


    /*
     * Insert a 'details' column to the table
     */
    var nCloneTh = document.createElement( 'th' );
    var nCloneTd = document.createElement( 'td' );
    nCloneTd.innerHTML = '<img src="'+path+'img/details_open.png">';
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
     oTable = $('#hidden-table-info').dataTable( {
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

            this.src =path+ "img/details_open.png";
            oTable.fnClose( nTr );
        }
        else
        {

            this.src = path+"img/details_close.png";
            oTable.fnOpen( nTr, fnFormatDetails(oTable, nTr), 'details' );


        }
        $('.multiple').multipleSelect({
            width:'100%',
            selectAll:false
        });
        //$('.multiple').each(function () {
         //   console.log('csacsa');

        //})

    } );








} );

function run(design, path2)
{

    des=design;
    path=path2;

}