from telethon import TelegramClient, events, Button

filialar = ['Islomobod', 'Saddatagi', 'Xortum']
filialar1 = {
    "Islomobod": {
        "description": "Islomobod filialimiz so'ngi ochilgan filliallardan bo'lishiga qaramasdan koplab o'quvchilarimiz IELTS dan yuqori ballarni olishga ulgurdi",
        "rasm": "https://avatars.mds.yandex.net/get-altay/11408080/2a00000190a1fdfcab203b5bb96deafb805c/L_height"
    },
    "Saddatagi": {
        "description": "Saddatagi filiali Bizni eng avvalgi filialimiz.",
        "rasm": "https://www.gazeta.uz/media/img/2023/02/ccWzM216753387489084_b.jpg"
    }
}
yonalishlar = [
    {"Xorijiy Tillar": ["Ingiliz", "Rus", "Koreys", "Nemis"]},
    {"Aniq Fanlar": ["Matematika", "Fizika"]},
    {"Tabiy Fanlar": ["Kimyo", "Biologiya"]},
    {"Zamonaviy Fanlar": ["Kompyuter Savodxonligi", "Mobilografiya | SMM", "Grafik Dizayn", "Dasturlash"]}

]
yonalishlar1 = {
    "Xorijiy Tillar": ["Ingiliz", "Rus", "Koreys", "Nemis"],
    "Aniq Fanlar": ["Matematika", "Fizika"],
    "Tabiy Fanlar": ["Kimyo", "Biologiya"],
    "Zamonaviy Fanlar": ["Kompyuter Savodxonligi", "Mobilografiya | SMM", "Grafik Dizayn", "Dasturlash"],

}
prices = {
    "Xorijiy Tillar": "250 000 so'm",
    "Aniq Fanlar": "250 000 so'm",
    "Tabiy Fanlar": "250 000 so'm",
    "Zamonaviy Fanlar": "500 000 so'm",
}
# Telegram API ma'lumotlari
api_id = "27668593"
api_hash = "db44de3510fb53c30375bfce090989d9"
# bot_token = "6189703946:AAGb1TA2yDg-sdu0c_AIDn39_07AuzvlZgE"
bot_token = "7740531471:AAHckXn4OvZ0kLbTuWWSxfQ3xyYBZhO0zoM"

client = TelegramClient("ibrat_talim_bot", api_id, api_hash).start(bot_token=bot_token)

# Foydalanuvchi ma'lumotlari
users = {}
user_states = {}

# Asosiy menyu
main_menu_buttons = [
    [Button.text("📍 Filiallar", resize=True), Button.text("📚 Mavjud yo'nalishlar", resize=True)],
    [Button.text("💰 Kurs narxlari", resize=True), Button.text("🎁 Chegirmalar", resize=True)]
]


@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    user_id = event.sender_id
    users[user_id] = {}
    user_states[user_id] = "waiting_for_name"

    await event.respond("🔸 Assalomu alaykum, 🏆 Ibrat ta'lim o'quv markazining maxsus telegram botiga xush kelibsiz!")

    await event.respond(
        "1️⃣ Ism va Familiyangizni lotin alifbosida to’liq kiriting.\n\n(Masalan: Saidakbar Mehmonxo'jayev)")


@client.on(events.NewMessage)
async def collect_info(event):
    user_id = event.sender_id
    message = event.raw_text.strip()
    print(message)
    if user_states.get(user_id) == "waiting_for_name":
        users[user_id]["name"] = message
        user_states[user_id] = "waiting_for_phone"

        await event.respond("2️⃣ 👨🏻‍💻 \"Shaxsiy kabinet\" ochish uchun raqamingizni tasdiqlashingiz lozim 👇",
                            buttons=[Button.request_phone("📞 Telefon raqamni yuborish", resize=True)]
                            )
        return

    if user_states.get(user_id) == "waiting_for_phone" and event.message.contact:
        users[user_id]["phone"] = event.message.contact.phone_number
        user_states[user_id] = "registered"

        await event.respond("🎉 Tabriklaymiz, Siz muvafaqqiyatli ro'yxatdan o'tdingiz!\n\n"
                            "🎓 IBRAT TA'LIM o'quv markazini tanlab adashmadingiz.\n\n"
                            "✅ Quyidagi bo‘limlardan birini tanlang 👇",
                            buttons=main_menu_buttons
                            )
        return

    if user_states.get(user_id) in ["waiting_for_name", "waiting_for_phone"]:
        await event.respond("❗ Iltimos, avval so‘ralgan ma'lumotni kiriting.")
        return

    # 📍 **Filiallar**
    if message == "📍 Filiallar":
        buttons = []
        for i in filialar:
            buttons.append(Button.text("📍" + i + " filiali ", resize=True))
        await event.respond("🏢 Ibrat Ta'lim filiallari", buttons=[
            buttons,
            [Button.text("📍 Islomobod filiali", resize=True), Button.text("📍 Saddatagi filiali", resize=True)],
            [Button.text("🔙 Ortga", resize=True)]
        ])
    elif message in filialar1:

    elif message == "📍 Islomobod filiali":
        await event.respond("📍 Islomobod filiali manzili: ...\n\n[Rasm](https://example.com/islomobod.jpg)")

    elif message == "📍 Saddatagi filiali":
        await event.respond("📍 Saddatagi filiali manzili: ...\n\n[Rasm](https://example.com/saddatagi.jpg)")


    # 📚 **Mavjud yo'nalishlar**
    elif message == "📚 Mavjud yo'nalishlar":
        yonalish_btn_list = []
        for y in yonalishlar:
            for i in y:
                yonalish_btn_list.append(Button.text(i, resize=True))
        await event.respond("📚 Quyidagi yo‘nalishlardan birini tanlang:", buttons=[
            [Button.text("🗣 Xorijiy tillar", resize=True), Button.text("🧑🏻‍💻 Zamonaviy kasblar", resize=True)],
            [Button.text("🟡 Aniq fanlar", resize=True), Button.text("🟡 Tabiiy fanlar", resize=True)],
            yonalish_btn_list,
            [Button.text("🔙 Ortga", resize=True)]
        ])
    elif message in yonalishlar1:
        print(yonalishlar1[message])
        buttons = []
        for i in yonalishlar1[message]:
            buttons.append(Button.text("🟡 " + i))
        await event.respond("🗣 Qaysi tilni o‘rganmoqchisiz?", buttons=[
            buttons,
            [Button.text("🔙 Ortga", resize=True)]
        ])
    elif message == "🗣 Xorijiy tillar":
        await event.respond("🗣 Qaysi tilni o‘rganmoqchisiz?", buttons=[
            [Button.text("🇬🇪 Ingliz tili"), Button.text("🇷🇺 Rus tili")],
            [Button.text("🇰🇷 Koreys tili"), Button.text("🇩🇪 Nemis tili")],
            [Button.text("🔙 Ortga", resize=True)]
        ])

    elif message in ["🇬🇪 Ingliz tili", "🇷🇺 Rus tili", "🇰🇷 Koreys tili", "🇩🇪 Nemis tili"]:
        await event.respond("✅ Siz muvafaqqiyatli ro'yxatdan o'tdingiz, tez orada aloqaga chiqamiz!")

    elif message == "🧑🏻‍💻 Zamonaviy kasblar":
        await event.respond("🧑🏻‍💻 Qaysi kasbni tanlamoqchisiz?", buttons=[
            [Button.text("🔸 Kompyuter savodxonligi"), Button.text("🔸 Dasturlash")],
            [Button.text("🔸 Grafik dizayn"), Button.text("🔸 Mobilografiya")],
            [Button.text("🔙 Ortga", resize=True)]
        ])

    elif message in ["🔸 Kompyuter savodxonligi", "🔸 Dasturlash", "🔸 Grafik dizayn", "🔸 Mobilografiya"]:
        await event.respond("✅ Siz muvafaqqiyatli ro'yxatdan o'tdingiz, tez orada aloqaga chiqamiz!")

    # 💰 **Kurs narxlari**
    elif message == "💰 Kurs narxlari":
        await event.respond("💰 Kurs narxlari:\n\n"
                            "1️⃣ Boshlang'ich daraja – 250 ming so'm\n"
                            "2️⃣ IELTS va CEFR – 400 ming so'm\n"
                            "3️⃣ Kompyuter savodxonligi – 250 ming so'm\n"
                            "4️⃣ Dasturlash va Grafik dizayn – 500 ming so'm",
                            buttons=[[Button.text("🔙 Ortga", resize=True)]]
                            )

    # 🎁 **Chegirmalar**
    elif message == "🎁 Chegirmalar":
        await event.respond("🎁 Chegirmalar:\n\n"
                            "🔹 Bitta oiladan 2 va undan ortiq farzandlar uchun – 20% doimiy chegirma\n"
                            "🔹 Kursni endigina boshlayotganlar uchun – 20% birinchi oy uchun chegirma",
                            buttons=[[Button.text("🔙 Ortga", resize=True)]]
                            )

    elif message == "🔙 Ortga":
        await event.respond("🏠 Asosiy menyu", buttons=main_menu_buttons)


client.run_until_disconnected()
