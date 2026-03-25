from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from .voice import generate_voice


class VoiceMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        response = await call_next(request)

        if request.method in ["POST", "PUT", "DELETE"]:

            try:

                message = f"{request.url.path} updated successfully"

                audio_file = generate_voice(message)

                if response.headers.get("content-type") == "application/json":

                    body = b"".join([chunk async for chunk in response.body_iterator])

                    data = {}

                    try:
                        import json
                        data = json.loads(body)
                    except:
                        data = {"message": "success"}

                    data["voice_url"] = "/" + audio_file

                    return JSONResponse(content=data)

            except Exception as e:
                print("Voice error:", e)

        return response
