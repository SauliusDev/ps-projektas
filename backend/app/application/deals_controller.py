from app.domain.schemas import TripListResponse, TripRead


class DealsController:
    def list_deals(self) -> TripListResponse:
        return TripListResponse(
            items=[TripRead(id=101, title='City Break Deal', city='Kaunas')]
        )
