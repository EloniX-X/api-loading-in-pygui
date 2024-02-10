import dearpygui.dearpygui as dpg
from threading import Thread
import time
import requests
import time

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

threadingcompletedquestionmark = False

def timer(): 
    global threadingcompletedquestionmark
    start_time = time.time()
    url = 'http://127.0.0.1:5000/test'
    response = requests.get(url)
    end_time = time.time() - start_time
    print(end_time)
    threadingcompletedquestionmark = True
    

#start counting
#start thread
#join once threads over 
#stop counting

def hello(): 
    global thread_completed
    print("hi")
    i = 0
    t1 = Thread(target=timer)
    t1.start()
    while threadingcompletedquestionmark == False:
   #     print("im coming in transit")
      #  time.sleep(1)
      #  i += 1
        dpg.set_value("lol", "im coming in transit") 
    else:
        dpg.set_value("lol", "ok we're done") 



with dpg.window(label="Example Window", width=300, height=400):
    dpg.add_text("heyyy", tag="lol")
    dpg.add_button(label="hey", callback=hello)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()