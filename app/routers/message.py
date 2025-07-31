from fastapi import APIRouter, Depends
from app.models.message import RequestMessage, ResponseMessage
from app.services.llm_service import LLMService

router = APIRouter(
    prefix="/api/mis02",
    tags=["messages"],
    responses={404: {"description": "Not found"}}
)
def get_llm_service():
    return LLMService()

@router.post("/generate-response", response_model=ResponseMessage)
async def generate_response(
    request_message: RequestMessage, 
    llm_service: LLMService = Depends(get_llm_service)
    ):
    """
    Generate a response from the LLM based on the request message.
    """
    return llm_service.generate_response(request_message)
