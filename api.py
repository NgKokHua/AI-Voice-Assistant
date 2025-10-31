import enum 
from typing import Annotated
from livekit.agents import llm
import logging

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)

class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

# Temperature data
temperature_data = {
    Zone.LIVING_ROOM: 22,
    Zone.BEDROOM: 20,
    Zone.KITCHEN: 21,
    Zone.BATHROOM: 23,
    Zone.OFFICE: 21,
}

@llm.function_tool(description="Get the temperature in a specific room.")
async def get_temperature(zone: Annotated[Zone, "The specific zone"]):
    logger.info("get temp - zone %s", zone)
    temp = temperature_data[Zone(zone)]
    return f"The temperature in the {zone} is {temp}C"

@llm.function_tool(description="Set the temperature in a specific room.")
async def set_temperature(
    zone: Annotated[Zone, "The specific zone"],
    temperature: Annotated[int, "The desired temperature in Celsius"]
):
    logger.info("set temp - zone %s to %dC", zone, temperature)
    temperature_data[Zone(zone)] = temperature
    return f"The temperature in the {zone} has been set to {temperature}C"

class AssistantFnc(llm.ToolContext):
    def __init__(self) -> None:
        # Pass the function tools to the ToolContext constructor
        super().__init__([get_temperature, set_temperature])