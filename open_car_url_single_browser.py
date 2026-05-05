
from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor, as_completed


def open_url_single_browser(car_url_list, max_tabs=5):
    print("-------------open_url_single_browser----------------")

    with sync_playwright() as f:
        browser  = f.chromium.launch(headless=False)
        context = browser.new_context()

        # Create fixed number of tabs
        pages = [ context.new_page() for i in range(max_tabs)]

        for i in range(0, len(car_url_list), max_tabs):

            batch = car_url_list[i:i + max_tabs]

            print(f"\nProcessing batch {i} → {i+len(batch)}")

            # Open all URLs in parallel tabs
            for j, data in enumerate(batch):
                url = data.get("car_url")
                print("Opening:", url)

                pages[j].goto(url, timeout=60000, wait_until="commit")

        browser.close()















# def open_url_single_browser(car_url_list, page):
#     print("-------------open_url_single_browser----------------")

#     # with sync_playwright() as f:
#     #     browser  = f.chromium.launch(headless=False)
#     #     context = browser.new_context()

#     # Create fixed number of tabs
#     # pages = context.new_page()

#     for data in car_url_list:
#         url = data.get("car_url")
#         print("Opening:", url)

#         page.goto(url, timeout=60000, wait_until="commit")


#     # pages = [ context.new_page() for i in range(max_tabs)]

#     # for i in range(0, len(car_url_list), max_tabs):

#     #     batch = car_url_list[i:i + max_tabs]

#     #     print(f"\nProcessing batch {i} → {i+len(batch)}")

#     #     # Open all URLs in parallel tabs
#     #     for j, data in enumerate(batch):
#     #         url = data.get("car_url")
#     #         print("Opening:", url)

#     #         pages[j].goto(url, timeout=60000, wait_until="commit")

#     # pages.close()



# def chunk_wise(cat_data, chunk_size):
#     print("-------------chunk_wise----------------")
#     for i in range(0, len(cat_data), chunk_size):
#         yield cat_data[i: i+chunk_size]

# def run_thread_wise(car_url_list, max_thread= 4):
#     with sync_playwright() as f:
#         browser = f.chromium.launch(headless=False)
#         context = browser.new_context()

#         chunk_size = len(car_url_list)//max_thread or 1

#         chunk_data_list = list(chunk_wise(car_url_list, chunk_size))
#         print(chunk_data_list)
#         print(len(chunk_data_list))
#         print("chunk_size : ", chunk_size)


#         pages = [context.new_page() for i in range((max_thread+1))]

#         print("pages : ", pages)
#         print("pages : ", len(pages))

        


#         with ThreadPoolExecutor(max_workers=max_thread) as execute:

#             futures = [
#                 execute.submit(open_url_single_browser, chunk, pages[index])
#                 for index, chunk in enumerate(chunk_data_list)
#             ]


#             for future in futures:
#                 try:
#                     future.result()
#                 except Exception as e:
#                     print("thread error : ", e)

#         print("Thread end")



#         # browser.close()












