import time
from praw import Reddit
from os import getenv
from sql_wrapper import SQL
from dotenv import load_dotenv
load_dotenv()

reddit = Reddit(
    client_id=getenv('DPB_CLIENTID'),
    client_secret=getenv('DPB_CLIENTSECRET'),
    user_agent=f"{getenv('DPB_SUBREDDIT')}'s DiscordPromoterBot'",
    username=getenv('DPB_USERNAME'),
    password=getenv('DPB_PASSWORD'),
)

db = SQL('posts.db')

submission_stream = reddit.subreddit(
    getenv('DPB_SUBREDDIT')).stream.submissions()

while True:
    for submission in submission_stream:
        # stops when posts older than 12 hours are reached
        # if submission.id in database:
        # break

        minutes_since_post = (time.time() - submission.created_utc) / 60
        if minutes_since_post > 720:  # checks post is within past 12 hours
            pass
            # db.remove(previous_post_older_than_12 hours)
            # db.add(submission.id)
        else:
            if submission.score >= getenv("DPB_MINSCORE"):
                # stickied discord promo comment
                comment_made = submission.reply(getenv("DPB_MESSAGE"))
                comment_made.mod.distinguish(sticky=True)
