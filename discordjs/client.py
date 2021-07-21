import inspect

from typing import Callable
from discord import Client as dpyClient

class BadEvent(Exception):
    """Raised if provided event type is not supported."""
    pass

class Client:
    """Base bot class"""
    
    def __init__(self):
        self.bot = dpyClient()

    def on(self, event_name: str, callback: Callable):
        if event_name == "ready":

            async def on_ready():
                callback()

            self.bot.event(on_ready)

        elif event_name == "message":

            async def on_message(message):
                if inspect.iscoroutinefunction(callback):
                    await callback(message)
                else:
                    callback(message)

            self.bot.event(on_message)
        else:
            raise BadEvent(
                "Unknown event type. Only 'ready' and 'message' events are supported for now."
            )

    def login(self, token):
        self.bot.run(token) 
