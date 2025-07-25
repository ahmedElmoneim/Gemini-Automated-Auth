from playwright.sync_api import sync_playwright
import os
import json

profile_path = os.path.expanduser("~/playwright-google-profile")
with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir=profile_path,
        headless=False,
        args=[
            "--start-maximized",
            "--disable-blink-features=AutomationControlled"
        ]
    )
  
    page = context.new_page()
    page.goto("https://accounts.google.com")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cookies_path = os.path.join(script_dir, "cookies.json")
        # حفظ الكوكيز بعد تسجيل الدخول
    cookies = context.cookies()
    with open(cookies_path, "w") as f:
        json.dump(cookies, f, indent=2)
        # حفظ الstorage (يشمل الكوكيز)

    
    storage_path = os.path.join(script_dir, "storage.json")
    context.storage_state(path="storage.json")
    input("سجّل دخولك يدويًا، بعدين اضغط Enter.")
    
    #after that you can use this commend : cd [code path]
    #after that you can use this commend : playwright codegen --load-storage=storage.json https://gemini.google.com/app