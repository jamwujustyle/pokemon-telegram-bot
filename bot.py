from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from typing import Final
from config import read_token, read_api
from fetch_poke import fetch_pokemon

TOKEN: Final = read_token()
BOT_USERNAME: Final = "@grab_pokemonBot"
POKEMON_API: Final = read_api()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi! this is a pokemon bot")


async def list_pokemons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Some pokemon names: \nPikachu, Bulbazaur, Charmander, Venusaur, Squirtle, Charizard, Metapod, Caterpoe, Blastoise, Wartortle"
    )


async def grab_pokemon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Please provide the name of a Pokemon. Example: /grab pikachu"
        )
    pokemon_name = context.args[0]
    pokemon_data = fetch_pokemon(POKEMON_API, pokemon_name)

    if "error" in pokemon_data:
        await update.message.reply(pokemon_data["error"])
    else:
        name = pokemon_data.get("name", "Unknown")
        height = pokemon_data.get("height", "N/A")
        weight = pokemon_data.get("weight", "N/A")
        types = ", ".join(
            t.get("type", {}).get("name", "") for t in pokemon_data.get("types", [])
        )

        await update.message.reply_text(
            f"Name: {name}\nHeight: {height}\nWeight: {weight}\nTypes: {types}"
        )


async def get_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "this is a pokemon bot. enter a name of a pokemon to get info!"
    )


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("list", list_pokemons))
    app.add_handler(CommandHandler("grab", grab_pokemon))
    app.add_handler(CommandHandler("help", get_help))

    app.run_polling(poll_interval=3)
