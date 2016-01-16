import praw
import argparse

parser = argparse.ArgumentParser(description='Stream self posts from any subreddit.')
parser.add_argument('-sub', required=False, default='all', help='Subreddit name (default=\'all\')')
parser.add_argument('-limit', required=False, default=100, help='Post limit (default=100, max=1000)', type=int)

args = parser.parse_args()
args.limit = 1000 if args.limit > 1000 else args.limit

r = praw.Reddit(user_agent='stream only self posts from a sub by /u/km97')
posts = [post for post in r.get_subreddit(args.sub).get_hot(limit=args.limit) if post.is_self]

for post in posts:
    print("Title:", post.title)
    print("Score: {} | Comments: {}".format(post.score, post.num_comments))
    print()
    print(post.selftext.replace('**', '').replace('*', ''))
    print()
    print("Link:", post.permalink)
    print('=' * 30)
