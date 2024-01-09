from flask import Flask
from flask_restful import Api
from resources.device import Devices, Device

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_request
def create_db():
    db.create_all()

api.add_resource(Devices, '/devices/')
api.add_resource(Device, '/devices/<int:device_id>')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True)