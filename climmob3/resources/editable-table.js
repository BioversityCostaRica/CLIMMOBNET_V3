/*$(document).ready(function() {
    EditableTable.init();
});*/
var EditableTable = function () {

    return {

        //main function to initiate the module
        init: function () {
            function restoreRow(oTable, nRow) {
                var aData = oTable.fnGetData(nRow);
                var jqTds = $('>td', nRow);

                for (var i = 0, iLen = jqTds.length; i < iLen; i++) {

                    oTable.fnUpdate(aData[i], nRow, i, false);
                }

                oTable.fnDraw();
            }

            function editRow(oTable, nRow) {
                var aData = oTable.fnGetData(nRow);
                var jqTds = $('>td', nRow);
                console.log(aData);
                for (var i=0; i<= jqTds.length-3;i++){
                    console.log(jqTds[i].innerHTML);

                    jqTds[i].innerHTML = '<input type="text" class="form-control small" value="' + aData[i] + '">';

                }
                jqTds[aData.length-2].innerHTML = '<a class="edit" href="">Save</a>';
                jqTds[aData.length-1].innerHTML = '<a class="cancel" href="" >Cancel</a>';

            }

            function saveRow(oTable, nRow) {

                var jqInputs = $('input', nRow);

                for (var i=0; i<= jqInputs.length-3;i++){
                    oTable.fnUpdate(jqInputs[i].value, nRow, i, false);
                    //jqTds[i].innerHTML = '<input type="text" class="form-control small" value="' + aData[i] + '">';
                }

                /*jqTds[jqInputs.length-2].innerHTML = '<a class="edit" href="javascript:;">Save</a>';
                jqTds[jqInputs.length-1].innerHTML = '<a class="cancel" href="javascript:;">Cancel</a>';

                oTable.fnUpdate(jqInputs[0].value, nRow, 0, false);
                oTable.fnUpdate(jqInputs[1].value, nRow, 1, false);
                oTable.fnUpdate(jqInputs[2].value, nRow, 2, false);
                oTable.fnUpdate(jqInputs[3].value, nRow, 3, false);*/


                oTable.fnUpdate('<a class="edit" href="">Edit</a>', nRow, jqInputs.length-2, false);
                oTable.fnUpdate('<a class="delete" href="">Delete</a>', nRow, jqInputs.length-1, false);
                oTable.fnDraw();
            }

            function cancelEditRow(oTable, nRow) {
                var jqInputs = $('input', nRow);

                 for (var i=0; i<= jqInputs.length-3;i++){
                    oTable.fnUpdate(jqInputs[i].value, nRow, i, false);

                    //jqTds[i].innerHTML = '<input type="text" class="form-control small" value="' + aData[i] + '">';
                }

                /*oTable.fnUpdate(jqInputs[0].value, nRow, 0, false);
                oTable.fnUpdate(jqInputs[1].value, nRow, 1, false);
                oTable.fnUpdate(jqInputs[2].value, nRow, 2, false);
                oTable.fnUpdate(jqInputs[3].value, nRow, 3, false);
                oTable.fnUpdate('<a class="edit" href="">Edit</a>', nRow, 4, false);*/
                oTable.fnUpdate('<a class="edit" href="">Edit</a>', nRow, jqInputs.length-2, false);
                oTable.fnDraw();
            }

            var oTable = $('#editable-sample').dataTable({
                "aLengthMenu": [
                    [5, 15, 20, -1],
                    [5, 15, 20, "All"] // change per page values here
                ],
                // set the initial value
                "iDisplayLength": 5,
                "sDom": "<'row'<'col-lg-6'l><'col-lg-6'f>r>t<'row'<'col-lg-6'i><'col-lg-6'p>>",
                "sPaginationType": "bootstrap",
                "oLanguage": {
                    "sLengthMenu": "_MENU_ records per page",
                    "oPaginate": {
                        "sPrevious": "Prev",
                        "sNext": "Next"
                    }
                },
                "aoColumnDefs": [{
                        'bSortable': false,
                        'aTargets': [0]
                    }
                ]
            });

            jQuery('#editable-sample_wrapper .dataTables_filter input').addClass("form-control medium"); // modify table search input
            jQuery('#editable-sample_wrapper .dataTables_length select').addClass("form-control xsmall"); // modify table per page dropdown

            var nEditing = null;



            $('#editable-sample a.delete').on('click', function (e) {
                e.preventDefault();

                if (confirm("Are you sure to delete this row ?") == false) {
                    return;
                }

                var nRow = $(this).parents('tr')[0];
                oTable.fnDeleteRow(nRow);
                alert("Deleted! Do not forget to do some ajax to sync with backend :)");
            });

            $('#editable-sample a.cancel').on('click', function (e) {
                e.preventDefault();
                if ($(this).attr("data-mode") == "new") {
                    var nRow = $(this).parents('tr')[0];
                    oTable.fnDeleteRow(nRow);
                } else {
                    restoreRow(oTable, nEditing);
                    nEditing = null;
                }
            });

            $('#editable-sample a.edit').on('click', function (e) {

                e.preventDefault();

                /* Get the row as a parent of the link that was clicked on */

                var nRow = $(this).parents('tr')[0];

                if (nEditing !== null && nEditing != nRow) {
                    /* Currently editing - but not this row - restore the old before continuing to edit mode */
                    restoreRow(oTable, nEditing);
                    editRow(oTable, nRow);
                    nEditing = nRow;
                } else if (nEditing == nRow && this.innerHTML == "Save") {
                    /* Editing this row and want to save it */

                    saveRow(oTable, nEditing);
                    nEditing = null;
                    alert("Updated! Do not forget to do some ajax to sync with backend :)");
                } else {
                    /* No edit in progress - let's start one */
                    editRow(oTable, nRow);
                    nEditing = nRow;
                }
            });
        }

    };

}();

