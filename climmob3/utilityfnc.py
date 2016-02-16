from dbuserfunctions import userExists, emailExists
#Form validation
def valideForm(data):
    error_summary = {}
    errors = False

    if (data["user_password"] != data["user_password2"]):
        error_summary["InvalidPassword"] = "Invalid password"
        errors = True
    if userExists(data["user_name"]):
        error_summary["UserExists"] = "User name already exits"
        errors = True
    if emailExists(data["user_email"]):
        error_summary["EmailExists"] = "There is already an account using to this email"
        errors = True
    if data["user_policy"] == "False":
        error_summary["CheckPolicy"] = "You need to accept the terms of service"
        errors = True
    if data["user_name"] == "":
        error_summary["EmptyUser"] = "User cannot be emtpy"
        errors = True
    if data["user_password"] == "":
        error_summary["EmptyPass"] = "Password cannot be emtpy"
        errors = True
    if data["user_fullname"] == "":
        error_summary["EmptyName"] = "Full name cannot be emtpy"
        errors = True
    if data["user_email"] == "":
        error_summary["EmptyEmail"] = "Email cannot be emtpy"
        errors = True

    return errors,error_summary
