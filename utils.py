"""Talaba Yordamchisi uchun hisoblash funksiyalari."""

FACTORS_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}

def calculate_average(grades):
    """Baholar ro‘yxatining o‘rtacha qiymatini qaytaradi."""
    if not grades:
        raise ValueError("Baholar ro‘yxati bo‘sh bo‘lmasligi kerak.")
    return sum(grades) / len(grades)

def calculate_percentage(number, percent):
    """Sonning berilgan foizini hisoblaydi."""
    return number * percent / 100

def convert_length(value, source, target):
    """Uzunlikni mm, cm, m yoki km birliklari orasida aylantiradi."""
    if source not in FACTORS_TO_METERS or target not in FACTORS_TO_METERS:
        raise ValueError("Noto‘g‘ri uzunlik birligi.")
    meters = value * FACTORS_TO_METERS[source]
    return meters / FACTORS_TO_METERS[target]
