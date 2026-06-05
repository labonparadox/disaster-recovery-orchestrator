users = []

def signup_user(user):

    for existing_user in users:

        if existing_user["email"] == user.email:
            return {
                "message": "Email already exists"
            }

    users.append({
        "name": user.name,
        "email": user.email,
        "password": user.password
    })

    return {
        "message": "Signup Successful"
    }