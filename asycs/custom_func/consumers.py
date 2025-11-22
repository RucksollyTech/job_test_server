import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .common import compute_sum_numbers

# This handles our websockets with channels
class PerformActionAsync(AsyncWebsocketConsumer):
    async def connect(self):
        print("got here")
        await self.accept()  # Accept connection

    # receives our data fron the client side 
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)

            method = data.get("method")
            params = data.get("params", {})
            
            if method != "compute_sum_numbers":
                await self.send(json.dumps({"error": "Unknown method"}))
                return

            a = params.get("a")
            b = params.get("b")

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                await self.send(json.dumps({"error": "Invalid parameters"}))
                return

            result = compute_sum_numbers(a, b)
            await self.send(json.dumps({"result": result}))

        except Exception as exc:
            await self.send(json.dumps({"error": str(exc)}))
