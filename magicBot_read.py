#from urllib.parse import quote_plus
import praw
import random
from praw.models import MoreComments

myUserAgent = 'MagicConch Bot 0.1 (by u/Tris42)'
myClientId = #secret ID 
myCLientSecret = #secret client per Reddit Api rules
keyWords = [ 'all hail the magic conch', 'praise the magic conch']
questionsPhrases = ['will','what should i', 'could i' ]
replies = ['Maybe some day', 'I don\'t think so', 'no', 'yes', 'Nothing', 'Try asking again']
reddit = praw.Reddit(user_agent=myUserAgent,
                      client_id=myClientId,
                      client_secret=myCLientSecret,
                      username='magicConchBot12',
                      password= #also a secret)

subreddit = reddit.subreddit("bikinibottomTwitter")
for submission in subreddit.hot(limit=20):
  allComments = submission.comments.list()
  for comment in allComments:
    if isinstance(comment, MoreComments):
      continue
    currentComment = comment.body.lower()
    if 'magic conch' in currentComment:
      for phrase in questionsPhrases:
        if phrase in currentComment and '?' in currentComment:
          replyNumber = random.randint(0,5)
          submission.reply(replies[replyNumber]'-I am a bot, please don\'t hurt me')
         # print(comment.body)
         # print(replies[replyNumber],"-I am a bot, please don\'t hurt me")
         # print('---------------------------------------------\n')
    else:
      print("no calls to the conch")
