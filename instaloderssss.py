import instaloader
L = instaloader.Instaloader()


username = 'ald.rich' 
password = 'GUitars252255199' 
L.login(username, password)

instagram_target = 'maldini4869' 
profile = instaloader.Profile.from_username(L.context, instagram_target)


follow_list = []
count = 1
file = open("instagram_followers.txt","w")
for followee in profile.get_followers():
    username = followee.username
    file.write(str(count) + ". " + username + "\n")
    print(str(count) + ". " + username)
    count = count + 1
    
print("list followers")

for post in profile.get_posts():
    shortcode = post.shortcode
    file.write(str(count) + ". " + shortcode + "\n")
    print(str(count) + ". " + shortcode)
    count = count + 1

print("post, hashtag and comments")

for post in profile.get_posts():
    L.download_post(post, target=profile.username)
    file.write(str(count) + ". " + username + "\n")
    print(str(count) + ". " + username)
    count = count + 1
    
print("likes")

for like in profile.get_likes():
    L.download_like(like, target=profile.username)
    file.write(str(count) + ". " + username + "\n")
    print(str(count) + ". " + username)
    count = count + 1
file.close()

