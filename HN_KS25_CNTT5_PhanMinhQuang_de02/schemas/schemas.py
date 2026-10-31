from pydantic import BaseModel, Field, ConfigDict

class DeviceCreate(BaseModel):
    device_code: str = Field(min_length=4, max_length=10)
    price: float = Field(gt=0)
    device_type_id: int

class DeviceTypeResponse(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class DeviceResponse(BaseModel):
    id: int
    device_code: str
    price: float
    device_type: DeviceTypeResponse
    model_config = ConfigDict(from_attributes=True)
