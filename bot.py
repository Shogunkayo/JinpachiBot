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
        await interaction.response.send_message(content=content)

    @discord.ui.button(label='Misc', custom_id='misc')
    async def misc_btn_callback(self, interaction, misc_btn):
        content = '```\nj!hello -> greet the bot :) it can get lonely sometimes\nj!roll -> get a random number between 1 and 100\nj!ping -> get the latency```'
        await interaction.response.send_message(content=content)

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

        # Debug printing
        with open('logs', 'a') as file:
            file.write((f"{username} said: '{user_message}' in ({channel})\n"))

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        elif user_message[0] + user_message[1] == 'j!':
            user_message = user_message[2:]
            await send_message(message, user_message, is_private=False, client=client)

    client.run(TOKEN)