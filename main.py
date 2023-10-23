from telegram.ext import Application
from model.common import *
from handler import *


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    config = open_config()
    token = config["BOT"]["TOKEN"]
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(compound_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

