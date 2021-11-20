import tkinter as tk
from tkinter import*
import requests
import os
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Weather App")
root.geometry("600x500")



def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City:%s\nConditions :%s\nTemprature :%s °F' % (city, condition, temp)

    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '802f976540cebc37068f58366372ff81'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parans = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, parans)

    weather = response.json()


    result['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size = int(frame_two.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete('all')
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


img = Image.open('./Weather/bg2.png')
img = img.resize((600, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

# the box height and width
bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

heading_title = tk.Label(bg_lbl, text='Including over 200,000 cities!', fg='red', bg='#ffe4e1',
                         font=('times new roman', 18, 'bold'))
heading_title.place(x=80, y=10, width=450, height=50)


frame_one = tk.Frame(bg_lbl, bg="#ffe4e1", bd=5)
frame_one.place(x=80, y=50, width=450, height=80)

txt_box = tk.Entry(frame_one, font=('Copperplate', 22), width=17)
txt_box.grid(row=0, column=0, sticky='w')

btn = tk.Button(frame_one, text='Get Weather', fg='green', font=('Monaco', 15, 'bold'),
                command=lambda: get_weather(txt_box.get()))

btn.grid(row=0, column=1, padx=9)

frame_two = tk.Frame(bg_lbl, bg="#ffb6c1", bd=5)
frame_two.place(x=80, y=190, width=450, height=250)

result = tk.Label(frame_two, font=30, bg='white', justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(result, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

frame_three=tk.Frame(bg_lbl, bg="#ffe4e1", bd=10)
frame_three.place(x=80, y=94, width=450, height=50)
mb=Menubutton(frame_three,text="City Graph" , fg='green', font=('Monaco', 15, 'bold'))
mb.pack(side="bottom")



mb.menu=Menu(mb)
mb["menu"]=mb.menu

opt1=IntVar()
opt2=IntVar()
opt3=IntVar()
opt4=IntVar()


mb.menu.add_checkbutton(label="New Delhi",variable=opt1,font='Monaco',command=lambda:os.system('gra.py'))
mb.menu.add_checkbutton(label="Mumbai",variable=opt2,font='Monaco',command=lambda:os.system('gra2.py'))
mb.menu.add_checkbutton(label="Kolkata",variable=opt3,font='Monaco',command=lambda:os.system('gra3.py'))
mb.menu.add_checkbutton(label="Shimla",variable=opt4,font='Monaco',command=lambda:os.system('gra4.py'))


mb.pack()

root.mainloop()