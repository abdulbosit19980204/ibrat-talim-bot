from telethon import TelegramClient, events, Button
from bot.data import TOKEN, API_ID, API_HASH, FILIALAR, YONALISHLAR, PRICES
from bot.buttons import (
    get_main_menu,
    get_filial_buttons,
    get_yonalish_buttons,
    get_fanlar_buttons,
    get_back_button,
    get_phone_button
)
from bot.api import (
    create_user,
    update_user_phone,
    get_price,
    get_filiallar,
    get_yonalishlar,
    get_chegirma,
    format_chegirmalar)

# Client yaratish
client = TelegramClient("ibrat_talim_bot", API_ID, API_HASH).start(bot_token=TOKEN)

# State va user ma'lumotlari
users = {}
user_states = {}


@client.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    """Start buyrug'ini qayta ishlash"""
    try:
        user_id = event.sender_id
        users[user_id] = {}
        user_states[user_id] = "waiting_for_name"
        is_created = create_user(username=event.sender.username, user_id=event.sender.id,
                                 name=event.sender.first_name, surname=event.sender.last_name,
                                 phone_number=event.sender.phone).get('id', None)
        if is_created is not None:
            await event.respond(
                "🔸 Assalomu alaykum, 🏆 Ibrat ta'lim o'quv markazining maxsus telegram botiga xush kelibsiz!"
            )
            # await event.respond(
            #     "1️⃣ Ism va Familiyangizni lotin alifbosida to'liq kiriting.\n\n(Masalan: Saidakbar Mehmonxo'jayev)"
            # )
        else:
            await event.respond(
                "Siz allaqachon botdan royxatdan otkansiz"
            )
    except Exception as e:
        print(f"Start handler error: {e}")


@client.on(events.NewMessage)
async def message_handler(event):
    """Barcha xabarlarni qayta ishlash"""
    try:
        user_id = event.sender_id
        message = event.raw_text.strip()
        # Ro'yxatdan o'tish jarayoni
        if user_states.get(user_id) == "waiting_for_name":
            users[user_id]["name"] = message
            user_states[user_id] = "waiting_for_phone"
            await event.respond(
                "2️⃣ 👨🏻‍💻 \"Shaxsiy kabinet\" ochish uchun raqamingizni tasdiqlashingiz lozim 👇",
                buttons=get_phone_button()
            )
            return

        if user_states.get(user_id) == "waiting_for_phone" and event.message.contact:
            users[user_id]["phone"] = event.message.contact.phone_number
            print(update_user_phone(user_id, event.message.contact.phone_number))
            user_states[user_id] = "registered"
            await event.respond(
                "🎉 Tabriklaymiz, Siz muvafaqqiyatli ro'yxatdan o'tdingiz!\n\n"
                "🎓 IBRAT TA'LIM o'quv markazini tanlab adashmadingiz.\n\n"
                "✅ Quyidagi bo'limlardan birini tanlang 👇",
                buttons=get_main_menu()
            )
            return

        if user_states.get(user_id) not in ["waiting_for_name", "waiting_for_phone"]:
            # Asosiy menyu
            if message == "📍 Filiallar":
                await event.respond(
                    "🏢 Ibrat Ta'lim filiallari",
                    buttons=get_filial_buttons(get_filiallar().keys())
                )

            elif message.startswith("📍") and "filiali" in message:
                filial_name = message[2:].replace(" filiali", "").strip()
                if filial_name in get_filiallar():
                    filial = get_filiallar()[filial_name]
                    await event.respond(
                        f"📍 {filial_name} filiali\n\n{filial['description']}\n\nManzil: {filial.get('manzil', '')}",
                        file=filial['rasm'], parse_mode="HTML",
                        buttons=get_back_button()
                    )

            elif message == "📚 Mavjud yo'nalishlar":
                await event.respond(
                    "📚 Quyidagi yo'nalishlardan birini tanlang:",
                    buttons=get_yonalish_buttons(get_yonalishlar().keys())
                )

            elif message in get_yonalishlar():
                await event.respond(
                    f"📚 {message} yo'nalishi bo'yicha fanlar:",
                    buttons=get_fanlar_buttons(get_yonalishlar()[message])
                )

            elif message.startswith("🖋 "):
                fan = message[2:].strip()
                price_data = {item['fan']['name']: item for item in get_price()}  # Dictionary formatiga o'tkazamiz
                for yonalish, fanlar in get_yonalishlar().items():
                    if fan in fanlar:
                        price_fan = price_data.get(fan, None)
                        if price_fan is not None:
                            price = price_data[fan].get('price', None)
                        else:
                            price = "Narxi korsatilmagan"
                        await event.respond(
                            f"✅ Siz {fan} kursiga yozildingiz.\n"
                            f"Narxi: {price}\n\n"
                            "Tez orada operatorlarimiz siz bilan bog'lanishadi.",
                            buttons=get_back_button()
                        )
                        break

            elif message == "💰 Kurs narxlari":
                narxlar_text = "💰 Kurs narxlari:\n\n"
                for i in get_price():
                    fan_nomi = i["fan"]["name"]  # Fan nomini to'g'ri olish
                    narx = i["price"]
                    izoh = i["comment"] if "comment" in i else ""

                    narxlar_text += f"📌 <b>{fan_nomi}</b>: <i>{narx}</i> UZS\n{izoh}\n\n"

                await event.respond(narxlar_text, parse_mode="HTML", buttons=get_back_button())

            elif message == "🎁 Chegirmalar":
                # Foydalanish
                chegirmalar = get_chegirma()
                chegirmalar_text = format_chegirmalar(chegirmalar)

                await event.respond(chegirmalar_text, parse_mode="HTML", buttons=get_back_button())

            elif message == "🔙 Ortga":
                await event.respond("🏠 Asosiy menyu", buttons=get_main_menu())

        else:
            await event.respond("❗ Iltimos, avval ro'yxatdan o'ting.")

    except Exception as e:
        print(f"Message handler error: {e}")
        await event.respond(
            "⚠️ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring yoki /start buyrug'ini yuboring.",
            buttons=get_back_button()
        )


def main():
    """Botni ishga tushirish"""
    try:
        print("Bot ishga tushdi...")
        print("Bot username: @ibrat_talim_bot")
        client.run_until_disconnected()
    except Exception as e:
        print(f"Bot ishga tushishda xatolik: {e}")


if __name__ == "__main__":
    main()
