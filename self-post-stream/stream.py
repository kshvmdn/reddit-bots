import praw

r = praw.Reddit(user_agent='stream only self posts from a sub by /u/km97')
posts = [post for post in r.get_subreddit('all').get_hot(limit=50) if post.is_self]

# print(dir(posts[0]))

for post in posts:
    print("Title:", post.title)
    print("Score: {}, Comments: {}".format(post.score, post.num_comments))
    print()
    print(post.selftext.replace('**', '').replace('*', ''))
    print()
    print("Link:", post.permalink)
    print('=' * 30)
