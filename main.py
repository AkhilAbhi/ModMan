from pyrogram import Client, filters
from modules import chek
# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual values
app = Client("my_bot", api_id=27376757, api_hash="27d4e363b3524401b62e86f1cc16c096", bot_token="6038826331:AAEbTWf0thTYGF2yZFEG6mJuzkdLW8YS5_M")

@app.on_message(filters.command("start"))
async def start(client, message):
    name = message.chat.first_name
    await message.reply_text(f"Hay {name} \nI am Mod Man \nYou can get all mod app and games free \nNo virus \nNo malwers \nNo Trojens \nSafe and Secure ❤")
    await message.reply_text("to join aver group\n👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇\nhttps://t.me/+WPt3ypAJM9AxNTY1")

#help message 

@app.on_message(filters.command("help"))
async def help(client,message):
    name = message.chat.first_name
    ss = f"""hay {name}
❤❤❤❤❤❤❤❤❤❤❤❤❤❤

COMMANDS

/help > get all commands and all details



#############################


HOW TO SEARCH APP OR GAME

To Search mod apps > app THE NAME OF THE APP YOU NEED

To Search mod games > game THE NAME OF THE GAME YOU NEED

To Search both > all The name of the app or game you need

#############################
    """
    
    await message.reply(ss)

@app.on_message()
async def handiling(client,message):
    await chek.chekall(client,message)


print("###########################\n runnig bot")
app.run()
