from fastapi import APIRouter

from app.application.trips_controller import TripsController
from app.domain.schemas import TripListResponse

router = APIRouter(prefix='/api/traveler', tags=['traveler'])
trips_controller = TripsController()


@router.get('/trips', response_model=TripListResponse)
def list_traveler_trips() -> TripListResponse:
    return trips_controller.list_trips(traveler_id=1)
