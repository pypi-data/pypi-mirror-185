# twitch-thumbnail

Download Twitch channel thumbnail

## Install

```bash
pip install twitch-thumbnail
```

**Require FFMPEG**

## Usage

### synchronous

```py
from twitch_thumbnail import download_thumbnail

download_thumbnail("woowakgood", "thumbnail.png")
```

### asynchronous

```py
import asyncio
from twitch_thumbnail.asynchronous import download_thumbnail

async def main():
    await download_thumbnail("woowakgood", "thumbnail.png")

asyncio.run(main())
```
