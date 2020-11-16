# DiscordPromoterBot
Promotes the Discord server on posts that hit a set amount of votes

## How to run the thing

1. Clone the repo
2. Change the name of `.env.example` to `.env` file in the top-level directory of the project and fill it with appropriate values
3. Run `pip install -r requirements.txt`
4. In `src/`, create a file called `posts.db`
5. Run `sqlite3 -init schema.sql`
6. Run `python bot.py`

If you've done everything correctly, the bot should be up and running.