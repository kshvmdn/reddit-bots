import praw, time

# replace with your username/password
username, password = USERNAME, PASSWORD

r = praw.Reddit(user_agent='A "tomorrow"-misspelling corrector by /u/tomorrow_corrector')
r.login(username, password, disable_warning=True)


def run_bot():
    '''Check /r/all for mispellings in comments and reply to them.'''

while True:
    run_bot()
    time.sleep(30)
