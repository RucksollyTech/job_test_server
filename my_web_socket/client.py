import asyncio
import json
import websockets

URI = "ws://localhost:8765"


async def call_compute_sum_numbers(a: float, b: float) -> float:
    """
    Call the server-side compute_sum_numbers function via WebSocket.

    Returns:
        result of a + b
    """
    async with websockets.connect(URI) as ws:
        await ws.send(json.dumps({
            "method": "compute_sum_numbers",
            "params": {"a": a, "b": b},
        }))

        response = await ws.recv()
        data = json.loads(response)

        if "error" in data:
            raise RuntimeError(data["error"])

        return data["result"]


async def demo():
    tests = [(1, 2), (10, 20), (-5, 15), (3.5, 4.5)]
    for a, b in tests:
        result = await call_compute_sum_numbers(a, b)
        print(f"compute_sum_numbers({a}, {b}) = {result}")


if __name__ == "__main__":
    asyncio.run(demo())



