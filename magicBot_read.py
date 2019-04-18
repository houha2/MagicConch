#from urllib.parse import quote_plus
import praw

myUserAgent = 'MagicConch Bot 0.1 (by u/Tris42)'

keyWords = [ 'all hail the magic conch', 'praise the magic conch']
questionsPhrases = ['will','what should i', 'could i' ]
replies = ['Maybe some day', 'I don\'t think so', 'no', 'yes', 'Nothing', 'Try asking again']
reddit = praw.Reddit(user_agent=myUserAgent,
                      client_id=myClientId,
                      client_secret=myCLientSecret)

subreddit = reddit.subreddit("bikinibottomTwitter")
for submission in subreddit.stream.submissions():
  allComments = submission.comments.list()
  for comment in allComments:
    currentComment = comment.body.lower()
    if 'magic conch' in currentComment:
      for phrase in questionsPhrases:
        if phrase in currentComment and '?' in currentComment:
          #replyTemplate = ''
          print(comment.body)