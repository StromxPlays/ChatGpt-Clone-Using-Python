import os
import customtkinter
from PIL import Image
# Api connection very imortant!!!
import openai
# Change the bg theme to dark
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("500x500")
app.minsize(1280, 720)
app.title("Chat Gpt")

# VARIABLES
openai.api_key = "YOUR_API_KEY"

# FUCNTIONS

def button_callback():
    user_input = text_1.get("1.0", "end")
    response = generate_response(user_input)
    label_1.delete("0.0", "end")
    label_1.insert("0.0", response) # update the text of label_1 with the response

# Create a cache dictionary
cache = {}

def generate_response(prompt):
    # Check if the prompt is already in the cache
    if prompt in cache: 
        return cache[prompt]

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1050,
        n=1,
        stop=None,
        temperature=0.2,
    )
    response = completions.choices[0].text
    # Add the prompt and response to the cache
    cache[prompt] = response
    return response

def change_theme_to_light():
    customtkinter.set_appearance_mode("light")

def change_theme_to_dark():
    customtkinter.set_appearance_mode("dark")


# Font for All
font=customtkinter.CTkFont(family='lucida', size=14)

# Frame 

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


# Text for input from user

text_1 = customtkinter.CTkTextbox(master=frame_1, width=600, height=100, text_color="white", font=("Perpetua Titling MT", 14))
text_1.place(x=370, y=160)
text_1.insert("0.0", "\n"*100)


# This button will execute the given data in entry widget by api connection

button_1 = customtkinter.CTkButton(master=frame_1, corner_radius=1000, text="Generate Response!", command=button_callback, width=300, font=("Perpetua Titling MT", 14))
button_1.place(x=500, y = 300)


# Create a CTkScrollbar widget
scrollbar = customtkinter.CTkScrollbar(master=frame_1)
scrollbar.pack(side="right", fill="y")

# Print Query
label_1 = customtkinter.CTkTextbox(master=frame_1, width=900, height=220, font=("Perpetua Titling MT", 15), text_color= "white", wrap="word")
label_1.place(x=170, y = 400)
label_1.insert("0.0", "\n"*30)

# Create a CTkScrollbar widget
scrollbar = customtkinter.CTkScrollbar(master=frame_1)
scrollbar.pack(side="right", fill="y")

# Associate the scrollbar with label_1
label_1.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=label_1.yview)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Chat With GPT-3", width=700, height=60, font=("Perpetua Titling MT", 30), text_color= "white", fg_color="transparent")
label_2.place(x=300, y=50)

label_3 = customtkinter.CTkLabel(master=frame_1, text="Output:", width=700, height=10, font=("Perpetua Titling MT", 25), text_color= "white")
label_3.place(x=-289, y=370)

# For changing to light theme
checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="Switch Light", command=change_theme_to_light)
checkbox_1.place(x = 100, y = 50)

# For changing to dark theme
checkbox_2 = customtkinter.CTkCheckBox(master=frame_1, text="Switch Dark", command=change_theme_to_dark)
checkbox_2.place(x = 100, y = 140)

# Image of Send

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images/")

send_img = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "send.png")), size=(20, 20))

chat_bot_img = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "bot.png")), size=(30, 30))

'''Label for img'''
send_frame = customtkinter.CTkLabel(master=frame_1, image=send_img, text="")
send_frame.place(x=340, y=160)

'''Chat bot img'''
chat_bot_frame = customtkinter.CTkLabel(master=frame_1, image=chat_bot_img, text="")
chat_bot_frame.place(x=120,y=400)

if __name__ == '__main__':
    app.mainloop()