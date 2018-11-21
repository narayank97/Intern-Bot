import praw
import config_int
import time
import os

def bot_login():
    r = praw.Reddit(client_id = config_int.client_id,
                    client_secret = config_int.client_secret,
                    user_agent = "Internship Bot scrapes cscareerquestions")
    return r


def run_bot(comment_id_tracker,comments_replied_to):

    print("Grabbing subreddit Master ...")

    subreddit = r.subreddit("cscareerquestions").comments(limit = None)

    print("I am grabbing the posts and comments master ...")

    words_to_match = ['internship','sophmore']

    for comment in subreddit:

        comment_text = comment.body.lower()

        isMatch = any(string in comment_text for string in words_to_match)

        if comment.id not in comment_id_tracker and isMatch:

            ## print("Match found Master ...")

            comment_id_tracker.append(comment.id)

            comments_replied_to.append(comment.body)

            ## print(comment.body)

            with open("internship_Stuff.txt", "a") as f:
                f.write(comment.body)
                f.write("\n\n")

    print("Done checking Master.")

def get_saved_comments():

    if not os.path.isfile("internship_Stuff.txt"):

        comments_replied_to = []

    else:
        with open("internship_Stuff.txt","r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None,comments_replied_to)

    return comments_replied_to

comment_id_tracker = [] ## list to prevent over scraping duplicate comments

r = bot_login()
r.read_only = True
comments_replied_to = get_saved_comments()
while True:
    run_bot(comment_id_tracker,comments_replied_to)
    time.sleep(10)
