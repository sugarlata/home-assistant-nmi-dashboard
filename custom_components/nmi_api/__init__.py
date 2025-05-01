from .api import UploadNMIDataView, GetNMIDataView

async def async_setup(hass, config):
    hass.http.register_view(UploadNMIDataView(hass))
    hass.http.register_view(GetNMIDataView(hass))
    return True
