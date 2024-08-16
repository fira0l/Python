facebook_post = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 2, "Shares": 3},
    {"Comments": 2, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]

total_likes = 0
for post in facebook_post:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass
print(f"total_like is {total_likes}")
