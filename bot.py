import os
import pickle
import discord
from dotenv import load_dotenv

load_dotenv()
print(load_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')

ACTIVATION_COMMAND = os.getenv('ACTIVATION_COMMAND') + " "

print(os.getenv('DISCORD_TOKEN'))
client = discord.Client()

pickle_in = open("dictionary/dict.pickle", "rb")
dictionary = pickle.load(pickle_in)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    query = message.content
    if query[0:len(ACTIVATION_COMMAND)] == ACTIVATION_COMMAND:
        query = query[len(ACTIVATION_COMMAND):]
        for i in dictionary.keys():
            if query.find(i) >= 0:
                query = query.replace(i, dictionary[i])
        query = query.split(" ")
        for i in range(len(query)):
            if query[i] in dictionary:
                query[i] = dictionary[query[i]]
        response = " ".join(query)
        await message.channel.send("Toronto Man -> English: " + response)


client.run(TOKEN)

git remote add origin https://github.com/AditMeh/Toronto-Man-Translator.git