from instafollowers import InstaFollowers
USERNAME = "fresnelprince@gmail.com"
PASSWORD = "Fresnel@2001"
SIMILAR_ACCOUNT = "chefsteps"

bot = InstaFollowers()
bot.login(USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
