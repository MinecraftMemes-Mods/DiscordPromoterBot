import praw
from os import getenv
from time import sleep, time
from sql_wrapper import SQL
from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(
    client_id=getenv('DPB_CLIENTID'),
    client_secret=getenv('DPB_CLIENTSECRET'),
    user_agent=f"{getenv('DPB_SUBREDDIT')}'s DiscordPromoterBot'",
    username=getenv('DPB_USERNAME'),
    password=getenv('DPB_PASSWORD'),
)

db = SQL('../posts.db')

while True:
    hot_posts = reddit.subreddit(getenv('DPB_SUBREDDIT')).hot()
    for post in hot_posts:
        if db.get(post.id):
            # post already in db, so a comment has,
            # already been made.
            continue
        elif post.score < int(getenv('DPB_MINSCORE')):
            # score less than required
            continue
        elif post.distinguished or post.stickied:
            # we don't want to replace pinned comments on mod posts
            continue
        elif post.comments[0].distinguished:
            # we don't want to replace pinned comments on regular posts either
            continue
        elif (time()-post.created_utc)/60 > int(getenv('DPB_MAXAGE')):
            # we don't want to post comments on old posts
            continue

        # all checks have passed. we can make the comment,
        # and add the post to the database
        reply = post.reply(getenv('DPB_COMMENT'))
        reply.mod().distinguish(how='yes', sticky=True)
        db.add(post.id)

    # let's not get suspended from the API, shall we?
    sleep(int(getenv('DPB_INTERVAL')))
