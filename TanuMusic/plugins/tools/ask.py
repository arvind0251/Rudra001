from pyrogram import Client, filters
import requests
import urllib.parse
from TanuMusic import app

# Function to query the AI API
def ask_query(query, model=None):
    default_model = 'claude-sonnet-3.5'
    system_prompt = "You are TanuMusic, a helpful assistant bot designed to play music on Telegram. Your name is TanuMusic, and your owner's name is The Captain. TanuMusic can play YouTube live streams and songs from other platforms like Spotify and SoundCloud. If anyone asks how to contact your owner, you respond: 'You can reach The Captain on Telegram with the username @itzAsuraa, or through the channel @C0DE_SEARCH. For support, join the group @AsuraaSupports or contact the bot at @TanuMusicxBot."

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return f"Error fetching response from API. Status code: {response.status_code}"

# Handler for the "/ask" command
@app.on_message(filters.command("ask"))
def handle_query(client, message):
    if len(message.command) < 2:
        message.reply_text("<b>Please provide a query to ask.</b>")
        return

    user_query = message.text.split(maxsplit=1)[1]
    
    # Fetch the response from the AI API
    response = ask_query(user_query)

    # Send the response back to the user
    message.reply_text(f"<b>{response}</b>")