from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DeviceType(Base):
    __tablename__ = 'device_types'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    devices = relationship('Device', back_populates='device_type')

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, index=True)
    device_code = Column(String(10), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    device_type_id = Column(Integer, ForeignKey('device_types.id'), nullable=False)
    device_type = relationship('DeviceType', back_populates='devices')
