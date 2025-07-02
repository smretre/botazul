from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "7978947898:AAFfshFH2M03IMfqLnyzS8rpL7tJAvkUzP8"

WELCOME_MESSAGE = """👋 Seja bem-vindo(a) ao grupo!

💸 Conheça o Azul Fund: a plataforma que está mudando vidas!

✅ Ganhe R$1.000 de bônus na hora do cadastro  
✅ Rendimento real que pode ser sacado via Pix  
✅ R$2 por login diário, sem precisar investir do bolso  
✅ Saque mínimo de apenas R$10!

🚀 Comece agora e transforme cliques em renda:
👉 https://azulfund.com?promotion=ESb9QG

Qualquer dúvida, estamos aqui no grupo pra ajudar! 💙"""

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(WELCOME_MESSAGE)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

print("🤖 Bot rodando... pressione CTRL+C para parar")
app.run_polling()
