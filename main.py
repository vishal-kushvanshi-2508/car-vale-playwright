


from databases import *
from car_url_open import *
from multi_browser_in_multi_tab import *

import time


def main():
    print("-----------main---------------")

    # fetch car url 
    car_url_list = fetch_car_url()

    # # ------------operation 1 (open url in 5 tab inside single browser)------------------------
    # # open car url in browser 
    # car_url_open(list_data=car_url_list)

    # ------------operation 2 (open url in 5 tab inside every browser like 5)------------------------

    run_url_thread_wise(car_url_list)

    






start_time = time.time()

main()

print("time different : " , time.time() - start_time)

