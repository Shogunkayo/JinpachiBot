import discord
import responses
import config
from discord.ui import Button, View


# Create Message View

class SearchView(View):
    def __init__(self, request, response):
        super().__init__(timeout=60)
        self.request = request
        self.current = 0
        self.response = response

    @discord.ui.button(label='<<-', custom_id='skip_start')
    async def skip_start_callback(self, interaction, skip_start_btn):
        skip_start_btn = [i for i in self.children if i.custom_id == 'skip_start'][0]
        await interaction.response.send_message('heheheheh')

    @discord.ui.button(label='<-', custom_id='prev')
    async def prev_callback(self, interaction, prev_btn):
        prev_btn = [i for i in self.children if i.custom_id == 'prev'][0]
        prev_btn.label = 'Turipipturip'
        await interaction.response.send_message('!!!')

    @discord.ui.button(label='->', custom_id='next')
    async def next_callback(self, interaction, next_btn):
        next_btn = [i for i in self.children if i.custom_id == 'next'][0]
        next_btn.label = 'HEHEHEHE'
        next_btn.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='->>', custom_id='skip_end')
    async def skip_end_callback(self, interaction, skip_end_btn):
        skip_end_btn = [i for i in self.children if i.custom_id == 'skip_end'][0]
        await interaction.response.send_message('sdmniasodnasopndsiao')

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.request.author:
            await interaction.response.send_message('You cant use that', ephemeral=True)
            return False
        return True

def create_ui_search(request, response):
    view = SearchView(request)
    return view

# Send messages
async def send_message(message, user_message, is_private):
    try:
        if(user_message[0] in ['p', 'n', 'c', 'l']):
            response = responses.handle_response_search(user_message)
            view = create_ui_search(message, response)
            await message.author.send(response, view=view) if is_private else await message.channel.send(response, view=view)
        else:
            response = responses.handle_response_misc(user_message)
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
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)