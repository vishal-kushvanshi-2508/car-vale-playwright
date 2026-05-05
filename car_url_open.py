

from playwright.sync_api import sync_playwright

def car_url_open(list_data, max_page=5):

    print(len(list_data))


    with sync_playwright() as f:
        browser = f.chromium.launch(headless=False)
        new_window = browser.new_context()

        page_list = [new_window.new_page() for i in range(max_page)]
        print(page_list)

        for i in range(0, len(list_data), max_page):
            batch = list_data[i: i+ max_page]

            for index, data in enumerate(batch):
                car_url = data.get("car_url")
                print("open car url : ", car_url)
                page_list[index].goto(car_url, wait_until="commit", timeout=60000)

        browser.close()

