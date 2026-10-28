import voluptuous as vol
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import config_validation as cv, device_registry as dr

DOMAIN = "delete_orphan"
SERVICE_REMOVE = "remove_device"

SERVICE_SCHEMA = vol.Schema({
    vol.Required("device_id"): cv.string,
})

async def async_setup(hass: HomeAssistant, config: dict):
    async def handle_remove_device(call):
        device_id = call.data.get("device_id")
        dev_reg = dr.async_get(hass)
        
        device = dev_reg.async_get(device_id)
        if device:
            dev_reg.async_remove_device(device_id)
            hass.components.persistent_notification.create(
                f"Successfully removed orphan device ID: {device_id}",
                title="Orphan Device Removed"
            )
        else:
            hass.components.persistent_notification.create(
                f"Device ID {device_id} not found in registry.",
                title="Device Not Found"
            )

    hass.services.async_register(
        DOMAIN, SERVICE_REMOVE, handle_remove_device, schema=SERVICE_SCHEMA
    )
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return True
