import asyncio
from pyrogram import Client
import logging
import os

# تنظیمات API تلگرام (از محیط بخونه یا داخل بنویس)
api_id = int(os.getenv("API_ID", "1368896"))  # عددی از my.telegram.org
api_hash = os.getenv("API_HASH", "ea02589c74400a5f4b5a49b12912a3bc")  # هش از همون جا

# لاگ ساده فارسی
logging.basicConfig(level=logging.INFO, format="📍 %(message)s")

# ایموجی‌های قابل استفاده
emoji_dict = {
    "🎲": "تاس (۱ تا ۶)",
    "🎯": "دارت (۱ تا ۶)",
    "🎰": "دستگاه شانس (برد = ۶۴)",
    "⚽": "فوتبال (گل = ۲)",
    "🏀": "بسکتبال (گل = ۲)",
    "🎳": "بولینگ (استرایک = ۶؟)"
}

async def main():
    print("🎮 ربات تلگرام - تاس تقلبی با اکانت شخصی\n")
    print("ایموجی مورد نظر رو انتخاب کن:")

    for emoji, desc in emoji_dict.items():
        print(f"{emoji} - {desc}")

    emoji = input("\n📌 ایموجی دلخواه رو وارد کن (مثلاً 🎯): ").strip()
    if emoji not in emoji_dict:
        print("❌ ایموجی واردشده پشتیبانی نمی‌شود.")
        return

    try:
        desired = int(input("🎯 عدد هدف چیه؟ (مثلاً ۶): ").strip())
    except ValueError:
        print("❌ لطفاً عدد معتبر وارد کن.")
        return

    chat_id = input("📩 آیدی چت یا گروه رو وارد کن (مثلاً @MyGroup یا عدد): ").strip()

    print("\n▶️ شروع ارسال ایموجی تا رسیدن به عدد هدف...\n")

    async with Client("my_account", api_id, api_hash) as app:
        while True:
            try:
                msg = await app.send_dice(chat_id, emoji=emoji)
                val = msg.dice.value
                logging.info(f"نتیجه: {val}")
                if val == desired:
                    logging.info("✅ به عدد هدف رسیدیم!")
                    break
                await asyncio.sleep(2)
            except Exception as e:
                logging.error(f"❌ خطا: {e}")
                logging.info("⏳ تلاش مجدد تا چند ثانیه دیگر...")
                await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())