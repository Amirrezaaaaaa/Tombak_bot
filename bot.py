from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import asyncio

bot_token = "7962689863:AAElTSY-_ceMI9cyRRUicKQUxOgt0FJH1q0"


async def porn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("❗ این کامند رو روی پیام خودت ریپلای کن")
        return

    if update.message.from_user.id != update.message.reply_to_message.from_user.id:
        await update.message.reply_text("❗ فقط میتونی روی پیام خودت این کامند رو استفاده کنی")
        return

    try:
        await update.message.delete()
    except Exception as e:
        print("❌ Error With Deleting Message :", e)

    await update.message.reply_to_message.reply_text("✅ پیام انتخاب‌شده بعد از ۲۴ ساعت حذف خواهد شد")

    await asyncio.sleep(86400)

    try:
        await context.bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.message.reply_to_message.message_id
        )
        print("✅ Message Deleted Successfully")
    except Exception as e:
        print("❌ Error With Deleting Message :", e)


def main():
    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("porn", porn_command))
    print("🔧 Bot Runned")
    app.run_polling()


if __name__ == "__main__":
    main()
