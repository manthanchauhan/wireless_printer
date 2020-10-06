import asyncio
import websockets
import json

HOST = "192.168.0.13"
PORT = "1234"
SERVER_KEY = "hy^3se%^GbuIoHEd"  # TODO move to env


async def client(text):
    url = "ws://" + HOST + ":" + PORT

    async with websockets.connect(url) as client_socket:
        auth_success = await auth_with_broadcast_server(client_socket)

        if not auth_success:
            return False

        text_data = {
            "text": text,
        }

        await client_socket.send(json.dumps(text_data))


def send_to_broadcast_server(text):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        asyncio.get_event_loop().run_until_complete(client(text))
    except ConnectionRefusedError:
        pass


async def auth_with_broadcast_server(client_socket):
    auth_data = {
        "type": "server",
        "password": SERVER_KEY,
    }

    data = json.dumps(auth_data)
    await client_socket.send(data)

    message = await client_socket.recv()

    return json.loads(message)["success"]
