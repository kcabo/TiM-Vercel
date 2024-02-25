from app.models import db, User
# from app.redis_setup import conn

class UserNotFound(Exception):
    def __init__(self, line_id):
        print(f'{line_id}による不明なアクセスを検知')


def validate_user(line_id):
    user = User.query.filter_by(lineid=line_id).one_or_none()
    if user: 
        menu_id = user.focus
        if menu_id:
            return int(menu_id)
        else:
            return 0
    
    raise UserNotFound(line_id)
