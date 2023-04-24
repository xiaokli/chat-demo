import asyncio
from websockets.server import serve
from json import decoder
from chat import Chat

class Server:

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.decoder = decoder.JSONDecoder()

    async def handle(self, websocket):
        async for message in websocket:
            chat = Chat.getOrCreate(websocket)
            await chat.handle(message)
            
    async def run(self):
        async with serve(self.handle, self.host, self.port):
            await asyncio.Future()


server = Server("localhost", 8765)
asyncio.run(server.run())
print("started ")