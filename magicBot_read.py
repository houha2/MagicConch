import praw
from praw.models import MoreComments
import random
import os

SUBREDDIT           = "BikiniBottomTwitter"

USER_AGENT          = 'MagicConch Bot 0.1 (by u/Tris42)'
BOT_USERNAME        = os.getenv('BOT_USERNAME')
BOT_PASSWORD        = os.getenv('BOT_PASSWORD')
CLIENT_ID           = os.getenv('CLIENT_ID')
CLIENT_SECRET       = os.getenv('CLIENT_SECRET')

MAGIC_CONCH_PHRASE  = 'magic conch'
KEYWORDS            = ['all hail the magic conch', 'praise the magic conch']
QUESTIONS_PHRASES   = ['will', 'what should i', 'could i']
REPLIES             = ['Maybe some day', 'I don\'t think so', 'no', 'yes', 'Nothing', 'Try asking again']

reddit_client = praw.Reddit(user_agent=USER_AGENT,
                           client_id=CLIENT_ID,
                           client_secret=CLIENT_SECRET,
                           username=BOT_USERNAME,
                           password=BOT_PASSWORD)

def get_bot_response():
  chosen_bot_response = random.choice(REPLIES)
  full_bot_response = chosen_bot_response + '\n' + \
                      "-I am a bot, please don\'t hurt me"
  return full_bot_response

def log_bot_response(comment, bot_response):
  sep = '-' * 20
  msg = (
    sep + '\n' + 
    "Comment: " + comment + '\n' + 
    "Bot Response: " + bot_response + '\n' + 
    sep
  )
  print(msg)

subreddit = reddit_client.subreddit(SUBREDDIT)
for submission in subreddit.hot(limit=20):
  allComments = submission.comments.list()
  for comment in allComments:
    if isinstance(comment, MoreComments):
      continue
    comment = comment.body.lower() # only looking at singleton comments
    if MAGIC_CONCH_PHRASE not in comment:
      continue
    for phrase in QUESTIONS_PHRASES:
      if phrase in comment and '?' in comment: # comment is valid question
        bot_response = get_bot_response()
        submission.reply(bot_response)
        log_bot_response(bot_response)
        break # bot makes 1 response per comment
      else:
        print("no calls to the conch")
