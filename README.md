# discord.js

This module let's you use discord.js in python by offering a similar syntax to the actual discord.js.

# Simple bot

```python
from discordjs import Client, console

client = Client()

client.on("ready", lambda:
    console.log("Bot is ready")
)

async def msg(message):
    if message.startswith("!ping"):
        await message.channel.send("pong")

client.on("message", msg)

client.login('Token')
```
