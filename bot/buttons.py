# keyboards.py
from telethon import Button


def get_main_menu():
    return [
        [Button.text("📍 Filiallar", resize=True), Button.text("📚 Mavjud yo'nalishlar", resize=True)],
        [Button.text("💰 Kurs narxlari", resize=True), Button.text("🎁 Chegirmalar", resize=True)]
    ]


def get_filial_buttons(filiallar):
    buttons = []
    row = []
    for filial in filiallar:
        row.append(Button.text(f"📍 {filial} filiali", resize=True))
        if len(row) == 3:  # Har qatorda 3 ta tugma
            buttons.append(row)
            row = []
    if row:  # Agar oxirgi qator to'liq bo'lmasa
        buttons.append(row)
    buttons.append([Button.text("🔙 Ortga", resize=True)])
    return buttons


def get_yonalish_buttons(yonalishlar):
    buttons = []
    row = []
    for yonalish in yonalishlar:
        row.append(Button.text(yonalish, resize=True))
        if len(row) == 3:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([Button.text("🔙 Ortga", resize=True)])
    return buttons


def get_fanlar_buttons(fanlar):
    buttons = []
    row = []
    for fan in fanlar:
        row.append(Button.text(f"{fan}", resize=True))
        if len(row) == 3:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([Button.text("🔙 Ortga", resize=True)])
    return buttons


def get_back_button():
    return [[Button.text("🔙 Ortga", resize=True)]]


def get_phone_button():
    return [Button.request_phone("📞 Telefon raqamni yuborish", resize=True)]
