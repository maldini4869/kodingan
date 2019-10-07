#import instaloader sebaga crawler intuk instagram
import instaloader

L = instaloader.Instaloader()

#login akun instagram, pada kali ini saya menggunakan instagram saya sendiri
L.interactive_login('maldini4869')

#mendapatkan data profil dari akun,saya menggunakan akun saya
profile = instaloader.Profile.from_username(L.context, 'maldini4869')

#mendapatkan URL post
posts = list(profile.get_posts())

#mendapatkan URL dari followers 
followers = set(profile.get_followers())

for post in profile.get_posts():
    print(post)

for followers in profile.get_followers():
    print(followers)

#mencetak URL dari tiap post yang ada d tiap followers
for followers in profile.get_followers():
    for post in profile.get_posts():
        print(post)





