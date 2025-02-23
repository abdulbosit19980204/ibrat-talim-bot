from telethon import TelegramClient, events
import random
from datetime import datetime, time
import asyncio

# Hisoblar ro‘yxati (o‘zingizning ma’lumotlaringizni qo‘ying)
ACCOUNTS = [
    {
        "session_name": "session1",
        "api_id": "21300124",
        "api_hash": "ba1928901f7c9c75ecbffdd5a523280a",
        "phone": "+998908302885"
    },
    {
        "session_name": "session_name",
        "api_id": "27668593",
        "api_hash": "db44de3510fb53c30375bfce090989d9",
        "phone": "+998999992334"
    },

    # Yana hisob qo‘shmoqchi bo‘lsangiz, shu tarzda davom ettiring
]

# Tasodifiy javoblar uchun shablonlar va so‘zlar
KECHKI_SABLONLAR = [
    "Assalomu alaykum! Hozir {vaqt} bo‘ldi, men {ish} bilan {holat}, {vaqt2} yozaman.",
    "Kechirasiz, {vaqt} vaqtida {ish} bilan ovoraman, {vaqt2} javob qaytaraman!",
    "Salom! {vaqt} dam olish bilan {holat}, {vaqt2} sizga xabar qilaman."
]
KECHKI_SOZLAR = {
    "vaqt": ["kech", "tun", "kechki soatlar"],
    "ish": ["oilam", "shaxsiy ishlarim", "uy yumushlari"],
    "holat": ["bandman", "ovoraman", "tinch o‘tiribman"],
    "vaqt2": ["ertalab", "tongda", "keyinroq"]
}
KECHKI_EMOJILAR = ["🌙", "🏡", "😴", "⭐"]

ODDIY_SABLONLAR = [
    "Salom! Hozir {ish} bilan {holat}, lekin {vaqt} sizga yozaman.",
    "Afsuski, {ish} {holat}, ammo {vaqt} javob qaytaraman!",
    "Rahmat xabar uchun! {ish} {holat}, {vaqt} aloqaga chiqaman."
]
ODDIY_SOZLAR = {
    "ish": ["ishlarim", "vazifalarim", "kundalik yumushlarim"],
    "holat": ["ko‘p", "chalkashib ketdi", "ketma-ket kelyapti"],
    "vaqt": ["tezda", "birozdan keyin", "imkonim bo‘lganda"]
}
ODDIY_EMOJILAR = ["⏳", "📝", "🙏", "⏰"]

NAMOZ_SABLONLAR = [
    "{namoz} vaqti {holat}, {eslatma}!",
    "Hozir {namoz} vaqti, {eslatma} qilib oling.",
    "{eslatma} — {namoz} vaqti {holat}!"
]
NAMOZ_SOZLAR = {
    "holat": ["kirib keldi", "bo‘ldi", "yaqinlashdi"],
    "eslatma": ["Robbingizni eslang", "vaqtni boy bermang", "yuragingizni yoriting"]
}
NAMOZ_EMOJILAR = ["🕌", "🤲", "🌟", "☪️"]

ILM_SABLONLAR = [
    "Assalomu alaykum! Hozir ertalabki {soat}, {ilm} uchun eng yaxshi vaqt!",
    "Salom! Bu {soat} ilm olish uchun juda {sifat}, {harakat} qilib ko‘ring!",
    "Ertalabki {soat} — {ilm} bilan shug‘ullanish uchun {sifat} vaqt."
]
ILM_SOZLAR = {
    "soat": ["tong", "ertalab", "soatlar"],
    "ilm": ["ilm", "bilim", "o‘qish"],
    "sifat": ["ajoyib", "muvoffaqiyatli", "foydali"],
    "harakat": ["bilim oling", "kitob o‘qing", "o‘rganing"]
}
ILM_EMOJILAR = ["📚", "✍️", "🌞", "🧠"]

# Qur’on oyatlari va Hadislar (bold formatda)
NAMOZ_OYATLARI = [
    "**‘Bas, Meni eslang, Men ham sizlarni eslayman.’ (Surah Al-Baqara, 2:152)**",
    "**‘Imon keltirganlarning qalblari Allohning zikri bilan tinchlanadi.’ (Surah Ar-Ra’d, 13:28)**",
    "**‘Namozni ado et. Namoz yomonlik va buzuq ishlardan qaytaradi.’ (Surah Al-Ankabut, 29:45)**",
    "**‘Meni eslash uchun namoz o‘qi.’ (Surah Taha, 20:14)**"
]
NAMOZ_HADISLARI = [
    "**‘Kim besh vaqt namozni o‘qisa, gunohlari daryoda yuvilgandek poklanadi.’ (Buxoriy)**",
    "**‘Namoz — har bir musulmon uchun nurdir.’ (Tirmiziy)**",
    "**‘Beshta narsa bor: ulardan biri namozni o‘z vaqtida o‘qish.’ (Muslim)**",
    "**‘Namoz — mo‘minning mi’roji.’ (Ahmad)**"
]

# Namoz vaqtlari
NAMOZ_VAQTLARI = {
    "Bomdod": time(6, 30),
    "Peshin": time(13, 00),
    "Asr": time(16, 30),
    "Shom": time(18, 15),
    "Xufton": time(19, 30)
}

# Har bir hisob uchun alohida last_response_time
last_response_times = {account["session_name"]: {} for account in ACCOUNTS}


# Tasodifiy javob generatsiya qilish
def generate_response(shablonlar, sozlar, emojilar, namoz_nomi=None, oyat_hadis=None):
    shablon = random.choice(shablonlar)
    sozlar_dict = {key: random.choice(values) for key, values in sozlar.items()}
    if namoz_nomi:
        sozlar_dict["namoz"] = namoz_nomi
    javob = shablon.format(**sozlar_dict)
    emoji = random.choice(emojilar)
    javob = f"{emoji} {javob}"
    if oyat_hadis:
        javob += f"\n\n{oyat_hadis}"
    return javob


def is_night_time():
    now = datetime.now().time()
    return now >= time(20, 0) or now <= time(6, 30)


def is_morning_study_time():
    now = datetime.now().time()
    return time(6, 30) <= now <= time(9, 30)


def get_current_namaz():
    now = datetime.now().time()
    for namoz, vaqt in NAMOZ_VAQTLARI.items():
        total_minutes = vaqt.hour * 60 + vaqt.minute + 20
        end_hour = total_minutes // 60 % 24  # Handle hour rollover
        end_minute = total_minutes % 60
        end_time = time(end_hour, end_minute)

        if vaqt <= now <= end_time:
            return namoz
    return None


# Har bir hisob uchun handler
def create_handler(client, session_name):
    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        chat_id = event.chat_id
        now = datetime.now()
        me = await client.get_me()

        if not event.is_private:
            return

        sender = await event.get_sender()
        if sender.id == me.id or (hasattr(sender, "bot") and sender.bot):
            return

        last_response_time = last_response_times[session_name]

        current_namaz = get_current_namaz()
        if current_namaz:
            oyat_yoki_hadis = random.choice(NAMOZ_OYATLARI + NAMOZ_HADISLARI)
            javob = generate_response(NAMOZ_SABLONLAR, NAMOZ_SOZLAR, NAMOZ_EMOJILAR, namoz_nomi=current_namaz,
                                      oyat_hadis=oyat_yoki_hadis)
            await event.respond(javob, parse_mode="md")
            print(f"[{session_name}] Namoz vaqti eslatmasi: {chat_id} ga yuborildi ({current_namaz})")
            return

        if is_morning_study_time():
            javob = generate_response(ILM_SABLONLAR, ILM_SOZLAR, ILM_EMOJILAR)
            await event.respond(javob)
            print(f"[{session_name}] Ilm olish vaqti javobi: {chat_id} ga yuborildi")
            return

        if is_night_time():
            javob = generate_response(KECHKI_SABLONLAR, KECHKI_SOZLAR, KECHKI_EMOJILAR)
            await event.respond(javob)
            print(f"[{session_name}] Kechki javob: {chat_id} ga yuborildi")
            return

        last_time = last_response_time.get(chat_id)
        if last_time:
            time_diff = (now - last_time).total_seconds() / 60
            if 5 <= time_diff <= 10:
                javob = generate_response(ODDIY_SABLONLAR, ODDIY_SOZLAR, ODDIY_EMOJILAR)
                await event.respond(javob)
                print(f"[{session_name}] 5-10 daqiqa kechikish javobi: {chat_id} ga yuborildi")
                last_response_time[chat_id] = now
        else:
            last_response_time[chat_id] = now

    return handler


# Har bir hisob uchun botni ishga tushirish
async def start_client(account):
    client = TelegramClient(account["session_name"], account["api_id"], account["api_hash"])
    create_handler(client, account["session_name"])
    print(f"[{account['session_name']}] Bot ishga tushdi...")
    await client.start(phone=account["phone"])
    await client.run_until_disconnected()


async def main():
    tasks = [start_client(account) for account in ACCOUNTS]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
