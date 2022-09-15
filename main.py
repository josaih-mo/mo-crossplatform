from tkinter import * 
from PIL import ImageTk, Image
import os
import openai
import typing



def get_ai_prompt(prm: str):
    # Get the AI's prompt.
    openai.api_key = "YOUR API KEY!"

    fixedprompt = """
    MO is a fun, caring, and happy AI. MO likes horses, fanart, and is red.


    """ + prm

    response = openai.Completion.create(
          model="text-davinci-002",
          prompt=fixedprompt,
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
    )
    return response.choices[0].text

print(get_ai_prompt("Hey MO, what's your name?"))

#exit(0)
root = Tk() 
root.title("MO Labs AI - Unofficial Cross-Platform Version") 
root.geometry("400x400") # add an image 
background_image = PhotoImage(file="background.png") 
background_label = Label(root, image=background_image) 
background_label.place(x=0, y=0, relwidth=1, relheight=1)

my_img = Image.open(
    r"C:\Users\Josiah\Downloads\mo-cp\idle.png")

my_img = my_img.resize((60, 60), Image.ANTIALIAS) 
my_img2 = ImageTk.PhotoImage(my_img)

root.iconphoto(True, my_img2) 
my_label = Label(image=my_img2) 
my_label.place(relx=0.5, rely=0.5, anchor=CENTER)
# add a text entry box 
my_entry = Entry(root, width=10) 
my_entry.pack() 
# add some text 
my_text = Label(root, height=10, text="momoto mo mo mo!") 
my_text.pack()

#add a button
def button_command():
    my_text.config(text = get_ai_prompt(my_entry.get()))
button1 = Button(root, text="Ask!", command=button_command)
button1.pack()
root.mainloop()
