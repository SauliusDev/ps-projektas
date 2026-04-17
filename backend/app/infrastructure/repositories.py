from app.domain.entities import Trip


class TripRepository:
    def list_for_traveler(self, traveler_id: int) -> list[Trip]:
        return [Trip(id=1, title='Weekend Trip', city='Vilnius')]
