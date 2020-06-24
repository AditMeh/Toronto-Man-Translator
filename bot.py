import os
import pickle
import discord
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
print(load_dotenv())

ACTIVATION_COMMAND = os.getenv('ACTIVATION_COMMAND') + " "

print(os.getenv('DISCORD_TOKEN'))
client = discord.Client()

pickle_in = open("dictionary/dict.pickle", "rb")
dictionary = pickle.load(pickle_in)

pickle_in = open("dictionary/filter.pickle", "rb")
filter_words = pickle.load(pickle_in)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    query = message.content
    filter_state = False
    if query[0:len(ACTIVATION_COMMAND)] == ACTIVATION_COMMAND:
        query = query[len(ACTIVATION_COMMAND):]
        for i in dictionary.keys():
            if query.find(i) >= 0:
                query = query.replace(i, dictionary[i])
        query = query.split(" ")
        for i in range(len(query)):
            if query[i] in filter_words:
                filter_state = True
                break
            elif query[i] in dictionary:
                query[i] = dictionary[query[i]]
        response = " ".join(query)
        if not filter_state:
            await message.channel.send("Toronto Man -> English: " + response)
        else:
            await message.channel.send("BLACK LIVES MATTER: https://tenor.com/view/black-lives-blackpeople-blacklivesmatter-gif-8493330")

keep_alive()

TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)

