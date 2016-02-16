/*---LEFT BAR ACCORDION----*/
$(function() {
    $('#nav-accordion').dcAccordion({
        eventType: 'click',
        autoClose: true,
        saveState: true,
        disableLink: true,
        speed: 'slow',
        showCount: false,
        autoExpand: true,
//        cookie: 'dcjq-accordion-1',
        classExpand: 'dcjq-current-parent'
    });
});

// right slidebar
$(function(){
 $.slidebars();
});

function showDeleteMode(modelId)
{

    var theForm = document.forms['deleteModelForm'];
    var oldInput = document.getElementById('deleteModelID')
    if (oldInput != null)
    {
        theForm.removeChild(oldInput);
    }
    var newInput = document.createElement('input');
    newInput.type = 'hidden';
    newInput.name = 'deleteModelID';
    newInput.id = 'deleteModelID';
    newInput.value = modelId;
    theForm.appendChild(newInput);

    $('#deleteModel').modal('show');
};

function showDeleteResult(resultId)
{

    var theForm = document.forms['deleteResultForm'];
    var oldInput = document.getElementById('deleteResultID')
    if (oldInput != null)
    {
        theForm.removeChild(oldInput);
    }
    var newInput = document.createElement('input');
    newInput.type = 'hidden';
    newInput.name = 'deleteResultID';
    newInput.id = 'deleteResultID';
    newInput.value = resultId;
    theForm.appendChild(newInput);

    $('#deleteResult').modal('show');
};


function showDeleteResultContainer(containerId)
{

    var theForm = document.forms['deleteContainerForm'];
    var oldInput = document.getElementById('deleteContainerID')
    if (oldInput != null)
    {
        theForm.removeChild(oldInput);
    }
    var newInput = document.createElement('input');
    newInput.type = 'hidden';
    newInput.name = 'deleteContainerID';
    newInput.id = 'deleteContainerID';
    newInput.value = containerId;
    theForm.appendChild(newInput);


    $('#deleteContainer').modal('show');
};

function showModifyResultContainer(containerId,code,description)
{
    document.getElementById('updresult_code').value=code;
    document.getElementById('updresult_description').value=description;

    var theForm = document.forms['modifyContainerForm'];
    var oldInput = document.getElementById('modifyContainerID')
    if (oldInput != null)
    {
        theForm.removeChild(oldInput);
    }
    var newInput = document.createElement('input');
    newInput.type = 'hidden';
    newInput.name = 'modifyContainerID';
    newInput.id = 'modifyContainerID';
    newInput.value = containerId;
    theForm.appendChild(newInput);


    $('#modifyContainer').modal('show');
};

function showAddResultContainer()
{
    document.getElementById('result_code').value="";
    document.getElementById('result_description').value="";
    $('#addNewContainer').modal('show');
};

function showRunModalWindow(modelid)
{
    var theForm = document.forms['runModelForm'];
    var oldInput = document.getElementById('modelID')
    if (oldInput != null)
    {
        theForm.removeChild(oldInput);
    }
    var newInput = document.createElement('input');
    newInput.type = 'hidden';
    newInput.name = 'modelID';
    newInput.id = 'modelID';
    newInput.value = modelid;
    theForm.appendChild(newInput);
    $('#myModal').modal('show');
};

function showDeleteSupplementModalWindow(supplementID)
{
    var theForm = document.forms['DelFeedForm'];
    var oldInput = document.getElementById('DeletesupplementID')
    if (oldInput != null)
    {
        theForm.removeChild(oldInput);
    }
    var newInput = document.createElement('input');
    newInput.type = 'hidden';
    newInput.name = 'supplementID';
    newInput.id = 'DeletesupplementID';
    newInput.value = supplementID;
    theForm.appendChild(newInput);
    $('#myModalDelete').modal('show');
};

function showUpdateSupplementModalWindow(supplementID,feedID,amount,meals)
{
    var theForm = document.forms['updFeedForm'];
    var oldInput = document.getElementById('UpdatesupplementID')
    if (oldInput != null)
    {
        theForm.removeChild(oldInput);
    }
    var newInput = document.createElement('input');
    newInput.type = 'hidden';
    newInput.name = 'supplementID';
    newInput.id = 'UpdatesupplementID';
    newInput.value = supplementID;
    theForm.appendChild(newInput);

    document.getElementById('UPDfeedID').value=feedID;

    $('#UPDfeedAmount').val(amount);
    $('#UPDnumMeals').val(meals);
    $('#myModalUpdate').modal('show');
};


var Script = function () {

//    sidebar dropdown menu auto scrolling

    jQuery('#sidebar .sub-menu > a').click(function () {
        var o = ($(this).offset());
        diff = 250 - o.top;
        if(diff>0)
            $("#sidebar").scrollTo("-="+Math.abs(diff),500);
        else
            $("#sidebar").scrollTo("+="+Math.abs(diff),500);
    });

//    sidebar toggle

    $(function() {
        function responsiveView() {
            var wSize = $(window).width();
            if (wSize <= 768) {
                $('#container').addClass('sidebar-close');
                $('#sidebar > ul').hide();
            }

            if (wSize > 768) {
                $('#container').removeClass('sidebar-close');
                $('#sidebar > ul').show();
            }
        }
        $(window).on('load', responsiveView);
        $(window).on('resize', responsiveView);
    });

    $('.fa-bars').click(function () {
        if ($('#sidebar > ul').is(":visible") === true) {
            $('#main-content').css({
                'margin-left': '0px'
            });
            $('#sidebar').css({
                'margin-left': '-210px'
            });
            $('#sidebar > ul').hide();
            $("#container").addClass("sidebar-closed");
        } else {
            $('#main-content').css({
                'margin-left': '210px'
            });
            $('#sidebar > ul').show();
            $('#sidebar').css({
                'margin-left': '0'
            });
            $("#container").removeClass("sidebar-closed");
        }
    });

// custom scrollbar
    $("#sidebar").niceScroll({styler:"fb",cursorcolor:"#e8403f", cursorwidth: '3', cursorborderradius: '10px', background: '#404040', spacebarenabled:false, cursorborder: ''});

    $("html").niceScroll({styler:"fb",cursorcolor:"#e8403f", cursorwidth: '6', cursorborderradius: '10px', background: '#404040', spacebarenabled:false,  cursorborder: '', zindex: '1000'});



// widget tools

    jQuery('.panel .tools .fa-chevron-down').click(function () {
        var el = jQuery(this).parents(".panel").children(".panel-body");
        if (jQuery(this).hasClass("fa-chevron-down")) {
            jQuery(this).removeClass("fa-chevron-down").addClass("fa-chevron-up");
            el.slideUp(200);
        } else {
            jQuery(this).removeClass("fa-chevron-up").addClass("fa-chevron-down");
            el.slideDown(200);
        }
    });

    jQuery('.panel .tools .fa-times').click(function () {
        jQuery(this).parents(".panel").parent().remove();
    });
    
    


//    tool tips

    $('.tooltips').tooltip();

//    popovers

    $('.popovers').popover();



// custom bar chart

    if ($(".custom-bar-chart")) {
        $(".bar").each(function () {
            var i = $(this).find(".value").html();
            $(this).find(".value").html("");
            $(this).find(".value").animate({
                height: i
            }, 2000)
        })
    }


    $("#user_cnty").select2();
    $("#user_sector").select2();
    $("#feed_type").select2();
    $("#cnty_cod").select2();
    $("#resultSet").select2();
    $("#model_bforageID").select2();
    $(".FeedSelect").select2();
   


}();