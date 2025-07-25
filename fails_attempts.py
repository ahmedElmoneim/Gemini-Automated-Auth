from playwright.sync_api import sync_playwright
import os
import json

profile_path = os.path.expanduser("~/playwright-google-profile")  # بروفايل جديد مش مستخدم

# with sync_playwright() as p:

#     context = p.chromium.launch_persistent_context(
#         user_data_dir="/Users/ahmedel-moneim/Library/Application Support/Google/Chrome/Profile 2",
#         headless=False,
#         args=[
#             "--start-maximized",
#             "--disable-blink-features=AutomationControlled"
#         ]
#     )
  
#     page = context.new_page()
#     page.goto("https://accounts.google.com")

    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # cookies_path = os.path.join(script_dir, "cookies.json")
#         # حفظ الكوكيز بعد تسجيل الدخول
#     cookies = context.cookies()
#     with open(cookies_path, "w") as f:
#         json.dump(cookies, f, indent=2)
#     input("سجّل دخولك يدويًا، بعدين اضغط Enter.")



# with sync_playwright() as p:
#     browser = p.chromium.launch_persistent_context(
#         user_data_dir=profile_path,
#         headless=False,
#         args=["--start-maximized"]
#     )
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # cookies_path = os.path.join(script_dir, "cookies.json")
    # with open(cookies_path, "r") as f:
    #     cookies = json.load(f)
    # browser.add_cookies(cookies)

#     page = browser.new_page()
#     page.goto("https://accounts.google.com")

#     input("سجّل دخولك في المتصفح يدويًا، وبعدين اضغط Enter علشان يكمل السكربت...")

# with sync_playwright() as p:
#     context = p.chromium.launch_persistent_context(
#         user_data_dir="~/playwright-profile",
#         headless=False,
#         args=["--disable-blink-features=AutomationControlled"]
#     )

#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     cookies_path = os.path.join(script_dir, "cookies.json")
#     with open(cookies_path, "r") as f:
#         cookies = json.load(f)
#     context.add_cookies(cookies)
#     page = context.pages[0] if context.pages else context.new_page()
    
#     page.goto("https://accounts.google.com")
#     input("🔐 سجّل دخولك يدويًا، واضغط Enter بعدها...")

#     context.storage_state(path="storage.json")
#     input("pess enter to end")  # انتظر تحميل الصفحة

from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=os.path.expanduser("~/playwright-google-profile"),
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    page = context.pages[0] if context.pages else context.new_page()

    # بدء تسجيل التتبع
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page.goto("https://gemini.google.com/app")

    input("سجّل دخولك أو نفّذ أي شيء يدوي، ثم اضغط Enter عشان نوقف التسجيل...")

    # حفظ ملف التتبع
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    context.tracing.stop(path=os.path.join(script_dir, "trace.zip"))
    print("✅ تم حفظ التتبع في trace.zip")
    context.close()
