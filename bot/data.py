# config.py
from bot.api import get_filiallar, get_yonalishlar

TOKEN = "7740531471:AAHckXn4OvZ0kLbTuWWSxfQ3xyYBZhO0zoM"
API_ID = "27668593"
API_HASH = "db44de3510fb53c30375bfce090989d9"
PHONE = +998999992334
ACCOUNTS = [
    {
        "session_name": "session1",
        "api_id": "",
        "api_hash": "",
        "phone": ""
    },
    {
        "session_name": "session_name",
        "api_id": "",
        "api_hash": "",
        "phone": ""
    },

    # Yana hisob qo‘shmoqchi bo‘lsangiz, shu tarzda davom ettiring
]
# Bot ma'lumotlari
FILIALAR = get_filiallar()
# FILIALAR = {
#     "Islomobod": {
#         "description": "Islomobod filialimiz so'ngi ochilgan filliallardan bo'lishiga qaramasdan koplab o'quvchilarimiz IELTS dan yuqori ballarni olishga ulgurdi",
#         "rasm": "https://avatars.mds.yandex.net/get-altay/11408080/2a00000190a1fdfcab203b5bb96deafb805c/L_height",
#         "manzil": "Islomobod filiali manzili..."
#     },
#     "Saddatagi": {
#         "description": "Saddatagi filiali Bizni eng avvalgi filialimiz.",
#         "rasm": "https://www.gazeta.uz/media/img/2023/02/ccWzM216753387489084_b.jpg",
#         "manzil": "Saddatagi filiali manzili..."
#     }
# }
YONALISHLAR = get_yonalishlar()

# YONALISHLAR = {
#     "🗣Xorijiy Tillar": ["🏴󠁧󠁢󠁥󠁮󠁧󠁿Ingiliz", "🇷🇺Rus", "🇰🇷Koreys", "🇩🇪Nemis"],
#     "📚Aniq Fanlar": ["➕Matematika", "⚡Fizika"],
#     "📚Tabiy Fanlar": ["🧪Kimyo", "🐍Biologiya"],
#     "💻Zamonaviy Fanlar": ["Kompyuter Savodxonligi", "Mobilografiya | SMM", "Grafik Dizayn", "Dasturlash"]
# }

PRICES = {
    "🗣Xorijiy Tillar": "\n Boshlang'ich daraja – 250 ming so'm\n"
                       " IELTS va CEFR – 400 ming so'm\n",
    "📚Aniq Fanlar": "250 000 so'm",
    "📚Tabiy Fanlar": "250 000 so'm",
    "💻Zamonaviy Fanlar": "\n Kompyuter savodxonligi – 250 ming so'm\n"
                         " Dasturlash va Grafik dizayn – 500 ming so'm",

}
