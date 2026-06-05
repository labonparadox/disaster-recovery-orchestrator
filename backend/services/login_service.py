from services.signup_service import users

def login_user(user):

    for existing_user in users:

        if (
            existing_user["email"] == user.email
            and existing_user["password"] == user.password
        ):
            return {
                "message": "Login Successful"
            }

    return {
        "message": "Invalid Credentials"
    }