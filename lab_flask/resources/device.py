from flask_restful import Resource, reqparse, request
from models.device import DeviceModel

def get_obj_dev_info(type_req=False, name_req=False):
        arg_recv = reqparse.RequestParser()
        arg_recv.add_argument('id', required=False)
        arg_recv.add_argument('type', type=str, required=type_req, help='The field \'type\' is required')
        arg_recv.add_argument('name', type=str, required=name_req, help='The field \'name\' is required')
        arg_recv.add_argument('enabled', type=bool, required=False)
        arg_recv.add_argument('state', type=bool, required=False)
        
        return arg_recv.parse_args()

class Devices(Resource):
    def get(self):
        devices = DeviceModel()
        return devices.read_all(), 200

    def post(self):        
        values = get_obj_dev_info(True, True)
        try:
            device = DeviceModel(**values)
            device.save_device()
        
            return device.json(), 201
        except:
            return {'message': 'Erro to add new device'}, 500

class Device(Resource):

    def get(self, device_id):
        device = DeviceModel().find_device_by_id(device_id)

        if device:
            return device.json(), 200
        
        return {'message': 'Device was not found'}, 400

    def put(self, device_id):
        try:
            device = DeviceModel().find_device_by_id(device_id)

            if device:
                values = get_obj_dev_info()
                device.update_device(**values)
                device.save_device()
                
                return device.json(), 201

            return {'message': 'Device was not found'}, 400

        except:
            return {f'message': 'Erro to edit device {device_id}'}, 500