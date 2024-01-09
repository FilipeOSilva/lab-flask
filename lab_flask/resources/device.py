from flask_restful import Resource, reqparse
from models.device import DeviceModel

class Devices(Resource):
    def get(self):
        devices = DeviceModel()
        return devices.read_all(), 200

    def post(self):        
        arg_recv = reqparse.RequestParser()
        arg_recv.add_argument('type')
        arg_recv.add_argument('name')
        arg_recv.add_argument('enabled')
        arg_recv.add_argument('state')
        
        values = arg_recv.parse_args()
        
        device = DeviceModel(None, values['type'], values['name'], int(values['enabled']), int(values['state']))
        device.save_device()
        
        return device.json()

class Device(Resource):

    def get(self, device_id):
        device = DeviceModel().find_device_by_id(device_id)

        if device:
            return device.json(), 200
        
        return {"message": "device don\'t found"}, 400

    def put(self, id):
        ...