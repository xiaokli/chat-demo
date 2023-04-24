import asyncio
from websockets.sync.client import connect

class Client:

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    
    def run(self):
        connectStr = f'ws://{self.host}:{self.port}'
        with connect(connectStr) as websocket:
             websocket.send("Hello world!")
             message = websocket.recv()
             print(f"Received: {message}")
             message = websocket.recv()
             print(f"Received: {message}")
           


client = Client("localhost", 8765)

client.run()