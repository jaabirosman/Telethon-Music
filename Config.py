import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17357369"))
    API_HASH = os.environ.get("API_HASH", "46da8af2f3a14d8a14fcfd9180ba56ba")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5739937035:AAF4h-mM5QD9xKkXq_tT-hx4pGXkxW2pzVg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BABSNFMpwzGPD4-KHjnG3hJ-pTFQKOmpOckWmfYiaNyfYVXbj6hi0jDHvMSpXVFxztr6TCMWJ_XJWa_D8TNme3sxwc3ymuWweeRfYvIU-sMhpQdds-0O05eakZ6pLcVvn2-1BLtqrP-QFe9L7oycgbIBXmMcDLQsqdUQQdDFcCbl6KWjnxRKbIxvMe3EAPeJuSfyq-xdnuvmviM6jOMCMUD-655AXzt4qci0t3UFSJtXAFA7Oz7MPB-qsCmMsGP2lm57V2iCn-TEdmxFW5CUWkagTvYDN8PPyg91M4b7nEeHAlNKQ5m9jtlz2WEhOJ-9FJ1o-xFt1nvh3Ho7JwdRaGboAAAAAS6VeJAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Anwar_Music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "osmanigroupbot")
    CHANNEL = os.environ.get("CHANNEL", "teamosmani")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID")) # required
