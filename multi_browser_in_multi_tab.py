

from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def multi_browser_in_multi_tab(chunk, max_tab=5):
    # print("----------multi_browser_in_multi_tab-----------------")
    print("chunk lenght : ", len(chunk) )

    with sync_playwright() as f:
        browser = f.chromium.launch(headless=False)
        new_cotext = browser.new_context()
        pages = [ new_cotext.new_page()  for i in range(max_tab)]

        for i in range(0, len(chunk), max_tab):
            batch = chunk[i:i+max_tab]
            
            for index, data in enumerate(batch):
                car_url = data.get("car_url")
                print("open car url : ", car_url)
                pages[index].goto(car_url, timeout=120000, wait_until="domcontentloaded")

        browser.close()



def data_into_chunk(car_url_list, chunk_size):
    # print("----------data_into_chunk-----------------")


    for i in range(0, len(car_url_list), chunk_size):
        yield car_url_list[i:i+chunk_size]


def run_url_thread_wise(car_url_list, max_thread=5):
    print("----------run_url_thread_wise-----------------")

    chunk_size = ( len(car_url_list) // max_thread ) + 1

    print("data is : ", chunk_size)

    chunk_data = list(data_into_chunk(car_url_list, chunk_size))

    with ThreadPoolExecutor(max_workers=max_thread) as executer:
        futures = [
            executer.submit(multi_browser_in_multi_tab, chunk)
            for chunk in chunk_data
        ]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print("Thread error:", e)
    print("process done....")








