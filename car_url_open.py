

from playwright.sync_api import sync_playwright
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# ----------opne and close browser chunck wise (total browser open and close 5) and open url in single page-----------------

def open_car_page(list_data :list):

    with sync_playwright() as f:
        browser = f.firefox.launch(headless=False)
        page =  browser.new_page()


        for data in list_data:
            id = data.get("id")
            car_name = data.get("car_name")
            car_url = data.get("car_url")
            print("car detail : ", id , ",car_name : ", car_name, ",car_url : ", car_url)

            page.goto(car_url, timeout=60000, wait_until="domcontentloaded")
            # time.sleep(20)
            # page.wait_for_load_state("domcontentloaded")  # faster than full load
        page.close()

        browser.close()


def chunk_data(data, chunk_size):
    print("-------chunk_data------------")
    for i in range(0, len(data), chunk_size):
        yield data[i:i+chunk_size]


def run_thread_futures(car_url_list, max_threads=5):
    chunk_size = len(car_url_list) // max_threads or 1

    chunks = list(chunk_data(car_url_list, chunk_size))
    
    # print(len(chunks))
    
    with ThreadPoolExecutor(max_workers=max_threads) as f:
        futures = [
            f.submit(open_car_page, list_data=chunk)
            for chunk in chunks
        ]

        for future in futures:
            try:
                future.result()
            except Exception as e:
                print("thread error : ", e)

    print("Thread end")









# # ----------opne and close browser for every car url-----------------

# def open_car_page(list_data :list):


#     for data in list_data:
#         id = data.get("id")
#         car_name = data.get("car_name")
#         car_url = data.get("car_url")
#         print("\ncar detail : ", id , car_name, car_url)

#         with sync_playwright() as f:
#             browser = f.firefox.launch(headless=False)
#             page =  browser.new_page()
#             page.goto(car_url)
#             # time.sleep(20)

#             browser.close()


# def run_thread_futures(car_url_list, max_threads=5):
#     # print(car_url_list)
#     # print(len(car_url_list))
    
#     with ThreadPoolExecutor(max_workers=max_threads) as f:
#         futures = [
#             f.submit(open_car_page, [dict_data])
#             for dict_data in car_url_list
#         ]

#         for future in futures:
#             try:
#                 future.result()
#             except Exception as e:
#                 print("thread error : ", e)

#     print("Thread end")

