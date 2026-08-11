import json
import os
import random

memory_file = "memory.json"

# حافظه
if os.path.exists(memory_file):
    with open(memory_file, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

def save():
    with open(memory_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)

print("🤖 Rayan AI روشن شد!")
print("برای خروج بنویس: exit")

while True:
    text = input("\nتو: ").lower()

    if text == "exit":
        print("AI: خداحافظ داداش 👋")
        break

    # یادگیری اسم
    if "اسم من" in text:
        name = text.replace("اسم من", "").strip()
        memory["name"] = name
        save()
        print("AI: یاد گرفتم 😎 اسمت رو ذخیره کردم!")
    
    elif "اسمم چیه" in text:
        if "name" in memory:
            print("AI: اسم تو " + memory["name"] + " هست 😁")
        else:
            print("AI: هنوز اسمت رو نمی‌دونم 🤔")

    elif "سلام" in text:
        answers = [
            "سلام داداش 😎",
            "سلام! آماده‌ام 🤖",
            "سلام رفیق 🔥"
        ]
        print("AI:", random.choice(answers))

    elif "خوبی" in text:
        print("AI: عالی‌ام! ممنون که پرسیدی 😁")

    elif "سازنده" in text:
        print("AI: من توسط یک برنامه‌نویس پایتونی ساخته شدم 🐍")

    elif "پایتون" in text:
        print("AI: پایتون یک زبان برنامه‌نویسی قدرتمند است 🐍")

    elif "خداحافظ" in text:
        print("AI: خداحافظ 👋")

    elif "بازی" in text:
        print("AI: بازی‌های کامپیوتری خیلی جذاب هستند 🎮")

    elif "کامپیوتر" in text:
        print("AI: کامپیوتر از سخت‌افزار و نرم‌افزار ساخته شده 💻")

    else:
        print("AI: هنوز اینو یاد نگرفتم، ولی می‌تونیم به من اضافه کنیم 🧠")
        