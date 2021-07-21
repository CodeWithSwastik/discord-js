from discord import Client as dpyClient
import inspect


class Client:
    def __init__(self):
        self.bot = dpyClient()

    def on(self, event_name, callback):
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
            raise Exception(
                "Unknown event type. Only 'ready' and 'message' events are supported for now!"
            )

    def login(self, token):
        self.bot.run(token)
