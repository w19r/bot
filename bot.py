from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def grade_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    try:
        grd = float(user_text)
        
        if grd > 1:
            await update.message.reply_text('out of range')
        elif grd < 0:
            await update.message.reply_text('out of range')
        elif grd >= 0.9:
            await update.message.reply_text('A')
        elif grd >= 0.8:
            await update.message.reply_text('B')
        elif grd >= 0.7:
            await update.message.reply_text('C')
        elif grd >= 0.6:
            await update.message.reply_text('D')
        elif grd < 0.6:
            await update.message.reply_text('F')
        else:
            await update.message.reply_text('error')
            
    except ValueError:
        await update.message.reply_text('الرجاء إدخال رقم!')

app = ApplicationBuilder().token("8504521425:AAECIk4as7iZU8VfnWkLzvI1xJMp6wly-BI").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, grade_bot))
app.run_polling()