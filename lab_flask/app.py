from flask import Flask
from flask_restful import Api
from resources.device import Devices #, Device
# from resources.user import User, Users, UserLogin
from flask_jwt_extended import JWTManager
import secrety
from blocklist import BLOCKLIST
# from models.user import UserModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = secrety.PATH_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_BLOCKLIST_ENABLED'] = True
app.config['JWT_SECRET_KEY'] = secrety.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = secrety.JWT_ACCESS_TOKEN_EXPIRES

api = Api(app)
jwt = JWTManager(app)

""" 
   TODO: In the future, change the way the database is started
"""
# @app.before_request
# def create_db():
#     try:
#         db.create_all()
#         first_user = {
#             'name': 'admin',
#             'enabled': True,
#             'login': 'admin',
#             'passw': 'admin'
#             }
#         user = UserModel(**first_user)
#         user.save_user()
#     except:
#         print("exists ADMIN!")

@jwt.token_in_blocklist_loader
def check_blocklist(self, token):
    return token['jti'] in BLOCKLIST

@jwt.revoked_token_loader
def invalid_token(jwt_header, jwt_data):
    return {'message':'Invalid token'}, 401

api.add_resource(Devices, '/devices/')
# api.add_resource(Device, '/devices/<int:device_id>')
# api.add_resource(Users, '/users/')
# api.add_resource(User, '/users/<int:user_id>')
# api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    # from sql_alchemy import db
    # db.init_app(app)
    app.run(host='0.0.0.0', debug=True)
