from sql_alchemy import db

class DeviceModel(db.Model):

    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(16))
    name = db.Column(db.String(32))
    enabled = db.Column(db.Boolean)
    state = db.Column(db.Integer)


    def __init__(self, id=None, name=None, type=None, enabled=None, state=None):
        self.id = id
        self.type = type
        self.name = name
        self.enabled = bool(enabled)
        self.state = state 

    def json(self):
        return {
           'id': self.id,
           'type': self.type,
           'name': self.name,
           'enabled': self.enabled,
           'state': self.state
            }

    @classmethod
    def find_device_by_id(cls, device_id):
        device = cls.query.filter_by(id=device_id).first()
        
        if device:
            return device

        return None

    def save_device(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read_all(cls):
        json_devices = []

        devices = cls.query.all()
        
        for device in devices:
            json_devices.append(device.json())

        return json_devices

    def update_device(self, name=None, type=None, enabled=None):
        self.type = type if type != None else self.type
        self.name = name if name != None else self.name
        self.enabled = enabled if enabled != None else self.enabled