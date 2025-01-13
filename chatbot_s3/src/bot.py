import telebot
from utils import call_llama

TOKEN = "7672878752:AAG9uZ6W3ms_JGHfJwx4t0H8U0EdkvHLrl0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["/start"])
def welcome(message):
    bot.reply_to(message, "Hi there! I'm your Llama-powered bot. Ask me anything. 😊")

@bot.message_handler(func=lambda message: True)
def handle(message):
    user_input = message.text
    bot.reply_to(message, "thinking...")

    response = call_llama("llama3.2", user_input)

    if "response" in response:
        bot.send_message(message.chat.id, response["response"])
    else:
        error_message = response.get("error", "something went wrong")
        bot.send_message(message.chat.id, f"error {error_message}")
        if "details" in response:
            bot.send_message(message.chat.id, f"details: {response["details"]}")

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()