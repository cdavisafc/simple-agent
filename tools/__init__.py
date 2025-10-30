from .get_location import get_location_info, get_ip_address
from .get_weather import get_weather_alerts
from .random_stuff import get_random_number

def get_handler(tool_name: str):
    if tool_name == "get_location_info":
        return get_location_info
    if tool_name == "get_ip_address":
        return get_ip_address
    if tool_name == "get_weather_alerts":
        return get_weather_alerts
    if tool_name == "get_random_number":
        return get_random_number