"""A script that monitors Reddit for new posts in subreddits of choice based on keywords. 
   Keyword are words that have to be found as well as the words that must not be used in the titles of posts.
   When a new post is posted, the user will get a Pushbullet notification on their phone containing the title and the link to the post.
   The script runs indefinitely, until stopped by the user

   Uses Reddit and Pushbullet API.
"""

import praw
import json
import pushbullet

#loading configuration file
with open('./resources/config.json') as f:
    config = json.load(f)

pb = pushbullet.PushBullet(config['pushbullet']['api_key'])

reddit = praw.Reddit(
    client_id=config['reddit']['client_id'],
    client_secret=config['reddit']['client_secret'],
    password=config['reddit']['password'],
    user_agent=config['reddit']['user_agent'],
    username=config['reddit']['username']
)

#multiple subreddits can be specified by joining them with pluses (+)
subreddits = '+'.join([subreddit for subreddit in config['monitor']['general_subreddits']]) + "+" + config['monitor']['specific_subreddit']
#class for Subreddits
subreddit = reddit.subreddit(subreddits)

#retrieve all new submissions made to the subreddits specified in the subreddits string
for entry in subreddit.stream.submissions(skip_existing=True):
    if any(word in entry.title.lower() for word in config['push_message']['invalid_match']):
        continue
    elif entry.subreddit.display_name == config['monitor']['specific_subreddit'] and any(word in entry.title.lower() for word in config['push_message']['specific_keywords']):
        pb.push_note(entry.title, "www.reddit.com" + entry.permalink)
    elif entry.subreddit.display_name in config['monitor']['general_subreddits'] and any(word in entry.title.lower() for word in config['push_message']['all_keywords']):
        pb.push_note(entry.title, "www.reddit.com" + entry.permalink)