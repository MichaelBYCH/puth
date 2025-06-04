import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


BOT_TOKEN = '8149108285:AAFdGVC5G4I8N-Ocbswg8hTLxkcbIk-UgGc'

# Словарь для хранения статистики игроков
stats = {}

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Это игра 'Камень, ножницы, бумага'. Нажмите /play, чтобы начать.")

# Функция для обработки команды /play
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Камень", callback_data='rock')],
        [InlineKeyboardButton("Ножницы", callback_data='scissors')],
        [InlineKeyboardButton("Бумага", callback_data='paper')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите:", reply_markup=reply_markup)

# Функция для обработки выбора игрока
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    user_choice = query.data
    bot_choice = random.choice(['rock', 'scissors', 'paper'])
    user_id = query.from_user.id

    result = determine_winner(user_choice, bot_choice)

    # Обновляем статистику
    if user_id not in stats:
        stats[user_id] = {"wins": 0, "losses": 0, "draws": 0}

    if result == "win":
        stats[user_id]["wins"] += 1
        await query.edit_message_text(f"Вы выбрали {user_choice}, я выбрал {bot_choice}. Вы победили!")
    elif result == "loss":
        stats[user_id]["losses"] += 1
        await query.edit_message_text(f"Вы выбрали {user_choice}, я выбрал {bot_choice}. Вы проиграли.")
    else:
        stats[user_id]["draws"] += 1
        await query.edit_message_text(f"Вы выбрали {user_choice}, я выбрал {bot_choice}. Ничья.")

# Функция для определения победителя
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "draw"
    if (user_choice == "rock" and bot_choice == "scissors") or \
       (user_choice == "scissors" and bot_choice == "paper") or \
       (user_choice == "paper" and bot_choice == "rock"):
        return "win"
    return "loss"

# Функция для обработки команды /stats
async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if user_id in stats:
        await update.message.reply_text(
            f"Ваша статистика:\nПобед: {stats[user_id]['wins']}\nПоражений: {stats[user_id]['losses']}\nНичьих: {stats[user_id]['draws']}"
        )
    else:
        await update.message.reply_text("Статистика пока отсутствует. Сыграйте хотя бы одну игру!")

import random

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("stats", stats_command))

    application.run_polling()

if __name__ == '__main__':
    main()
