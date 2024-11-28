from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Hello! Welcome to Condor Capital Bot. Use /links to explore our resources!'
    )

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Commands available:\n'
        '/start - Start the bot\n'
        '/help - List available commands\n'
        '/links - Explore resources with links and images!'
    )

# Links command handler
async def links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Define links, images, and captions
    resources = [
        {
            "image": "images/IMG_3404.PNG",
            "caption": "Explore Endless Gimps! [Link](https://gimporium.xyz/loading.html)"
        },
        {
            "image": "images/99_Billion_Gimps.png",
            "caption": "Visit the NFT Marketplace! [Link](https://www.gimpnftgallery.com/)"
        },
        {
            "image": "images/shop.webp",
            "caption": "Shop the Collection! [Link](https://my-store-7766589.creator-spring.com/)"
        },
        {
            "image": "images/ock2.jpeg",
            "caption": "Learn about Artist Ock! [Link](https://ock-website.vercel.app/)"
        },
        {
            "image": "images/gold_condor_icon.png",
            "caption": "Gold Condor Capital! [Link](https://www.gcc-bsc.online/)"
        },
        {
            "image": "images/cake.png",
            "caption": "Buy GCC Tokens! [Link](https://pancakeswap.finance/swap?outputCurrency=0x092ac429b9c3450c9909433eb0662c3b7c13cf9a)"
        },
        {
            "image": "images/youtube.jpg",
            "caption": "Watch on YouTube! [Link](https://www.youtube.com/@TradingNFTwithGCC/streams)"
        },
        {
            "image": "images/art.jpg",
            "caption": "Play Games! [Link](https://www.gccgames.vercel.app)"
        },
        {
            "image": "images/twitter.webp",
            "caption": "Follow on Twitter! [Link](https://twitter.com/GimpNft)"
        },
        {
            "image": "images/tiktok.png",
            "caption": "Follow on TikTok! [Link](https://www.tiktok.com/@ockdraws)"
        },
    ]

    # Send each image with its caption
    for resource in resources:
        image_path = resource["image"]
        caption = resource["caption"]

        # Send the image with the caption
        with open(image_path, "rb") as photo:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo,
                caption=caption,
                parse_mode="Markdown"
            )

# Main function
def main():
    # Your bot token
    TOKEN = "6520064780:AAENR13Z2mLpannbnBXXvGeIgkQnvAgGaUg"  # Replace with your actual bot token

    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("links", links))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
