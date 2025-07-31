import requests
from app.config import settings
from app.models.message import RequestMessage, ResponseMessage
from fastapi import HTTPException

class LLMService:
    def __init__(self):
        self.api_key = settings.HF_API_KEY
        self.api_uri = "https://router.huggingface.co/v1/chat/completions" 

    def generate_response(self, request_message: RequestMessage) -> ResponseMessage:
        headers = {
            "Authorization": f"Bearer {self.api_key}", 
            "Content-Type": "application/json"
        }
        payload = {
            "messages": [
                {
                    "role": "user", 
                    "content": request_message.request
                }
            ],
            "model": "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai",  
            "use_cache": False
        }

        try:
            response = requests.post(self.api_uri, headers=headers, json=payload)
            reply = response.json()["choices"][0]["message"]["content"]
            return ResponseMessage(reply=reply, timestamp=request_message.timestamp)
        
        except Exception as e:
            raise HTTPException(
                status_code=500, 
                detail=f"Invalid response format: {str(e)}, Response: {response.text}"
            )