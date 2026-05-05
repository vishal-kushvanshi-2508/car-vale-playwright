


import time
from store_data_database import *
from car_url_open import *
from open_car_url_single_browser import *


def main():
    # # -------first operation-----------

    # fetch_kia_location_url_table data 
    car_url_list = fetch_cars_url_table()

    # # --------operatin 1 open car url in 5 browser--------------
    # # without thread
    # # open_car_page(list_data = car_url_list)

    # # with thread
    # run_thread_futures(car_url_list)

    
    # --------operatin 2 open car url is open in 5 tab inside  single browser  --------------
    # without thread
    open_url_single_browser(car_url_list)

    # # # with thread

    # run_thread_wise(car_url_list)










if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("time different  : ", end - start)