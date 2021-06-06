import discord
import time
import asyncio

messages = joined = 0
dic = {'Pompompurin#8317': 1}

client = discord.Client()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open('stats.txt', 'a') as f:
                f.write(f'Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n')

            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_member_join(message):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == 'general':
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(523854018771157013)
    channels = ['member', 'general', 'bot-test']
    bad_words = ['fuck', 'shit', 'bitch', 'cunt']

    for word in bad_words:
        if message.content.count(word) > 0:
            print('A bad word was said')
            await message.channel.purge(limit=1)
            await message.channel.send('Watch your mouth!')

    if message.content == '~help':
        embed = discord.Embed(title='Help on BOT', description='Some useful commands')
        embed.add_field(name='~hello', value='Greets the user')
        embed.add_field(name='~users', value='Shows number of users')
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels:
        if message.content.find('~hello') != -1:
            await message.channel.send('Hi')
        elif message.content == "~users":
            await message.channel.send(f"""# of Members: {id.member_count}""")


client.loop.create_task(update_stats())

client.run("ODUwODU4MDAyNDQ5ODI1Nzky.YLv1Qw.J2R1nBChpg3KjBwLHKUofS8W7Q0")
