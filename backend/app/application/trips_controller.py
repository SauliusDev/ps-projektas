from app.domain.schemas import TripListResponse, TripRead
from app.infrastructure.repositories import TripRepository


class TripsController:
    def __init__(self, trip_repository: TripRepository | None = None) -> None:
        self.trip_repository = trip_repository or TripRepository()

    def list_trips(self, traveler_id: int) -> TripListResponse:
        trips = self.trip_repository.list_for_traveler(traveler_id)
        return TripListResponse(
            items=[TripRead(id=trip.id, title=trip.title, city=trip.city) for trip in trips]
        )
