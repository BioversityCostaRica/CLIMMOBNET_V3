/**
 * Created by cquiros on 29/02/16.
 */

function showAddProject()
{
    $('#newproject_code').val('')
    $('#newproject_name').val('')
    $('#newproject_description').val('')
    $('#newproject_otro2').val('')
    $('#newproject_principal_investigator').val('')
    $('#newproject_mail_address').val('')
    $('#newproject_country').val('')
    $('#newproject_technology').val('')
    $('#newproject_languaje').val('')

    $('#addNewProject').modal('show');
};

function showModifyProject(code,name,description,otro2,principal_investigator,mail_address,country,technology,languaje)
{
    $('#updproject_code').val(code)
    $('#updproject_name').val(name)
    $('#updproject_description').val(description)
    $('#updproject_otro2').val(otro2)
    $('#updproject_principal_investigator').val(principal_investigator)
    $('#updproject_mail_address').val(mail_address)
    $('#updproject_country').val(country)
    $('#updproject_technology').val(technology)
    $('#updproject_languaje').val(languaje)

    $('#modifyProject').modal('show');
}

function showDeleteProject(code)
{
    document.getElementById('delproject_code').value=code;
    $('#deleteProject').modal('show');
};