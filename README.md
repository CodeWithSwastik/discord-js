# discord.js

This module lets you use discord.js in python by offering a similar syntax to the actual discord.js.

## Installation

Stable version:

```
pip install discord.js
```

Working version:

```
pip install git+https://github.com/CodeWithSwastik/discord-js
```

## Simple bot

```python
from discordjs import Client
from javascript import console

client = Client()

client.on("ready", lambda:
    console.log("Bot is ready")
)

async def msg(message):
    if message.content.startswith("!ping"):
        await message.channel.send("pong")

client.on("message", msg)

client.login('Token')
```
