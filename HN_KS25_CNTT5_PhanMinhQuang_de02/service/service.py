from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError
from models.models import Device, DeviceType
from schemas.schemas import DeviceResponse

def add_device(db, info):
    if db.query(DeviceType).filter(DeviceType.id == info.device_type_id).first() is None:
        return 404, 'Loại thiết bị không tồn tại', None
    if db.query(Device).filter(Device.device_code == info.device_code).first():
        return 409, 'Mã thiết bị đã tồn tại', None
    device = Device(**info.model_dump())
    try:
        db.add(device)
        db.commit()
        db.refresh(device)
    except IntegrityError:
        db.rollback()
        return 409, 'Mã thiết bị bị trùng hoặc dữ liệu không hợp lệ', None
    return 201, 'Thêm thiết bị thành công', DeviceResponse.model_validate(device).model_dump()

def get_devices(db):
    devices = db.query(Device).options(joinedload(Device.device_type)).all()
    return [DeviceResponse.model_validate(item).model_dump() for item in devices]

def remove_type(db, type_id):
    item = db.query(DeviceType).filter(DeviceType.id == type_id).first()
    if item is None:
        return 404, 'Không tìm thấy loại thiết bị'
    if db.query(Device).filter(Device.device_type_id == type_id).first():
        return 409, 'Loại thiết bị đang có thiết bị, không thể xóa'
    db.delete(item)
    db.commit()
    return 200, 'Xóa loại thiết bị thành công'
