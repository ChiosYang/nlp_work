import customtkinter
import tkinterDnD
from categorization import fuck_nlp


customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1080x720")
app.title("No NLP")

print(type(app), isinstance(app, tkinterDnD.Tk))


def button_callback():
    content = text_1.get("0.0","end")
    model_name = optionmenu_1.get()
    result = fuck_nlp(model_name,content)
    result = "Result : "+result
    label_1.configure(text=result)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["TextCNN", "TextRNN", "TextRNN_Att", "Transformer"], anchor="center")
optionmenu_1.pack(pady=20, padx=10)
optionmenu_1.set("TextCNN")

text_1 = customtkinter.CTkTextbox(master=frame_1, width=600, height=200)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "在这输入文本")

button_1 = customtkinter.CTkButton(master=frame_1, text='Start',command=button_callback)
button_1.pack(pady=10, padx=10)


label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT,text='',font=('Arial', 30, 'bold'))
label_1.pack(pady=40, padx=10)

app.mainloop()