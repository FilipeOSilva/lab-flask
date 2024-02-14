from sql_alchemy import db

class UserModel(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    login = db.Column(db.String(32), unique=True, nullable=False)
    passw = db.Column(db.String(32))
    enabled = db.Column(db.Boolean)

    def __init__(self, name=None, type=None, enabled=True, login=None, passw=None):
        self.name = name
        self.enabled = bool(enabled)
        self.login = login
        self.passw = passw

    def json(self):
        return {
           'id': self.id,
           'name': self.name,
           'enabled': self.enabled,
           'login': self.login
            }

    @classmethod
    def find_user_by_login(cls, user_login):
        user = cls.query.filter_by(login=user_login).first()
        
        if user:
            return user 

        return None

    @classmethod
    def find_user_by_id(cls, user_id):
        user = cls.query.filter_by(id=user_id).first()
        
        if user:
            return user

        return None

    def save_user(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @classmethod
    def read_all(cls):
        json_users = []

        users = cls.query.all()
        
        for user in users:
            json_users.append(user.json())

        return json_users

    def update_user(self, name=None, enabled=None, login=None, passw=None):
        self.name = name if name != None else self.name
        self.enabled = enabled if enabled != None else self.enabled

    def delete_user(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
