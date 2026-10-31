from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.schemas import DeviceCreate
from service.service import add_device, get_devices, remove_type
from responds.responds import response

router = APIRouter()

@router.get('/devices')
def list_devices(db: Session = Depends(get_db)):
    return response(200, 'Lấy danh sách thiết bị thành công', get_devices(db))

@router.post('/devices')
def create_device(info: DeviceCreate, db: Session = Depends(get_db)):
    status, message, data = add_device(db, info)
    return response(status, message, data, None if status == 201 else message)

@router.delete('/device-types/{id}')
def delete_device_type(id: int, db: Session = Depends(get_db)):
    status, message = remove_type(db, id)
    return response(status, message, None, None if status == 200 else message)
