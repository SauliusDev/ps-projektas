from pydantic import BaseModel


class TripRead(BaseModel):
    id: int
    title: str
    city: str


class TripListResponse(BaseModel):
    items: list[TripRead]
