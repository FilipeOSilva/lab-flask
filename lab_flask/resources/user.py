from flask_restful import Resource, reqparse, request
from models.user import UserModel

class Users(Resource):
    def get(self):
        users = UserModel()
        return users.read_all(), 200

    def post(self):        
        values_args = reqparse.RequestParser()
        values_args.add_argument('name', type=str, required=True, help='The field \'name\' cannot be left blank.')
        values_args.add_argument('login', type=str, required=True, help='The field \'login\' cannot be left blank.')
        values_args.add_argument('passw', type=str, required=True, help='The field \'passw\' cannot be left blank.')
        values_args.add_argument('enabled', type=bool)
        data = values_args.parse_args()

        try:
            if UserModel.find_user_by_login(data['login']):
                return {'message': f'The login {data["login"]} already exists.'}, 400

            user = UserModel(**data)
            user.save_user()
        
            return user.json(), 201
        except:
            return {'message': 'Erro to add new user.'}, 500

class User(Resource):

    def get(self, user_id):
        user = UserModel().find_user_by_id(user_id)

        if user:
            return user.json(), 200
        
        return {'message': 'User was not found.'}, 400

    def delete(self, user_id):
        try:
            user = UserModel().find_user_by_id(user_id)

            if user:
                user.delete_user()
                
                return {'message': 'User deleted.'}, 201

            return {'message': 'User was not found'}, 400

        except:
            return {f'message': 'Erro to delete user {user_id}.'}, 500