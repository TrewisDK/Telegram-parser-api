from fastapi import FastAPI
from fastapi.responses import FileResponse
import api_manifest
from pyrogram import Client

app = FastAPI()


@app.get("/")
async def api():
    return {"message": "Hello in simple fastapi API"}


@app.get("/api")
async def api_methods():
    return {"message": f"API methods: {api_manifest.methods}"}


@app.get("/api/version")
async def api_version():
    return {"message": f"API version: {api_manifest.version}"}


@app.get("/api/parse_members_{chat}")
async def api_start_wor(chat: str):
    async with Client("my_account", api_manifest.api_id, api_manifest.api_hash) as app:
            await app.join_chat(chat)
            async for member in app.get_chat_members(chat):
                member_is = member.user.username
                print(member_is)
                try:
                    with open(f"{chat}_members.txt", "a+") as f:
                        f.write("@" + member_is + "\n")
                except Exception:
                    continue

    return FileResponse(path=f"{chat}_members.txt", media_type="application/octet-stream", filename="result.txt")






