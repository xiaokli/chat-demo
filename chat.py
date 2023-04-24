from model import run, index
class Chat:
    CHATS = {}

    def __init__(self, websocket) -> None:
        self.websocket = websocket
        self.ask = 0
    
    async def handle(self, message):
        self.ask += 1
        
        queryResult = index.query(message)
        queryResult2 = index.query_with_sources(message)
        aiResult = run(message)
        await self.websocket.send(f"queryResult: {queryResult}")
        await self.websocket.send(f"queryResult2: {queryResult2}")
        await self.websocket.send(f"aiResult: {aiResult}")

    @classmethod
    def getOrCreate(cls, websocket):
        if websocket in cls.CHATS.keys():
            return cls.CHATS[websocket]
        else:
            chat = Chat(websocket)
            cls.CHATS[websocket] = chat
            return chat