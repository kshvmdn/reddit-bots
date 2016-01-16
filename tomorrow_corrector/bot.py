import praw, time

# replace with your username/password
username, password = USERNAME, PASSWORD

r = praw.Reddit(user_agent='A "tomorrow"-misspelling corrector by /u/tomorrow_corrector')
r.login(username, password, disable_warning=True)

misspellings = ['tommorow', 'tommorrow', 'tomorow']
comment_cache = []

def run_bot():
    '''Check /r/all for mispellings in comments and reply to them.'''
    subreddit = r.get_subreddit('all')
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        if any(string in comment.body.lower() for string in misspellings) and not comment.id in comment_cache:
            comment.reply('I think you meant "tomorrow".')
            comment_cache.append(comment.id)

while True:
    run_bot()
    time.sleep(30)
