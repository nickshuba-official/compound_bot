from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from button import *
from reply import *
from model.financial import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    r_start = f"""
    👋 Привет, {update.message.chat.first_name}!
    Рад приветствовать в нашем боте.
    """

    await update.message.reply_text(r_start)
    await update.message.reply_text(
        text=r_start_2,
        reply_markup=ReplyKeyboardMarkup(keyboard=[[b_calc]], resize_keyboard=True)
    )
    await update.message.delete()


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=r_main,
        reply_markup=ReplyKeyboardMarkup(keyboard=[[b_calc]], resize_keyboard=True)
    )
    await update.message.delete()
    return 0


async def comp1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global r
    r = update.message.text
    r = r.replace(",", ".")
    r = r.replace("%", "")
    r = float(r)

    await update.message.reply_text(
        text=r_comp1,
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [b_daily, b_weekly, b_monthly, b_quarterly],
            [b_semiannual, b_annual, b_bullet, b_continuous],
            [b_calc]
        ], resize_keyboard=True)
    )
    return 1


async def comp2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global c1
    c1 = update.message.text

    await update.message.reply_text(
        text=r_comp2,
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [b_daily, b_weekly, b_monthly, b_quarterly],
            [b_semiannual, b_annual, b_bullet, b_continuous],
            [b_calc]
        ], resize_keyboard=True)
    )
    return 2


async def term(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global c2
    c2 = update.message.text

    await update.message.reply_text(
        text=r_term,
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [b_skip]
        ], resize_keyboard=True)
    )
    return 3


async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global c2
    c2 = update.message.text

    """Skips the location and asks for info about the user."""
    await update.message.reply_text(
        text=r_result
    )
    return 3


async def result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # term param
    global t
    t = update.message.text
    if t != "skip":
        t = int(t)

    await update.message.reply_text(
        text=r_result
    )

    comp_result = compound(
        rate=float(r),
        current_comp=c1,
        target_comp=c2,
        bullet_term_mnth=t
    )

    await update.message.reply_text(
        text=str(comp_result),
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[b_calc]],
            resize_keyboard=True
        ))

    await update.message.reply_text(
        text="Если нужно посчитать еще нажмите /calc.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[b_calc]],
            resize_keyboard=True
        ))

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Ошибка ввода.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

compound_handler = ConversationHandler(
        entry_points=[CommandHandler("calc", calc)],
        states={
            0: [MessageHandler(filters.Regex(".*"), comp1)],
            1: [MessageHandler(filters.Regex(".*"), comp2)],
            2: [MessageHandler(filters.Regex(".*"), term), CommandHandler("skip", skip)],
            3: [MessageHandler(filters.Regex(".*"), result)]

        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )