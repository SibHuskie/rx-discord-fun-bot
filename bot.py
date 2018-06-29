import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS
import urbandictionary as ud

''''''

Client = discord.Client()
bot_prefix= "}"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='414089074870321153')
footer_text = "[Realm X] - [X Fun]"

member_role = '453194601247801354'
bot1_role = '453194562379186176'
bot2_role = '453195460346380288'
owner_role = '453194638077984768'
partner_role = '453194705732239360'
lvl2_role = '453194792457732096'
lvl5_role = '453195170662449152'
lvl10_role = '453195184327491594'
lvl15_role = '453195194607861761'
lvl20_role = '453195205416321034'
lvl25_role = '453195220192854027'
lvl35_role = '453195231517474826'
lvl40_role = '453195258675855361'
lvl50_role = '453195292376825856'
vip_role = '453195303403913227'
legend_role = '453195358575656986'
punished_role = '453195421611982848'
helper_role = '453195469309476877'
mod_role = '453195518785486858'
admin_role = '453195993987416064'
manager_role = '453196026547929088'
hell_role = '453247719067090944'
nsfw_role = '453247786637590570'
partner2_role = '453247829855567872'
lvl0_role = '453653105696047105'
error_img = ':octagonal_sign:'

''''''

suicidemsgs = ["was mentally ill and couldn't keep living with it so they decided to commit suicide!",
               "had anxiety for way too long so they took their own life away!",
               "had a bipolar disorder which made them commit suicide!",
               "was depressed for a few years, not having any hope left, they killed themselves!",
               "had schizophrenia, living with that made them kill themselves!",
               "was physically abused and that experience made them commit suicide!",
               "was sexually abused, later that day they took their own life by jumping off a plane!",
               "lived in war and terror for far too long, today is the day they had enough and commited suicide!",
               "was bullied everyday, in school, outside and on the internet. Not having any friends, they decided to kill themselves, thinking the world would be a better place without them!",
               "had some sort of a personality disorder, which made them commit suicide!",
               "was addicted to drugs. One day they took a few more pills than they were supposed to, later that day they were found dead in their bathroom!",
               "had an eating disorder, thinking that they are not meant to be in this world, they took their own life!",
               "was lonely their whole life, not having anyone to talk to, they decided to leave this world!",
               "had relationship problems, their partner leaving them and telling them to kill themselves made them commit suicide!",
               "felt lonely after their whole family was killed, they decided to join them in the after life by killing themselves!",
               "didn't have any motivation or hope left, so they took their own life away by overdosing!",
               "commited suicide! Too bad there is no one to leave a flower on their grave...",
               "died! Ok, that's it they just died! They totally didn't commit suicide!!",
               "put a rope around their neck and died!",
               "overdosed and died!",
               "tried to commit suicide, but failed! Better luck next time, I guess.",
               "was forced to commit suicide by the dark lord!",
               "killed themselves after losing their diamonds in minecraft!",
               "had no internet connection for over 5 seconds, later that day, they commited suicide!",
               "didn't have a life! They killed themselves!",
               "watched boku no pico, few seconds later they decided to kill themselves!",
               "lost all of their hentai, after not being able to find it, they commited suicide!",
               "saw Zero's face reveal, they commited suicide after that!",
               "got all of their memes stolen, not having any memes left, they decided to kill themselves!",
               "killed themselves!",
               "realised how shitty this server actually is, later that day they commited suicide!"]

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

patlinks = ["https://i.imgur.com/8eApUKG.gif",
            "https://i.imgur.com/qVcP9Pt.gif",
            "https://i.imgur.com/X9hKO2p.gif",
            "https://i.imgur.com/v8cRPH9.gif",
            "https://i.imgur.com/N6C7C30.gif",
            "https://i.imgur.com/M9QPcY6.gif",
            "https://i.imgur.com/oUSdjX6.gif",
            "https://i.imgur.com/mFFr4e0.gif",
            "https://i.imgur.com/3F7kmCd.gif",
            "https://i.imgur.com/7yFvJ6m.gif",
            "https://i.imgur.com/y3La9yP.gif"]

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

nomlinks = ["https://i.imgur.com/E1eQPfu.gif",
            "https://i.imgur.com/UUZY3Rb.gif",
            "https://i.imgur.com/Zd6fIpA.gif",
            "https://i.imgur.com/i2NaBS7.gif",
            "https://i.imgur.com/Up5J6Nn.gif",
            "https://i.imgur.com/J5MLku7.gif",
            "https://i.imgur.com/7yYgZXE.gif"]

throwlinks = ["https://i.imgur.com/o9j2oNi.gif",
              "https://i.imgur.com/wSb8aux.gif",
              "https://i.imgur.com/QO8TrkK.gif",
              "https://i.imgur.com/Ts3Cc52.gif",
              "https://i.imgur.com/D3ggzfW.gif",
              "https://i.imgur.com/eD5mE7R.gif",
              "https://i.imgur.com/JCUipZJ.gif",
              "https://i.imgur.com/VSg0YLw.gif",
              "https://i.imgur.com/8mUufrm.gif"]

bitelinks = ["https://i.imgur.com/E0jIIa9.gif",
             "https://i.imgur.com/Nvkw6hN.gif",
             "https://i.imgur.com/wr7l06j.gif",
             "https://i.imgur.com/uce91VI.gif"]

bloodsucklinks = ["https://i.imgur.com/UbaeYIq.gif",
                  "https://i.imgur.com/qi83Eft.gif",
                  "https://i.imgur.com/CtwmzpG.gif",
                  "https://i.imgur.com/DAuEJ2F.gif",
                  "https://i.imgur.com/By6IGzq.gif"]

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

highfivelinks = ["https://i.imgur.com/hjoQeOt.gif",
                 "https://i.imgur.com/9nhheqT.gif",
                 "https://i.imgur.com/yw3xMOu.gif",
                 "https://i.imgur.com/Y4g5fsT.gif",
                 "https://i.imgur.com/p6Hvx5r.gif",
                 "https://i.imgur.com/33nuO9D.gif",
                 "https://i.imgur.com/uFQnmYa.gif",
                 "https://i.imgur.com/9KG3k2n.gif",
                 "https://i.imgur.com/nHCC1ps.gif",
                 "https://i.imgur.com/aKvaNba.gif",
                 "http://i.imgur.com/hnHR29x.gif"]

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]


punchlinks = ["https://i.imgur.com/T2HdIv8.gif",
              "https://i.imgur.com/LZz65rg.gif",
              "https://i.imgur.com/FqPBIf3.gif",
              "https://i.imgur.com/KmqPDQG.gif",
              "https://i.imgur.com/yEx4aKu.gif"]

starelinks = ["https://i.imgur.com/f8rFNH0.gif",
              "https://i.imgur.com/ACCQDj4.gif",
              "https://i.imgur.com/1Co1i9t.gif",
              "https://i.imgur.com/uPZHQxV.gif",
              "https://i.imgur.com/wXQLAb3.gif",
              "https://i.imgur.com/hY7ZngK.gif"]

facepalmlinks = ["http://media.giphy.com/media/8BYLSNmnJYQxy/giphy.gif",
                 "https://uploads.disquscdn.com/images/84e9a7cef36a59ae605fad98c7ac567841be388820bf3fb936fd21b646a1d605.gif",
                 "https://media1.tenor.com/images/74199573d51d1bd9b61029b611ee7617/tenor.gif?itemid=5695432",
                 "http://i0.kym-cdn.com/photos/images/original/000/173/877/Facepalm.gif",
                 "http://i.imgur.com/gXOcRsW.gif",
                 "https://media.giphy.com/media/8cPpgUhTMjhF6/giphy.gif",
                 "https://media1.tenor.com/images/a0282083ab6b592ab419659e4fb08624/tenor.gif?itemid=4745847"]

crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif"]

suicidelinks = ["https://i.imgur.com/wgOudvL.gif",
                "https://i.imgur.com/rYVvGjd.gif",
                "https://i.imgur.com/rxKk3Mw.gif",
                "https://i.imgur.com/CyuEKD9.gif",
                "https://i.imgur.com/f7xjGP6.gif",
                "https://i.imgur.com/y6wW8zc.gif",
                "https://i.imgur.com/EwzhaIu.gif"]

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

panlinks = ["https://i.imgur.com/DPBafqb.gif",
            "https://i.imgur.com/iXryDZy.gif",
            "https://i.imgur.com/49h6CKN.gif",
            "https://i.imgur.com/EQ4G9Ig.gif",
            "https://i.imgur.com/t8FGb8R.gif",
            "https://i.imgur.com/T8rUe4N.gif",
            "https://i.imgur.com/ABpc6pn.gif",
            "https://i.imgur.com/f9XLuyn.gif"]

''''''

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("============================================================")
    print("X - FUN")
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name="games 24/7."))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")

# FUN MESSAGES
@client.event
async def on_message(msg):
    p = random.randint(0, 10)
    if msg.content == "o/" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "\o")
    elif msg.content == "\o" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "o/")
    elif msg.content == "hello" and msg.author != client.user and p > 4:
        c = ["hi there ( ͡° ͜ʖ ͡°)", "hoi! O/"]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "bye" and msg.author != client.user and p > 4:
        c = ["cyah tonite :>", "noo come back :<"]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "good bot" and msg.author != client.user and p > 4:
        c = ["yesh me gud bottu ʕ•ᴥ•ʔ", "gOoD bOt -.-", "I'm not your dog, bitch.", "meow? <:kat:453199975044874250>"]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "bad bot" and msg.author != client.user and p > 4:
        c = ["D':", "no pls i gud bot ;-;/", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "Shut up. I'm not your fucking dog."]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "i love you" and msg.author != client.user and p > 4:
        c = ["i love me too", "***ok.****", "Error! The user you are trying to message has blocked you.", "just give me the virus link"]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "wroom" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "♪~ ᕕ(ᐛ)ᕗ")
    elif msg.content == "gay" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "˙ ͜ʟ˙")
    elif msg.content == "whalecum" and msg.author != client.user and p > 4:
        c = ["(╯°□°）╯︵ ┻━┻", "stop saying that shit, kthxbai", "fucking weeb", "<:boi:453200003759079424>"]
        await client.send_message(msg.channel, "{}".format(random.choice(c)))
    elif msg.content == "what is love?" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "baby :notes: don't :musical_note:  hurt :notes: me :musical_note: , don't :notes: hurt :musical_note:  me :musical_note: , no :notes: more :musical_note: ")
    elif msg.content == "have you ever had a dream?" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "have you ever had a dream where you you could where you like in and you can in the dream you could you want him so much to do you can do anything?")
    elif msg.content == "ayy" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "ayy lmao")
    elif msg.content == "yas" and msg.author != client.user and p > 4:
        c = ["yas moist fam", "oh fucking hell the cringe", "yasss", "that word is illegal"]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "die" and msg.author != client.user and p > 4:
        c = ["no u", "yes", "wOw Im oFfEndEd", "i would gladly die for my country, Africa."]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "nab" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "lmfao u nab")
    elif msg.content == "zero" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "is gey asf")
    elif msg.content == "black" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "whiten't*")
    elif msg.content == "jimmy" and msg.author != client.user and p > 4:
        c = ["Jimmy stole the fucking soap again!", "That fucking Jimmy! I'll kill that kid.", "jImMy iS sUch A dIcK buT wE aLl FrIEnDs wIth HiM cuZ he Has De SoAp"]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "kat" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "meow")
    elif msg.content == "owo" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "owo what's this?")
    elif msg.content == "im leaving" and msg.author != client.user and p > 4:
        c = ["no dad wait! D;", "no pls ;-;/", "MUM HE LEF", "y tho"]
        await client.send_message(msg.channel, random.choice(c))
    elif msg.content == "<@453210408384462848>" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "<:Ping:453202438783238145>")
    elif msg.content == "fuck u" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "<:fucku:453203813352996864>")
    elif msg.content == "boi" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "<:boi:453200003759079424>")
    elif msg.content == "what?" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "<:wat:453199996716843009>")
    elif msg.content == "want sum fuk?" and msg.author != client.user and p > 4:
        await client.send_message(msg.channel, "<:LennyThink:453199966727569408>")
    else:
        await client.process_commands(msg)
    
''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }ping
@client.command(pass_context=True)
async def ping(ctx, option = None):
    channel = ctx.message.channel
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    if option == None:
        print("")
    elif option == "g":
        print("")
    elif option == "f":
        msg.add_field(name=":satellite: ", value="My ping: `{}ms`.".format(round((t2-t1)*1000)))
        await client.say(embed=msg)
    elif option == "s":
        print("")
    elif option == "all":
        msg.add_field(name=":satellite: ", value="My ping: `{}ms`.".format(round((t2-t1)*1000)))
        await client.say(embed=msg)
    else:
        print("")

# }rainbow
'''
@client.command(pass_context=True)
async def rainbow(ctx):
    color = discord.Color(random.randint(0x000000, 0xFFFFFF))
    msg = discord.Embed(colour=color, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":rainbow: RAINBOWS :rainbow: ", value=":rainbow: R A I N B O W S :rainbow: ")
    channel = ctx.message.channel
    b = await client.send_message(channel, embed=msg)
    g = [":large_blue_circle:", ":red_circle:", ":white_circle:", ":purple_heart:", ":green_heart:", ":yellow_heart:", ":black_circle:"]
    for i in range(20):
        color = discord.Color(random.randint(0x000000, 0xFFFFFF))
        msg2 = discord.Embed(colour=color, description= "")
        msg2.title = ""
        msg2.set_footer(text=footer_text)
        msg2.add_field(name=":rainbow: RAINBOWS :rainbow: ", value=":rainbow: **__R A I N B O W S__** :rainbow: ")
        msg2.set_image(url="https://i.imgur.com/rItq9Ph.gifv")
        await client.edit_message(b, embed=msg2)
        await asyncio.sleep(float(2))
        '''

# }calculator <math problem>
@client.command(pass_context=True)
async def calculator(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please specify a math problem you want me to solve.")
    else:
        try:
            answer = str(eval(args))
            msg.add_field(name=":fax: Calculator", value="<@{}>: what is `{}`?\n \n<@{}>: {}".format(author.id, args, client.user.id, answer))
        except:
            msg.add_field(name=":fax: Calculator", value="<@{}>: I am having trouble solving that problem.".format(client.user.id))
    await client.say(embed=msg)

# }battle <user>
@client.command(pass_context=True)
async def battle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=error_img, value="Please mention someone you want to battle.\nExample: `}battle @Jimmy`.")
    else:
        a_attacks = ["<@{}> punches <@{}> :punch: ".format(author.id, userName.id),
                     "<@{}> kicks <@{}> :boot: ".format(author.id, userName.id),
                     "<@{}> grabs and throws <@{}> :raised_hands: ".format(author.id, userName.id),
                     "<@{}> stabs <@{}> :dagger: ".format(author.id, userName.id),
                     "<@{}> shoots <@{}> :gun: ".format(author.id, userName.id),
                     "<@{}> cuts <@{}> :knife: ".format(author.id, userName.id),
                     "<@{}> hits <@{}> with a hammer :hammer: ".format(author.id, userName.id),
                     "<@{}> uses dark magic on <@{}> :skull_crossbones: ".format(author.id, userName.id),
                     "<@{}> uses chains to choke <@{}> :chains: ".format(author.id, userName.id),
                     "<@{}> casts a spell on <@{}> :sparkles: ".format(author.id, userName.id),
                     "<@{}> pukes on <@{}> :nauseated_face: ".format(author.id, userName.id),
                     "<@{}> scares <@{}> :ghost: ".format(author.id, userName.id),
                     "<@{}> summons a demon to attack <@{}> :smiling_imp: ".format(author.id, userName.id),
                     "<@{}> calls a robot army to attack <@{}> :robot: ".format(author.id, userName.id),
                     "<@{}> farts at <@{}> :dash: ".format(author.id, userName.id),
                     "<@{}> creates a tornado behind <@{}> :cloud_tornado: ".format(author.id, userName.id),
                     "<@{}> summons a meteor and the meteor falls on <@{}> :comet: ".format(author.id, userName.id),
                     "<@{}> strikes <@{}> with lightning :zap: ".format(author.id, userName.id),
                     "<@{}> freezes <@{}> :snowflake: ".format(author.id, userName.id),
                     "<@{}> cripples <@{}> :boom: ".format(author.id, userName.id),
                     "<@{}> shoots <@{}> with a bow and arrow :gun: ".format(author.id, userName.id),
                     "<@{}> drives over <@{}> :red_car: ".format(author.id, userName.id),
                     "<@{}> chops off <@{}>'s leg :crossed_swords: ".format(author.id, userName.id),
                     "<@{}> drains some of <@{}>'s life :broken_heart: ".format(author.id, userName.id),
                     "<@{}> steals <@{}>'s soul :black_heart: ".format(author.id, userName.id),
                     "<@{}> stuns <@{}> :octagonal_sign: ".format(author.id, userName.id),
                     "<@{}> uses nuclear energy to attack <@{}> :radioactive: ".format(author.id, userName.id),
                     "<@{}> stabs <@{}> in the eyes and blinds them :eye: ".format(author.id, userName.id),
                     "<@{}> uses ear-rape to deafen <@{}> :ear: ".format(author.id, userName.id),
                     "<@{}> uses mind control on <@{}> :alien: ".format(author.id, userName.id),
                     "<@{}> summons minions to attack <@{}> :busts_in_silhouette: ".format(author.id, userName.id),
                     "<@{}> traps <@{}> :spider_web: ".format(author.id, userName.id)]
        
        u_attacks = ["<@{}> punches <@{}> :punch: ".format(userName.id, author.id),
                     "<@{}> kicks <@{}> :boot: ".format(userName.id, author.id),
                     "<@{}> grabs and throws <@{}> :raised_hands: ".format(userName.id, author.id),
                     "<@{}> stabs <@{}> :dagger: ".format(userName.id, author.id),
                     "<@{}> shoots <@{}> :gun: ".format(userName.id, author.id),
                     "<@{}> cuts <@{}> :knife: ".format(userName.id, author.id),
                     "<@{}> hits <@{}> with a hammer :hammer: ".format(userName.id, author.id),
                     "<@{}> uses dark magic on <@{}> :skull_crossbones: ".format(userName.id, author.id),
                     "<@{}> uses chains to choke <@{}> :chains: ".format(userName.id, author.id),
                     "<@{}> casts a spell on <@{}> :sparkles: ".format(userName.id, author.id),
                     "<@{}> pukes on <@{}> :nauseated_face: ".format(userName.id, author.id),
                     "<@{}> scares <@{}> :ghost: ".format(userName.id, author.id),
                     "<@{}> summons a demon to attack <@{}> :smiling_imp: ".format(userName.id, author.id),
                     "<@{}> calls a robot army to attack <@{}> :robot: ".format(userName.id, author.id),
                     "<@{}> farts at <@{}> :dash: ".format(userName.id, author.id),
                     "<@{}> creates a tornado behind <@{}> :cloud_tornado: ".format(userName.id, author.id),
                     "<@{}> summons a meteor and the meteor falls on <@{}> :comet: ".format(userName.id, author.id),
                     "<@{}> strikes <@{}> with lightning :zap: ".format(userName.id, author.id),
                     "<@{}> freezes <@{}> :snowflake: ".format(userName.id, author.id),
                     "<@{}> cripples <@{}> :boom: ".format(userName.id, author.id),
                     "<@{}> shoots <@{}> with a bow and arrow :gun: ".format(userName.id, author.id),
                     "<@{}> drives over <@{}> :red_car: ".format(userName.id, author.id),
                     "<@{}> chops off <@{}>'s leg :crossed_swords: ".format(userName.id, author.id),
                     "<@{}> drains some of <@{}>'s life :broken_heart: ".format(userName.id, author.id),
                     "<@{}> steals <@{}>'s soul :black_heart: ".format(userName.id, author.id),
                     "<@{}> stuns <@{}> :octagonal_sign: ".format(userName.id, author.id),
                     "<@{}> uses nuclear energy to attack <@{}> :radioactive: ".format(userName.id, author.id),
                     "<@{}> stabs <@{}> in the eyes and blinds them :eye: ".format(userName.id, author.id),
                     "<@{}> uses ear-rape to deafen <@{}> :ear: ".format(userName.id, author.id),
                     "<@{}> uses mind control on <@{}> :alien: ".format(userName.id, author.id),
                     "<@{}> summons minions to attack <@{}> :busts_in_silhouette: ".format(userName.id, author.id),
                     "<@{}> traps <@{}> :spider_web: ".format(userName.id, author.id)]
        a_health = []
        u_health = []
        r = []
        for i in range(1000):
            a_health.append(".")
            u_health.append(".")
        msg.add_field(name=":crossed_swords: **__D E A T H   B A T T L E__** :crossed_swords: ", value="***`>>>`*** <@{}> :vs: <@{}> ***`<<<`***\n**~~__==============================__~~**".format(author.id, userName.id))
        for i in range(1000):
            if len(a_health) == 0 or len(u_health) == 0:
                if len(a_health) > len(u_health):
                    m = ":crown: WINNER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                    m += "\n "
                    m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                elif len(a_health) < len(u_health):
                    m = ":crown: WINNER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                    m += "\n "
                    m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                else:
                    k = random.randint(0, 100)
                    if k >= 50:
                        m = ":crown: RANDOM WINNER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                        m += "\n "
                        m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                    else:
                        m = ":crown: RANDOM WINNER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                        m += "\n "
                        m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                msg.add_field(name="**~~__==============================__~~**", value=m)
                break
            else:
                r.append(".")
                a_d = random.randint(100, 250)
                u_d = random.randint(100, 250)
                m = ":small_red_triangle_down: {}!\n`{}` DMG!".format(random.choice(a_attacks), a_d)
                m += "\n:small_red_triangle_down: {}!\n`{}` DMG!".format(random.choice(u_attacks), u_d)
                msg.add_field(name=":arrow_right: ROUND `{}`:".format(len(r)), value=m)
                for i in range(a_d):
                    if len(u_health) == 0:
                        break
                    else:
                        u_health.remove(".")
                for i in range(u_d):
                    if len(a_health) == 0:
                        break
                    else:
                        a_health.remove(".")
    await client.say(embed=msg)

# }ship <something> | <something else>
@client.command(pass_context=True)
async def ship(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give 2 things you want to ship.\nExample: `}ship Jimmy | u dad`.")
    else:
        if len(str(args)) > 400:
            msg.add_field(name=error_img, value="The ship cannot be longer than 400 characters.")
        else:
            if "|" in str(args):
                a = args.split('|')
                if len(a) > 2:
                    msg.add_field(name=error_img, value="The command was used incorrectly.\nExample: `}ship you | the toilet`.")
                else:
                    p = random.randint(0, 101)
                    if p >= 0 and p <= 10:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Shit\n```\n:sob: ".format(a[0], a[1], p)
                    elif p >= 11 and p <= 20:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Awful\n```\n:cry: ".format(a[0], a[1], p)
                    elif p >= 21 and p <= 30:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Really Bad\n```\n:frowning2: ".format(a[0], a[1], p)
                    elif p >= 31 and p <= 40:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Bad\n```\n:slight_frown: ".format(a[0], a[1], p)
                    elif p >= 41 and p <= 50:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Okay\n```\n:neutral_face: ".format(a[0], a[1], p)
                    elif p >= 51 and p <= 60:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Good\n```\n:slight_smile: ".format(a[0], a[1], p)
                    elif p >= 61 and p <= 70:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Very Good\n```\n:smiley: ".format(a[0], a[1], p)
                    elif p >= 71 and p <= 80:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Fantastic\n```\n:blush: ".format(a[0], a[1], p)
                    elif p >= 81 and p <= 90:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Amazing\n```\n:heart_eyes: ".format(a[0], a[1], p)
                    else:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Perfect\n```\n:revolving_hearts: ".format(a[0], a[1], p)
                    msg.add_field(name=":heartpulse: **__S H I P   M A C H I N E__** :heartpulse: ", value=m)
            else:
                msg.add_field(name=error_img, value="The command was used incorrectly.\nExample: `}ship Jimmy | u mom`")
    await client.say(embed=msg)

# }rps <rock/paper/scissors>
@client.command(pass_context=True)
async def rps(ctx, o = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if o == None:
        msg.add_field(name=error_img, value="Please choose what you want to use.\nExample: `}rps rock`.")
    else:
        if o == "rock" or o == "paper" or o == "scissors":
            a = ["rock", "paper", "scissors"]
            c = random.choice(a)
            msg.add_field(name=":fist: **__ROCK, PAPER, SCISSORS__** :fist: ", value="**~~__==============================__~~**\n:arrow_forward: <@{}>\n------- `{}`\n:arrow_forward: <@{}>\n------- `{}`".format(author.id, o, client.user.id, c))
            if o == "rock" and c == "scissors":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "paper" and c == "rock":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "scissors" and c == "paper":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "rock" and c == "paper":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            elif o == "paper" and c == "scissors":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            elif o == "scissors" and c == "rock":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            else:
                msg.add_field(name="**~~__==============================__~~**", value=":no_entry: It's a tie!")
        else:
            msg.add_field(name=error_img, value="Invalid choice.\nChoices: `rock`, `paper`, `scissors`.")
    await client.say(embed=msg)

# }kill <user>
@client.command(pass_context=True)
async def kill(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention the user you want to kill.")
    else:
        msgs = ["On a beautiful, sunny day, <@{}> went to the store. As they walked in to the store, they slipped and the doors cut off their head.".format(user.id),
                "<@{}> was sitting on a tree, but because of their weight, the branch broke and they fell right on their head.".format(user.id),
                "On a beautiful morning <@{}> suddenly jumped out of bed and started running towards the bathroom. However, they slipped on a banana and fell out of the window.".format(user.id),
                "<@{}> watched the Emoji movie. The next day they died from too much cringe.".format(user.id),
                "<@{}> was browsing the web one day. They accidentaly clicked on a pop-up saying 'DIE FOR FREE!'.".format(user.id),
                "<@{}> got caught watching hentai. They had no choice but to kill themselves in order to wash away their sins.".format(user.id),
                "All of <@{}>'s memes got stolen! They couldn't live for more than 0.420 seconds without memes.".format(user.id),
                "<@{}> was walking down the village when all of a sudden a piano fell on top of them, crashing all their bones.".format(user.id),
                "Long time ago <@{}> lived in peace and harmony, until the fire nation attacked. Now <@{}> is pretty much dead.".format(user.id, user.id),
                "<@{}> died a virgin. LMAO what a loser.".format(user.id),
                "<@{}> was playing hopscotch on a landmine field. You can tell how that went.".format(user.id),
                "<@{}> was playing the Sims. Their computer crashed and they got a heart attack.".format(user.id),
                "Wait, <@{}> died? Oh well.".format(user.id),
                "<@{}> commited suicide. I guess it's a way of saying 'You can't fire me! I quit!' to God.".format(user.id),
                "<@{}> gave their heart to <@{}>... Literally.".format(user.id, author.id),
                "There hasn't been rain around the whole world, plants are dying and the temperatures are very high. <@{}> was a vegan.".format(user.id),
                "<@{}> decided to go on the moon. However they forgot their space suit. All the kids wanted to hear about the corpse on the moon...".format(user.id),
                "One day <@{}> was chilling with their friends. All of them were bored, they didn't have anything to do. One of them said 'So gentlemen, what do we do now?', <@{}> replied: 'We die.'. Yeah, they were really bored.".format(user.id, user.id),
                "<@{}> tried to lay an egg. Humans can't do that, nor can bots!".format(user.id),
                "All of <@{}>'s diamonds were stolen on their Christian minecraft server. Out of anger they said 'heck' and got killed instantly.".format(user.id),
                "<@{}> forgot how to breathe.".format(user.id),
                "<@{}> saw <@{}>'s face and instantly died.".format(user.id, author.id),
                "...and then <@{}> said: I don't feel so good...".format(user.id),
                "<@{}> livedn't.".format(user.id),
                "<@{}> had a lot of mental disorders and couldn't live with them anymore. They commited suicide by cutting a deep wound on their chest with a kitchen knife.".format(user.id),
                "<@{}> drowned <@{}> in a glass of water.".format(author.id, user.id),
                "<@{}> threw <@{}> in a pool with sharks.".format(author.id, user.id),
                "<@{}> spammed <@{}>'s DMs and they died from all the notifications they got.".format(author.id, user.id),
                "<@{}> stole all of <@{}>'s chocolate. <@{}> simply couldn't live without their chocolate and decided that their life is not worth living anymore.".format(author.id, user.id, user.id),
                "<@{}>'s toaster was hacked by <@{}>. They couldn't live with no toast.".format(user.id, author.id),
                "<@{}> watched furry porn and died from what they saw.".format(user.id),
                "<@{}> 'accidentally' fell off a building.".format(user.id),
                "<@{}> may have ate food with cyanide.".format(user.id),
                "<@{}> saw Zero's face reveal and had no choice but to commit suicide.".format(user.id),
                "<@{}> starved in a fast food restaurant. What a fucking idiot.".format(user.id),
                "...And <@{}> died happily ever after... Wait no, I messed it up!".format(user.id),
                "<@{}> joined this server and died. Oh well, that's not a first.".format(user.id),
                "<@{}> was gay in Iran.".format(user.id),
                "<@{}> choked on a banana ( ͡° ͜ʖ ͡°) and died.".format(user.id),
                "<@{}> drove off a cliff and survived, but died from shock when they saw the high price of the hospital bill.".format(user.id),
                "<@{}> listened to Justin Beiber for more than 0.69 seconds.".format(user.id),
                "<@{}> drank too much anti-freeze.".format(user.id),
                "<@{}> got stabbed with a cucumber by <@{}>.".format(user.id, author.id),
                "<@{}> died from a heatstroke in the artic.".format(user.id),
                "<@{}> tried to fly. It worked till they hit the ground.".format(user.id),
                "<@{}> wanted to get a haircut in a faster way. They thought setting their hair on fire would do the trick.".format(user.id),
                "On a peaceful night. The moon was shining and everyone was sleeping and enjoying their dreams while <@{}> suffocated in their pillow.".format(user.id),
                "<@{}> got run over by a boat. A fricking boat!".format(user.id),
                "What's that smell? It smells like toast... Hey, <@{}>! Don't take out the toast with a fork- too late...".format(user.id),
                "<@{}> got a paper cut on both of their eyes, walked off a cliff and died. I guess books are evil.".format(user.id),
                "<@{}> tried putting out fire with gasoline.".format(user.id),
                "<@{}>'s head exploded while they were sitting on the toilet and pressing.".format(user.id),
                "<@{}> died of laughter. No I mean they actually died.".format(user.id),
                "<@{}> got locked in a refrigerator and died of hunger.".format(user.id),
                "<@{}> drowned in their own tears after losing a game of Fortnite.".format(user.id),
                "<@{}> got beat up by their imaginary friends.".format(user.id),
                "<@{}> played My Little Ponny for too long.".format(user.id),
                "<@{}> choked on air.".format(user.id),
                "<@{}> got poked by Chuck Norris.".format(user.id),
                "<@{}> took a selfie with a gun.".format(user.id),
                "<@{}>'s brain exploded after <@{}> saying 'What if dolphins had legs?'.".format(user.id, author.id),
                "<@{}> died after eating their favourite snack, tide pods.".format(user.id),
                "<@{}> survived the biggest waves then tripped on a rock and died.".format(user.id),
                "<@{}> ate white chocolate. Who the fuck eats white chocolate?".format(user.id),
                "<@{}> demonstrated how to die and then had a heart attack. How ironic.".format(user.id),
                "<@{}> fell in a toilet and then got flushed.".format(user.id),
                "<@{}> got stuck in a vending machine.".format(user.id),
                "<@{}> choked on their toothbrush and died.".format(user.id),
                "<@{}> found their butthole and died from excitement.".format(user.id),
                "<@{}> died. That's it. They just died.".format(user.id)]
        msg.add_field(name=":newspaper2: ", value="{}".format(random.choice(msgs)))
    await client.say(embed=msg)

# }nothing
@client.command(pass_context=True)
async def nothing(ctx):
    await client.say("` `")

# }eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please ask a yes/no question.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The question cannot be longer than 1900 characters.")
        else:
            a = ["Hell no!",
                 "No!",
                 "Hell yes!",
                 "Yes!",
                 "Definitely!",
                 "Definitely not!",
                 "Probably!",
                 "Probably not!",
                 "Most likely!",
                 "Yes! I'm sure of it!",
                 "No! I'm sure of it!"]
            msg.add_field(name=":8ball: ", value=":grey_question: `Question:`\n<@{}>: {}\n \n:grey_exclamation: `Answer:`\n**Magic Eight Ball**: {}".format(author.id, args, random.choice(a)))
    await client.say(embed=msg)

# }roast <user>
@client.command(pass_context=True)
async def roast(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention a user you want to roast.")
    else:
        a = ["<@{}>: Hey, <@{}>! I saw a piece of shit today... it reminded me of you.".format(author.id, user.id),
             "<@{}>: You look familiar, <@{}>. Oh yeah! I see you in the trash.".format(author.id, user.id),
             "<@{}>: Don't worry, <@{}>, you're not adopted. We're still searching for someone who wants you.".format(author.id, user.id),
             "<@{}>: If I wanted to kill myself, I'd jump climb up your ego and jump in your IQ, <@{}>.".format(author.id, user.id),
             "<@{}>: <@{}>, you are so stupid that you got hit by a parked car.".format(author.id, user.id),
             "<@{}>: <@{}>, you are so fat and so old that when God created light, you were asked to move out of the way.".format(author.id, user.id),
             "<@{}>: I heard <@{}> sucks so much that they were used as a vacuum cleaner.".format(author.id, user.id),
             "<@{}>: Hey, <@{}>! Try to not spit when you talk, we don't need a public shower here.".format(author.id, user.id),
             "<@{}>: I'm going to be honest... <@{}>, you remind me of Zero, eew.".format(author.id, user.id),
             "<@{}>: I can't breathe when I see you, <@{}>... cause I'm suffocating from your bullshit.".format(author.id, user.id),
             "<@{}>: <@{}>, you have the right to remain silent cause anything you say is probably going to be stupid anyway.".format(author.id, user.id),
             "<@{}>: It's really hard to ignore <@{}>. Mostly cause they smell like shit.".format(author.id, user.id),
             "<@{}>: <@{}>, did you fall from Heaven? Cause so did Satan.".format(author.id, user.id),
             "<@{}>: <@{}>, were you sent to kill people? Cause your face is killing me.".format(author.id, user.id),
             "<@{}>: If laughter is the best medicine, your face must be curing the world, <@{}>.".format(author.id, user.id),
             "<@{}>: The only way you'll ever get laid is if you crawl up a chicken's ass and wait, <@{}>.".format(author.id, user.id),
             "<@{}>: <@{}>, your family tree must be a cactus. Cause everyone on it is a prick.".format(author.id, user.id),
             "<@{}>: <@{}>, save your breath, you'll need it to blow your date.".format(author.id, user.id),
             "<@{}>: <@{}>, the zoo called. They are wondering how you got out of your cage?".format(author.id, user.id),
             "<@{}>: <@{}>, you're so ugly that when you look in the mirror your reflection looks the away.".format(author.id, user.id),
             "<@{}>: <@{}>, it's better to let someone think you're stupid than open your mouth and prove it.".format(author.id, user.id),
             "<@{}>: I just stepped in something that is smarter than you, <@{}>... It smelled better too.".format(author.id, user.id),
             "<@{}>: <@{}>, you're stupid just like your father when he thought he didn't need a condom.".format(author.id, user.id),
             "<@{}>: <@{}> is so stupid that they stopped at a stop sign and waited for it to say go.".format(author.id, user.id),
             "<@{}>: <@{}>, you're so ugly that you have to trick or treat over the phone.".format(author.id, user.id),
             "<@{}>: <@{}>, you're so fat that your school photo was a double picture.".format(author.id, user.id),
             "<@{}>: I'd like to kick <@{}> in the teeth but that would be an improvement for them.".format(author.id, user.id),
             "<@{}>: <@{}> is so old that when they were in school there was no history class.".format(author.id, user.id),
             "<@{}>: <@{}> is so stupid that they called me to ask me for my phone number.".format(author.id, user.id),
             "<@{}>: <@{}>, at least my mom pretends to love me.".format(author.id, user.id),
             "<@{}>: <@{}>, don't play hard to get when you are hard to want.".format(author.id, user.id),
             "<@{}>: <@{}>, you're hating yourself too much for me to roast you.".format(author.id, user.id),
             "<@{}>: <@{}>, I can't even call you ugly. Nature has beaten me to it.".format(author.id, user.id),
             "<@{}>: People like you, <@{}>, are the reason God doens't talk to us anymore.".format(author.id, user.id),
             "<@{}>: We all dislike you, <@{}>. But not quite enough to think about you.".format(author.id, user.id),
             "<@{}>: <@{}>, you are a stupid.".format(author.id, user.id),
             "<@{}>: <@{}>, I'd like to invite you to a nice, warming cup of shut the fuck up.".format(author.id, user.id),
             "<@{}>: <@{}>, your mother might have told you, you can be whatever you want to but a cunt wasn't what she meant.".format(author.id, user.id),
             "<@{}>: <@{}> is so fat, Thanos had to clap.".format(author.id, user.id)]
        msg.add_field(name=":fire: Roast Machine", value="{}".format(random.choice(a)))
    await client.say(embed=msg)

# }leave
@client.command(pass_context=True)
async def leave(ctx):
    author = ctx.message.author
    a = ["**{}** left the server!".format(author.name),
         "**{}** left the game!".format(author.name),
         "**{}** left your party!".format(author.name),
         "**{}** left!".format(author.name),
         "**{}** died!".format(author.name),
         "**{}** has been killed!".format(author.name)]
    await client.say(random.choice(a))
    await client.delete_message(ctx.message)

# }suicide
@client.command(pass_context=True)
async def suicide(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(suicidelinks)))
    msg.add_field(name=":newspaper2: ", value="<@{}> {}".format(author.id, random.choice(suicidemsgs)))
    await client.say(embed=msg)

# }rate <text>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Nothing to rate given.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The text cannot be longer than 1900 characters.")
        else:
            msg.add_field(name=":scales:", value=":arrow_forward: <@{}>\nI'd rate {} a {}/10!".format(author.id, args, random.randint(0, 11)))
    await client.say(embed=msg)

# }dicklength
@client.command(pass_context=True)
async def dicklength(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    choice = random.randint(0, 10)
    if choice == 0 or choice == 1:
        c = random.randint(0, 1)
        if c == 1:
            msg.add_field(name=":straight_ruler: ", value="I'm sorry, <@{}>, your dick ran away.".format(author.id))
        else:
            msg.add_field(name=":straight_ruler: ", value="I'm sorry, <@{}>, your dick fell off.".format(author.id))
    elif choice == 9 or choice == 10:
        msg.add_field(name=":straight_ruler: ", value="Currently <@{}>'s dick is too big for me to take the length of it.".format(author.id))
    else:
        msg.add_field(name=":straight_ruler: ", value="Currently, <@{}>'s dick is {}cm long.".format(author.id, random.randint(1, 101)))
    await client.say(embed=msg)

# }urban <text>
@client.command(pass_context=True)
async def urban(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give something you want to define.")
    else:
        if len(str(args)) > 150:
            msg.add_field(name=error_img, value="The text cannot be longer than 150 characters.")
        else:
            try:
                defs = ud.define('{}'.format(args))
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \n{}".format(author.id, args, random.choice(defs)))
            except:
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \nNo definition found.".format(author.id))
    await client.say(embed=msg)

# }chocolate
@client.command(pass_context=True)
async def chocolate(ctx):
    await client.say(":chocolate_bar: *yum* ^~^")

# }howgay <user>
@client.command(pass_context=True)
async def howgay(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please tag someone.")
    else:
        p = random.randint(0, 101)
        c = random.randint(0, 10)
        if c > 4:
            msg.add_field(name=":thinking: :gay_pride_flag: ", value="<@{}>: How gay is <@{}>?\n \n<@{}>: <@{}> is {}% gay.".format(author.id, user.id, client.user.id, user.id, p))
        elif c == 1 or c == 0:
            msg.add_field(name=":thinking: :gay_pride_flag: ", value="<@{}>: How gay is <@{}>?\n \n<@{}>: <@{}> is hella fucking gay.".format(author.id, user.id, client.user.id, user.id))
        else:
            msg.add_field(name=":thinking: :gay_pride_flag: ", value="<@{}>: How gay is <@{}>?\n \n<@{}>: <@{}> is not gay at all.".format(author.id, user.id, client.user.id, user.id))
    await client.say(embed=msg)

''' COMMANDS FOR VIPS '''
# }hug <user>
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to hug.")
        else:
            msg.set_image(url="{}".format(random.choice(huglinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got a hug from <@{}>! How cute.".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to kiss.")
        else:
            msg.set_image(url="{}".format(random.choice(kisslinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got a kiss from <@{}>! owo what's this?".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to cuddle.")
        else:
            msg.set_image(url="{}".format(random.choice(cuddlelinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> cuddled <@{}>! Aww.".format(author.id, user.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }bite <user>
@client.command(pass_context=True)
async def bite(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to bite.")
        else:
            msg.set_image(url="{}".format(random.choice(bitelinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got biten by <@{}>! Ouch.".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }bloodsuck <user>
@client.command(pass_context=True)
async def bloodsuck(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to suck blood from.")
        else:
            msg.set_image(url="{}".format(random.choice(bloodsucklinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> sucked some of <@{}>'s blood! Yummy.".format(author.id, user.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }throw <user>
@client.command(pass_context=True)
async def throw(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to throw.")
        else:
            msg.set_image(url="{}".format(random.choice(throwlinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got throw by <@{}>! Weee.".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }pat <user>
@client.command(pass_context=True)
async def pat(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to pat.")
        else:
            msg.set_image(url="{}".format(random.choice(patlinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got a pat from <@{}>! uwu".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }punch <user>
@client.command(pass_context=True)
async def punch(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to punch.")
        else:
            msg.set_image(url="{}".format(random.choice(punchlinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got punched by <@{}>! Wow, calm down.".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }nom <user>
@client.command(pass_context=True)
async def nom(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to nom.")
        else:
            msg.set_image(url="{}".format(random.choice(nomlinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> nommed <@{}>! ( ͡° ͜ʖ ͡°)".format(author.id, user.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }highfive <user>
@client.command(pass_context=True)
async def highfive(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to highfive.")
        else:
            msg.set_image(url="{}".format(random.choice(highfivelinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> highfived <@{}>! Woo.".format(author.id, user.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }poke <user>
@client.command(pass_context=True)
async def poke(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to poke.")
        else:
            msg.set_image(url="{}".format(random.choice(pokelinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got poked by <@{}>! Hmm?".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }slap <user>
@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to slap.")
        else:
            msg.set_image(url="{}".format(random.choice(slaplinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got slapped by <@{}>! They probably deserved it.".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }stare <user>
@client.command(pass_context=True)
async def stare(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to stare at.")
        else:
            msg.set_image(url="{}".format(random.choice(starelinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> is staring at <@{}>! Creep.".format(author.id, user.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }facepalm
@client.command(pass_context=True)
async def facepalm(ctx):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        msg.set_image(url="{}".format(random.choice(facepalmlinks)))
        msg.add_field(name=":handshake: Interactions", value="<@{}> facepalmed. <_<".format(author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }spank <user>
@client.command(pass_context=True)
async def spank(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to spank.")
        else:
            msg.set_image(url="{}".format(random.choice(spanklinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> got spanked by <@{}>! =3".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

# }lick <user>
@client.command(pass_context=True)
async def lick(ctx, user: discord.Member = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to lick.")
        else:
            msg.set_image(url="{}".format(random.choice(licklinks)))
            msg.add_field(name=":handshake: Interactions", value="<@{}> licked <@{}>! I'm not sure what to think of this, you weirdos.".format(author.id, user.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends.")
    await client.say(embed=msg)

''' COMMANDS FOR OWNERS '''
@client.command(pass_context=True)
async def pan(ctx, user: discord.Member = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    msg = discord.Embed(colour=0x00FFFF, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to pan. Be careful, though, this is one of the most powerful commands ever created.")
        else:
            msg.set_image(url="{}".format(random.choice(panlinks)))
            msg.add_field(name="<:pan:453199967541264386>", value="<@{}> just got panned by <@{}>. Holy shit.".format(user.id, author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by Owners. No one else is capable to handle its power.")
    await client.say(embed=msg)
    
#######################
client.run(os.environ['BOT_TOKEN'])
