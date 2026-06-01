import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        print(f"Received sync signal: {message}")
        await websocket.send(f"ACK: {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    print("WebSocket Server initialized. Listening on port 8765...")
