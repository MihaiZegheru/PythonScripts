from instaFollower import InstaFollower

EMAIL = ""
PASSWORD = ""


bot = InstaFollower()
bot.login(EMAIL, PASSWORD)
bot.find_followers()
bot.follow()

