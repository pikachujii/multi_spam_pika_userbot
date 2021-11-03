from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("PIKACHU MULTISPAM BOT STRING GENERATOR")
print("")
API_KEY = "6507247"
API_HASH = "209032e68c419e88a982e827552cf40c"

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("")
            session = client.session.save()
            client.send_message("me", f"`{session}`")
            print(
                "Your Telethon String session has been successfully stored in your telegram, Please check your Telegram Saved Messages"
            )
            print("")
    except:
        print("")
        print("Wrong phone number \n make sure its with correct  country code")
        print("")
        continue
    break
