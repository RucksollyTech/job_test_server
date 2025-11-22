import asyncio
import json
from websockets.server import serve

async def compute_sum_numbers(a: float, b: float) -> float:
    return a + b



async def handle_connection(websocket):
    """
    This is for handling incoming WebSocket connections.

    Expected request (JSON):
        {
            "method": "compute_sum_numbers",
            "params": {"a": 10, "b": 20}
        }

    Response needed for eample:
        {"result": 30}
    """
    async for message in websocket:
        try:
            data = json.loads(message)

            if data.get("method") != "compute_sum_numbers":
                await websocket.send(json.dumps({"error": "Unknown method"}))
                continue

            params = data.get("params", {})
            a = params.get("a")
            b = params.get("b")

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                await websocket.send(json.dumps({"error": "Invalid parameters"}))
                continue

            result = await compute_sum_numbers(a, b)
            await websocket.send(json.dumps({"result": result}))

        except Exception as exc:
            await websocket.send(json.dumps({"error": str(exc)}))


async def main():
    print("WebSocket server is running on ws://localhost:8765")
    async with serve(handle_connection, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
