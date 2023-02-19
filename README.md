# **About**

A script that monitors Reddit for new posts in subreddits of choice based on keywords. Keyword are words that have to be found as well as the words that must not be used in the titles of posts.

When a new post is posted, the user will get a Pushbullet notification on their phone containing the title and the link to the post.

The script runs indefinitely, until stopped by the user.

# **Usage**

A file called [config.json](https://github.com/djordje-pejic/Reddit-Notification-Tracker/tree/main/resources/config.json) was created in order to protect the user's private data. It can be found in [resources](https://github.com/djordje-pejic/Reddit-Notification-Tracker/tree/main/resources). It is the file that stores necessary data for the proper functioning of notification tracker. It needs to be modified and provided with the following information:

- Username, password, client ID, client secret, and user agent provided by Reddit API 

- Pushbullet API key 

- Subredit names and keywords. The script monitors a list of subreddits and one subreddit of choice. The list of subreddits (general_subreddits) is being monitored based on the words specified in all_keywords, while the specific subreddit is monitored based on the words in specific_keywords. The words that must not appear in the title are specified in invalid_match. 

# **License**

The project is licensed under [GNU General Public License v3.0](https://github.com/djordje-pejic/Reddit-Notification-Tracker/blob/main/LICENSE)