from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import InitPrediction
from tkinter import messagebox, ttk

villagename = ""


def center_window(w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def read_input():
    print("inside read_input")

    farmername = textBox1.get()
    farmermobile = textBox2.get()
    n = textBox3.get()
    p = textBox4.get()
    k = textBox5.get()
    ph = textBox6.get()

    sod = textBox7.get()
    crop = textBox8.get()
    print("farmername  ", farmername)
    print("farmermobile  ", farmermobile)
    print("n  ", n)
    print("p  ", p)
    print("k  ", k)
    print("ph  ", ph)
    print("sod  ", sod)
    print("crop  ", crop)
    print("Village name is ", villagename)
    import WeatherParameters
    temperature, humidity, rainfall = WeatherParameters.getWeatherParameters(
        villagename)
    InitPrediction.startPrediction(farmername, farmermobile, n, p, k,
                                   ph, temperature, humidity,  rainfall, crop, villagename, sod)


def selection_changed(event):
    selection = combo.get()
    messagebox.showinfo(
        title="New Selection",
        message=f"Village name Selected as: {selection}"
    )
    global villagename
    villagename = selection


def getData():

    import ExtractSoilData
    N_VALUE, P_VALUE, K_VALUE, PH_VALUE = ExtractSoilData.getSoilParameters()

    print("Getting Sensor Data")
    textBox3.insert(0, N_VALUE)
    textBox4.insert(0, P_VALUE)
    textBox5.insert(0, K_VALUE)
    textBox6.insert(0, PH_VALUE)


root = Tk()
root.configure(background='#6495ED')
root.title("SHETI MITRA - FARMER'S VIRTUAL FRIEND")
#root.title2("Farmer's Virtual Friend")
center_window(1500, 900)
image = Image.open("model/main_img.jpg")

# Resize the image using resize() method
resize_image = image.resize((1500, 900))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()


username = Label(root, text="CROP YIELD PREDICTION SYSTEM", font=(
    "Courier", 30, 'bold'), fg='black', bg='#6495ED').place(x=310, y=20)
username1 = Label(root, text="FARMER'S VIRTUAL FRIEND", font=(
    "Courier", 20, 'bold'), fg='#753030', bg='#6495ED').place(x=540, y=70)

# code to create label
label1 = Label(root, text="Farmer Name: ", bg='#6495ED',
               fg='white', font=("Ariel", 16, 'bold')).place(x=100, y=150)
label2 = Label(root, text="Farmer Mobile No. : ", bg='#6495ED',
               fg='white', font=("Ariel", 16, 'bold')).place(x=100, y=210)
label3 = Label(root, text="Nitrogen (N) value. : ", bg='#6495ED',
               fg='white', font=("Ariel", 16, 'bold')).place(x=100, y=270)
label4 = Label(root, text="Phosphorus (P) value. : ", bg='#6495ED',
               fg='white', font=("Ariel", 16, 'bold')).place(x=100, y=330)
label5 = Label(root, text="Pottassium (K) value : ", bg='#6495ED',
               fg='white', font=("Ariel", 16, 'bold')).place(x=100, y=390)
label6 = Label(root, text="Ph value : ", bg='#6495ED', fg='white',
               font=("Ariel", 16, 'bold')).place(x=100, y=450)
label7 = Label(root, text="Sowing Date ( DD/MM/YYYY) : ", bg='#6495ED',
               fg='white', font=("Ariel", 16, 'bold')).place(x=100, y=510)
label8 = Label(root, text="Crop : ", bg='#6495ED', fg='white',
               font=("Ariel", 16, 'bold')).place(x=100, y=570)

label9 = Label(root, text="Village name : ", bg='#6495ED',
               fg='white', font=("Ariel", 16, 'bold')).place(x=100, y=630)


# code to insert textbox
textBox1 = tk.Entry(root, width=60, bd=4)
textBox1.place(x=525, y=150, height=40)

textBox2 = tk.Entry(root, width=60, bd=4)
textBox2.place(x=525, y=210, height=40)

textBox3 = tk.Entry(root, width=60, bd=4)
textBox3.place(x=525, y=270, height=40)  # N

textBox4 = tk.Entry(root, width=60, bd=4)  # P
textBox4.place(x=525, y=330, height=40)

textBox5 = tk.Entry(root, width=60, bd=4)  # K
textBox5.place(x=525, y=390, height=40)

textBox6 = tk.Entry(root, width=60, bd=4)       # ph
textBox6.place(x=525, y=450, height=40)

textBox7 = tk.Entry(root, width=60, bd=4)         # SOD
textBox7.place(x=525, y=510, height=40)

textBox8 = tk.Entry(root, width=60, bd=4)          # Crop name
textBox8.place(x=525, y=570, height=40)


combo = ttk.Combobox(values=["Akole", "Sangamner", "Sinnar ",
                     "Kokangaon", "Rajapur", "Loni", "Ashwi ", "Wadgaon", "Devgad"])
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=525, y=630, height=40)


# combo = ttk.Combobox()
# combo.place(x=525, y=630)
# combo = ttk.Combobox(state="readonly")
# combo = ttk.Combobox(
#     state="readonly",
#     values=["Python", "C", "C++", "Java"]
# )


# command=lambda: retrieve_input() >>> just means do this when i press the button
button = Button(root, height=1, width=13, bg='#14f526',bd=5, font=("Ariel", 16, 'bold'),
                text="SEND REPORT", command=lambda: read_input()).place(x=450, y=750)

# Button for closing
exit_button = Button(root, height=1, width=13, bg='#ff8282',bd=5, font=(
    "Ariel", 16, 'bold'), text="Exit", command=root.destroy).place(x=900, y=750)
sensorbutton = Button(root, height=1, width=15, bg='#b7f4f7', bd=5, font=("Ariel", 16, 'bold'),
                      text="GET SOIL DATA", command=lambda: getData()).place(x=1150, y=450)

mainloop()
