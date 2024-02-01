def check_admin(user) -> bool:
    roles = user.roles
    
    if roles:
        for role in roles:
            if role.name == 'Admin' or role.name == 'Mysterious Aura':
                return True

    return False