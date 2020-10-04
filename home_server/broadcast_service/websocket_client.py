import asyncio
import websockets

HOST = "192.168.0.13"
PORT = "1234"


async def client(text):
    url = "ws://" + HOST + ":" + PORT

    async with websockets.connect(url) as client_socket:
        await client_socket.send(text)


def send_to_broadcast_server(text):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        asyncio.get_event_loop().run_until_complete(client(text))
    except ConnectionRefusedError:
        pass
