#Script to retrieve the top nth submissions of the "hot" and "new" sections of a certain subreddit
#Depending on the section, different attributes will be printed

import praw
#file with credentials for the bot
import Ze1598Bot_credentials as cred
reddit_instance = praw.Reddit(client_id = cred.client_id, client_secret = cred.client_secret, user_agent = cred.user_agent)
subreddit_instance = reddit_instance.subreddit('technology')

print('Subreddit name: {}\nSubreddit title: {}'.format(subreddit_instance.display_name, subreddit_instance.title))
print()

#Create a list with the top 3 submissions in the hot section of 'subreddit_instance'
first_nth_hot = list(subreddit_instance.hot(limit=4))
#Then delete the first submission (usually this post is about the subreddit itself/not relevant for this)
del first_nth_hot[0]

#Then print the title, score and url of each submission
print('Top', len(first_nth_hot), 'submissions in the hot section of', subreddit_instance)
for submission in first_nth_hot:
    print('Title:', submission.title)
    print('Score:', submission.score)  
    print('Url:', submission.url)
    print()
print()

#Create a list with the top 5 submissions in the new section of 'subreddit_instance'
first_nth_new = list(subreddit_instance.new(limit=5))

print('Top', len(first_nth_new), 'submissions in the new section of', subreddit_instance)
for submission in first_nth_new:
    print('Title:', submission.title)
    print('Url:', submission.url)
    print()