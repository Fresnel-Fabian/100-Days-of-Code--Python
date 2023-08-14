from internetspeedtwitterbot import InternetSpeedTwitterBot

EMAIL = "fresnelfabian@gmail.com"
PASSWORD = "Fresnel@18"
USERNAME = "FresnelFabian_"
PROMISED_DOWN = 10
PROMISED_UP = 10
i = InternetSpeedTwitterBot()
# i.get_internet_speed()
# if i.up < 7 and i.down < 7:
i.tweet_at_provider(EMAIL, PASSWORD, USERNAME, PROMISED_DOWN, PROMISED_UP)