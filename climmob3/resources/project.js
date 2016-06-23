/**
 * Created by cquiros on 29/02/16.
 */

jQuery('.tm-inputadd').tagsManager
(
    {
        output:'#newproject_tag',
        tagsContainer:'#space_tags',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-add'
    }
);

jQuery('.tm-inputadd2').tagsManager
(
    {
        output:'#newproject_tagE',
        tagsContainer:'#space_tagsE',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-add'
    }
);

jQuery('.tm-inputupt').tagsManager
(
    {
        output:'#updproject_tag',
        tagsContainer: '#space_tagsM',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-edit'
    }
);

jQuery('.tm-inputupt2').tagsManager
(
    {
        output:'#updproject_tagE',
        tagsContainer: '#space_tagsME',
        delimiters: [9, 13, 126],
        tagClass:'tm-tag-edit'
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


function showModifyProject(code,name,description,tags,principal_investigator,mail_address)
{
    $('#updproject_code').val(code)
    $('#updproject_name').val(name)
    $('#updproject_description').val(description)

    var different_tags = tags.split('~')
    var number_of_options = different_tags.length-1
    $('#tags1').val('')
    jQuery('.tm-inputupt').tagsManager('empty');

    for (var i=0; i<= number_of_options; i++)
    {
        jQuery('.tm-inputupt').tagsManager('pushTag',different_tags[i])
    }

    $('#updproject_principal_investigator').val(principal_investigator)
    $('#updproject_mail_address').val(mail_address)

    $('#modifyProject').modal('show');
}

function showDeleteProject(code)
{
    document.getElementById('delproject_code').value=code;
    $('#deleteProject').modal('show');
}


