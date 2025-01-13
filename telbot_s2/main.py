import telebot
from get_token import get_spotify_token
from getsongs import get_songs_by_singer

client_id = "9b3001e75c2346478a951e4bfefd8eff"
client_secret = "087ed2886e4b489091a9cd82b665c5fd"

token = get_spotify_token(client_id, client_secret)

API_TOKEN = "7418170803:AAHQm3uwGHX3Ig4qOhrezCWM_cWhrcdAdvQ"
bot = telebot.TeleBot(API_TOKEN)

# Handle /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Welcome! Send me a singer's name, and I'll return a list of their songs."
    )

# Handle text messages (singer names)
@bot.message_handler(func=lambda message: True)
def send_songs(message):
    singer_name = message.text.strip()
    bot.reply_to(message, f"Searching for songs by {singer_name}...")

    try:
        # Call your Spotify function
        songs = get_songs_by_singer(singer_name, token)

        # Create a response
        if songs:
            response = f"Songs by {singer_name}:\n" + "\n".join(songs)
        else:
            response = f"Sorry, no songs found for {singer_name}."

    except Exception as e:
        response = f"An error occurred while fetching songs: {str(e)}"

    # Reply with the result
    bot.reply_to(message, response)



# Start polling
print("Bot is running...")
bot.polling()
