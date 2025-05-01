import os
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant
from aiohttp import web

# Temp file path (you can adjust this)
TEMP_PATH = "/config/nmi_latest.csv"

class UploadNMIDataView(HomeAssistantView):
    url = "/api/nmi/upload"
    name = "api:nmi_upload"
    requires_auth = False  # Set to True for auth-protected

    def __init__(self, hass: HomeAssistant):
        self.hass = hass

    async def post(self, request: web.Request):
        data = await request.read()
        with open(TEMP_PATH, "wb") as f:
            f.write(data)
        return self.json({"status": "ok", "message": f"Saved to {TEMP_PATH}"})


class GetNMIDataView(HomeAssistantView):
    url = "/api/nmi/data"
    name = "api:nmi_get"
    requires_auth = False  # Set to True for auth-protected

    def __init__(self, hass: HomeAssistant):
        self.hass = hass

    async def get(self, request: web.Request):
        if not os.path.exists(TEMP_PATH):
            return self.json({"error": "No file found"}, status_code=404)
        with open(TEMP_PATH, "r") as f:
            content = f.read()
        return web.Response(text=content, content_type="text/plain")
