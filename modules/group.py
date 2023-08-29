from pyrogram import Client, filters
from telegraph import upload_file

app = Client("my_bot", api_id=27376757, api_hash="27d4e363b3524401b62e86f1cc16c096", bot_token="6038826331:AAEbTWf0thTYGF2yZFEG6mJuzkdLW8YS5_M")

@app.on_message(filters.document)
async def document_handler(client, message):
    if message.document:
        print("Received a document")
        input_file = message.document.file_id
        fpath = await app.download_media(input_file, file_name="downloaded_file")
        print(f"File downloaded at: {fpath}")
        telegraph_url = await upload_to_telegraph(fpath)
        await message.reply_text(f"Uploaded to Telegraph. Link: {telegraph_url}")

async def upload_to_telegraph(file_path):
    response = await upload_file(file_path)
    return response["src"]

app.run()
