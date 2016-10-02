import praw
import time
import random
from lxml import html

r = praw.Reddit(user_agent = "Random Image Responder")

r.login('us','pss')

# Use words to look for
words_to_match = ['Words to look for']
cache = []
cachesub = []


def run_bot():
	print("Grabbing subreddit...")
	subreddit = r.get_subreddit("753951")
	# Check submissiones in subreddit
	submissions = list(r.get_subreddit("subreddit").get_hot(limit=10))
	print("Grabbing comments...")
	comments = subreddit.get_comments(limit=10)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:
			
			rnd = random.uniform(0, 9)
			rnd = int(round(rnd))

			print("Match found! Comment Id" + comment.id)
			# Reply Text with Random Image
			comment.reply('Text' +' [Image]('+ submissions[rnd].url +')')
			print("Reply Success!")

			cache.append(comment.id)
			cachesub.append(submissions[rnd].id)

	print("For loop finish, time to sleep...")

while True:
	run_bot()
	time.sleep(10)
