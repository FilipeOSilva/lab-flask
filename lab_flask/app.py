from flask import Flask
from flask_restful import Api
from resources.device import Devices, Device
from resources.user import User, Users
import secrety

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = secrety.PATH_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_request
def create_db():
    db.create_all()

api.add_resource(Devices, '/devices/')
api.add_resource(Device, '/devices/<int:device_id>')
api.add_resource(Users, '/users/')
api.add_resource(User, '/users/<int:user_id>')
# api.add_resource(Login, '/login')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True)
