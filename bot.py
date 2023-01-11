import discord
import responses
import config
from discord.ui import Button, View


# Create Message View
class SearchView(View):
    def __init__(self, message, response):
        super().__init__(timeout=60)
        self.message = message
        self.response = response
        self.end = False
        self.current = 0
    
    @discord.ui.button(label='<<-', custom_id='skip_start', disabled= True)
    async def skip_start_callback(self, interaction, skip_start_btn):
        prev_btn = [i for i in self.children if i.custom_id == 'prev'][0]
        next_btn = [i for i in self.children if i.custom_id == 'next'][0]
        skip_start_btn = [i for i in self.children if i.custom_id == 'skip_start'][0]
        skip_end_btn = [i for i in self.children if i.custom_id == 'skip_end'][0]

        self.current = 0

        if(self.current < len(self.response)-1):
            next_btn.disabled = False
            skip_end_btn.disabled = False

        skip_start_btn.disabled = True
        prev_btn.disabled = True

        await interaction.response.edit_message(content= self.response[self.current], view=self)

    @discord.ui.button(label='<-', custom_id='prev', disabled= True)
    async def prev_callback(self, interaction, prev_btn):
        prev_btn = [i for i in self.children if i.custom_id == 'prev'][0]
        next_btn = [i for i in self.children if i.custom_id == 'next'][0]
        skip_start_btn = [i for i in self.children if i.custom_id == 'skip_start'][0]
        skip_end_btn = [i for i in self.children if i.custom_id == 'skip_end'][0]

        if(self.current > 0):
            self.current -= 1
        
        if(self.current == 0):
            prev_btn.disabled = True
            skip_start_btn.disabled = True

        if(self.current < len(self.response)-1):
            next_btn.disabled = False
            skip_end_btn.disabled = False

        
        await interaction.response.edit_message(content= self.response[self.current], view=self)

    @discord.ui.button(label='->', custom_id='next')
    async def next_callback(self, interaction, next_btn):
        prev_btn = [i for i in self.children if i.custom_id == 'prev'][0]
        next_btn = [i for i in self.children if i.custom_id == 'next'][0]
        skip_start_btn = [i for i in self.children if i.custom_id == 'skip_start'][0]
        skip_end_btn = [i for i in self.children if i.custom_id == 'skip_end'][0]
        
        if(self.current < len(self.response)-1):
            self.current += 1
        
        if(self.current == len(self.response)-1):
            next_btn.disabled = True
            skip_end_btn.disabled = True

        if(self.current > 0):
            prev_btn.disabled = False
            skip_start_btn.disabled = False

        await interaction.response.edit_message(content= self.response[self.current], view=self)

    @discord.ui.button(label='->>', custom_id='skip_end')
    async def skip_end_callback(self, interaction, skip_end_btn):
        prev_btn = [i for i in self.children if i.custom_id == 'prev'][0]
        next_btn = [i for i in self.children if i.custom_id == 'next'][0]
        skip_start_btn = [i for i in self.children if i.custom_id == 'skip_start'][0]
        skip_end_btn = [i for i in self.children if i.custom_id == 'skip_end'][0]

        self.current = len(self.response) - 1

        if(self.current > 0):
            prev_btn.disabled = False
            skip_start_btn.disabled = False

        next_btn.disabled = True
        skip_end_btn.disabled = True

        await interaction.response.edit_message(content= self.response[self.current], view=self)

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.message.author:
            await interaction.response.send_message('You cant use that', ephemeral=True)
            return False
        return True

class HelpView(View):
    def __init__(self, message):
        super().__init__(timeout=60)
        self.message = message

    @discord.ui.button(label='Search', custom_id='search')
    async def search_btn_callback(self, interaction, search_btn):
        content = '```\nj!player {playername} -> search for a player\nj!p {playername} -> shorthand for player\nj!nation {nation} -> get a list of all players of the nation\nj!n {nation} -> shorthand for nation\nj!club {club} -> get a list of all players of the club\nj!c {club} -> shorthand for club\nj!league {league} -> get a list of all players of the league\nj!l {leauge} -> shorthand for league\nj!position {position} -> get a list of all players playing in the position\nj!pos {position} -> shorthand for position```'
        await interaction.response.edit_message(content=content, view=self)

    @discord.ui.button(label='Misc', custom_id='misc')
    async def misc_btn_callback(self, interaction, misc_btn):
        content = '```\nj!hello -> greet the bot :) it can get lonely sometimes\nj!roll -> get a random number between 1 and 100\nj!ping -> get the latency```'
        await interaction.response.edit_message(content=content, view=self)

    @discord.ui.button(label='Anime', custom_id='anime')
    async def anime_btn_callback(self, interaction, anime_btn):
        content = '```\nj!anime {animename} -> search real time information about an anime (source: livechart.me)```'
        await interaction.response.edit_message(content=content, view=self)

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.message.author:
            await interaction.response.send_message('You cant use that', ephemeral=True)
            return False
        return True

class AnimeView(View):
    def __init__(self, message, response):
        super().__init__(timeout=60)
        self.message = message
        self.response = response
    
    @discord.ui.button(label='1', custom_id='first')
    async def first_btn_callback(self, interaction, first_btn):
        content = '```\n' + f"Name: {self.response[0]['name']}\n\nDescription:\n{self.response[0]['description']}\n\nGenre:{self.response[0]['genre']}\nStudio:{self.response[0]['studio']}\nOriginal Title:{self.response[0]['original_title']}\nStatus:{self.response[0]['status']}\nPremiere:{self.response[0]['premiere']}\nSeason:{self.response[0]['season']}\nTotal Episodes:{self.response[0]['episodes']}\nNext Episode:{self.response[0]['new_ep']}" + '\n```'
        await interaction.response.edit_message(content=content, view=self)

    
    @discord.ui.button(label='2', custom_id='second')
    async def second_btn_callback(self, interaction, second_btn):
        if(len(self.response) > 1):
            content = '```\n' + f"Name: {self.response[1]['name']}\n\nDescription:\n{self.response[1]['description']}\n\nGenre:{self.response[1]['genre']}\nStudio:{self.response[1]['studio']}\nOriginal Title:{self.response[1]['original_title']}\nStatus:{self.response[1]['status']}\nPremiere:{self.response[1]['premiere']}\nSeason:{self.response[1]['season']}\nTotal Episodes:{self.response[1]['episodes']}\nNext Episode:{self.response[1]['new_ep']}" + '\n```'
        else:
            second_btn.disabled = True
            content = "Teehee"
        await interaction.response.edit_message(content=content, view=self)
    
    
    @discord.ui.button(label='3', custom_id='third')
    async def third_btn_callback(self, interaction, third_btn):
        if(len(self.response) > 2):
            content = '```\n' + f"Name: {self.response[2]['name']}\n\nDescription:\n{self.response[2]['description']}\n\nGenre:{self.response[2]['genre']}\nStudio:{self.response[2]['studio']}\nOriginal Title:{self.response[2]['original_title']}\nStatus:{self.response[2]['status']}\nPremiere:{self.response[2]['premiere']}\nSeason:{self.response[2]['season']}\nTotal Episodes:{self.response[2]['episodes']}\nNext Episode:{self.response[2]['new_ep']}" + '\n```'
        else:
            third_btn.disabled = True
            content = "Teehee"
        await interaction.response.edit_message(content=content, view=self)

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.message.author:
            await interaction.response.send_message('You cant use that', ephemeral=True)
            return False
        return True

def create_ui_search(message, response):
    view = SearchView(message, response)
    return view

def create_ui_help(message):
    view = HelpView(message)
    return view

def create_ui_anime(message, response):
    view = AnimeView(message, response)
    return view

# Send messages
async def send_message(message, user_message, is_private, client=False):
    try:
        if(user_message[0] in ['p', 'n', 'c', 'l'] and user_message != 'ping'):
            response = responses.handle_response_search(user_message)
            view = create_ui_search(message, response)
            if(len(response) == 0):
                message.author.send('Nothing found') if is_private else await message.channel.send('Nothing found')
            else:
                await message.author.send(response[0], view=view) if is_private else await message.channel.send(response[0], view=view)
        
        elif(user_message[:4] == 'help' or user_message[0] == 'h' and user_message != 'hello'):
            response = responses.handle_response_help()
            view = create_ui_help(message)
            await message.author.send(response, view=view) if is_private else await message.channel.send(response, view=view)
        
        elif(user_message[:5] == 'anime'):
            response = responses.handle_anime_response(user_message)
            view = create_ui_anime(message, response)
            if(response[0]['code'] == 0):
                output = response[0]['name']
                view = None
            else:
                output = f"```\nTop {len(response)} results:\n" + "\n".join([str(i+1)+ '. ' + response[i]['name'] for i in range(len(response))])  + "\n```"
            await message.author.send(output, view=view) if is_private else await message.channel.send(output, view=view)
        
        else:
            response = responses.handle_response_misc(user_message, client)
            await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_bot():
    TOKEN = config.token
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):

        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if(user_message[0] + user_message[1] != 'j!'):
            return
    
        # Debug printing
        with open('logs', 'a') as file:
            file.write((f"{username} said: '{user_message}' in ({channel})\n"))

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[2] == '?':
            user_message = user_message[3:]
            await send_message(message, user_message, is_private=True)
        else:
            user_message = user_message[2:]
            await send_message(message, user_message, is_private=False, client=client)

    client.run(TOKEN)