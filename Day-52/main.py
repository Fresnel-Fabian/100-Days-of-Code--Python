from instafollowers import InstaFollowers
USERNAME = "INSTAGRAM USERNAME"
PASSWORD = "INSTAGRAM PASSWORD"
SIMILAR_ACCOUNT = "chefsteps"

bot = InstaFollowers()
bot.login(USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
