from praw import reddit
from os import getenv
from sql_wrapper import SQL
from dotenv import load_dotenv
load_dotenv()

reddit = reddit(
    client_id=getenv('DPB_CLIENTID'),
    client_secret=getenv('DPB_CLIENTSECRET'),
    user_agent=f"{getenv('DPB_SUBREDDIT')}'s DiscordPromoterBot'}",
    username=getenv('DPB_USERNAME'),
    password=getenv('DPB_PASSWORD'),
)

db = SQL('posts.db')
