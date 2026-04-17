from fastapi import APIRouter

from app.application.trips_controller import TripsController
from app.domain.schemas import TripListResponse

router = APIRouter(prefix='/api/admin', tags=['admin'])
trips_controller = TripsController()


@router.get('/trips', response_model=TripListResponse)
def list_admin_trips() -> TripListResponse:
    return trips_controller.list_trips(traveler_id=0)
