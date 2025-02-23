from telethon import TelegramClient, events
import random
from datetime import datetime, time

# API ma'lumotlarni shu yerga qo‘ying
API_ID = "SIZNING_API_ID"
API_HASH = "SIZNING_API_HASH"
PHONE = "SIZNING_TEL_RAQAMINGIZ"
from bot.data import PHONE, API_ID, API_HASH

client = TelegramClient("session_name", API_ID, API_HASH)

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

NAMOZ_SABLONLAR = [
    "{namoz} vaqti {holat}, {eslatma}!",
    "Hozir {namoz} vaqti, {eslatma} qilib oling.",
    "{eslatma} — {namoz} vaqti {holat}!"
]
NAMOZ_SOZLAR = {
    "holat": ["kirib keldi", "bo‘ldi", "yaqinlashdi"],
    "eslatma": ["Robbingizni eslang", "vaqtni boy bermang", "yuragingizni yoriting"]
}

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
    "Bomdod": time(5, 0),
    "Peshin": time(12, 30),
    "Asr": time(16, 30),
    "Shom": time(18, 30),
    "Xufton": time(20, 00)
}

last_response_time = {}


# Tasodifiy javob generatsiya qilish
def generate_response(shablonlar, sozlar, namoz_nomi=None, oyat_hadis=None):
    shablon = random.choice(shablonlar)
    sozlar_dict = {key: random.choice(values) for key, values in sozlar.items()}
    if namoz_nomi:
        sozlar_dict["namoz"] = namoz_nomi
    javob = shablon.format(**sozlar_dict)
    if oyat_hadis:
        javob += f"\n\n{oyat_hadis}"
    return javob


def is_night_time():
    now = datetime.now().time()
    return now >= time(20, 0) or now <= time(9, 30)


def get_current_namaz():
    now = datetime.now().time()
    for namoz, vaqt in NAMOZ_VAQTLARI.items():
        end_time = time(vaqt.hour, vaqt.minute + 20)
        if vaqt.hour == 23 and vaqt.minute + 20 >= 60:
            end_time = time(0, (vaqt.minute + 20) % 60)
        if vaqt <= now <= end_time:
            return namoz
    return None


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

    current_namaz = get_current_namaz()
    if current_namaz:
        oyat_yoki_hadis = random.choice(NAMOZ_OYATLARI + NAMOZ_HADISLARI)
        javob = generate_response(NAMOZ_SABLONLAR, NAMOZ_SOZLAR, namoz_nomi=current_namaz, oyat_hadis=oyat_yoki_hadis)
        await event.respond(javob, parse_mode="md")
        print(f"Namoz vaqti eslatmasi: {chat_id} ga yuborildi ({current_namaz})")
        return

    if is_night_time():
        javob = generate_response(KECHKI_SABLONLAR, KECHKI_SOZLAR)
        await event.respond(javob)
        print(f"Kechki javob: {chat_id} ga yuborildi")
        return

    last_time = last_response_time.get(chat_id)
    if last_time:
        time_diff = (now - last_time).total_seconds() / 60
        if 5 <= time_diff <= 10:
            javob = generate_response(ODDIY_SABLONLAR, ODDIY_SOZLAR)
            await event.respond(javob)
            print(f"5-10 daqiqa kechikish javobi: {chat_id} ga yuborildi")
            last_response_time[chat_id] = now
    else:
        last_response_time[chat_id] = now


async def main():
    print("Bot ishga tushdi...")
    await client.start(phone=PHONE)
    await client.run_until_disconnected()


if __name__ == "__main__":
    client.loop.run_until_complete(main())
