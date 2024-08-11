from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")  # Fixed the geometry syntax
root.config(background="#dae6f6")  # Fixed the background attribute spelling

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())
    spell.config(text="Correct text is: " + right)

heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("Poppins", 25), bg="white", borderwidth=2, relief="solid")
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font=("Arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack(pady=20)

spell = Label(root, font=("Poppins", 20), bg="#dae6f6", fg="#364971")
spell.pack(pady=20)

root.mainloop()
