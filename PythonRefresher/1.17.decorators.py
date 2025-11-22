import functools

user = {"username": "seishiro", "access_level": "player"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permisions"
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "manager: 1234"

@make_secure("player")
def get_dashboard_password():
    return "player: player_password"

# get_admin_password = make_secure(get_admin_password)

print(get_dashboard_password())
