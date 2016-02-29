/**
 * Created by cquiros on 29/02/16.
 */

function showAddProject()
{
    document.getElementById('project_code').value="";
    document.getElementById('project_desc').value="";
    $('#addNewProject').modal('show');
};

function showModifyProject(code,description)
{
    document.getElementById('updproject_code').value=code;
    document.getElementById('updproject_desc').value=description;

    $('#modifyProject').modal('show');
}

function showDeleteProject(code)
{
    document.getElementById('delproject_code').value=code;
    $('#deleteProject').modal('show');
};