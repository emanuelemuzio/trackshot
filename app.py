import tkinter as tk
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


if(len(sys.argv) > 1):
    f = open(sys.argv[1])
    try: 
        for line in f:
            prodotto = line
            driver = webdriver.Chrome()
            driver.get(prodotto)
            try:
                elem = driver.find_element(By.ID, "price")
                print(elem.text)
            except BaseException as err: 
                print('Prezzo non trovato')
            finally: driver.close()
    finally: driver.quit()
    exit()

def research():

    prodotto = url.get()
    driver = webdriver.Chrome()
    driver.get(prodotto)
    elem = driver.find_element(By.ID, "price")
    print(elem.text)
    driver.close()
    driver.quit()

window = tk.Tk()
window.title("TrackShoot")
window.resizable(width=False, height=False)

bg_frame = tk.Frame(
    master=window,
    width=600,
    height=400, 
    bg="grey"
    )

bg_frame.pack(
    fill=tk.BOTH,
    expand=True
)

main_frame = tk.Frame(
    master=bg_frame,
    width=420,
    height=220, 
    bg="white"
    )

main_frame.place(
    x=80,
    y=80
)

label = tk.Label(
    master=main_frame,
    text="Inserisci il link del prodotto Amazon che stai cercando",
    bg="white"
)

label.place(
    x=50,
    y=50
)

url = tk.Entry(
    bg="light gray", 
    master=main_frame,
    width=50
    )

url.place(
    x=50,
    y=100
)

search_btn = tk.Button(
    bg="light gray",
    master=main_frame,
    text="Cerca",
    command=research
    )

search_btn.place(
    x=180,
    y=130
)

window.mainloop()    








