from pyrogram import Client, filters
from . import group

async def chekall(client,message):
    name = str(message.chat.type)
    if(name == "ChatType.PRIVATE"):
        print('private chat')
    elif(name == "ChatType.GROUP"):
        # print("group chat")
        pass
        #await group.getMessage(client,message)
    elif(name == "ChatType.CHANNEL"):
        print("chanel chat")
    else:
        print('somthin went worng')
