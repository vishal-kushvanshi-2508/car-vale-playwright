



from playwright.sync_api import sync_playwright

def capture_main_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        def handle_response(response):
            try:
                # 👉 only main document request
                if (
                    response.url == "https://www.flipkart.com/"
                    and response.request.resource_type == "document"
                ):
                    print("\n✅ Found main HTML response\n")

                    html = response.text()   # 👈 get HTML content
                    print(html[:2000])       # print first 2000 chars (avoid huge output)

            except Exception as e:
                print("Error:", e)

        # 🔴 attach before navigation
        page.on("response", handle_response)

        page.goto("https://www.flipkart.com/", wait_until="load")

        page.wait_for_timeout(5000)

        browser.close()

capture_main_html()