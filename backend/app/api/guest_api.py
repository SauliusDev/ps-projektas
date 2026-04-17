from fastapi import APIRouter

from app.application.deals_controller import DealsController
from app.domain.schemas import TripListResponse

router = APIRouter(prefix='/api/guest', tags=['guest'])
deals_controller = DealsController()


@router.get('/deals', response_model=TripListResponse)
def list_guest_deals() -> TripListResponse:
    return deals_controller.list_deals()
