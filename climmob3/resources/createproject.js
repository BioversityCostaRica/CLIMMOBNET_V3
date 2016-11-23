/**
 * Created by brandon on 21/11/16.
 */


jQuery(document).ready(function()
{
    showAddProject();

});

jQuery('.tm-inputadd').tagsManager
(
    {
        output:'#newproject_tag',
        tagsContainer:'#space_tags',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-add'
    }
);

function showAddProject()
{
    $('#newproject_code').val('')
    $('#newproject_name').val('')
    $('#newproject_description').val('')
    $('#tags').val('')
    jQuery('.tm-inputadd').tagsManager('empty');
    $('#newproject_principal_investigator').val('')
    $('#newproject_mail_address').val('')


    $('#addNewProject').modal('show');

};

