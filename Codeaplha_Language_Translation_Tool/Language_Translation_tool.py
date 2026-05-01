from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

engine = pyttsx3.init()

# Supported languages (clean names → codes)
languages = {
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-cn"
}

# Main Window
root = Tk()
root.title("AI Language Translator")
root.geometry("700x500")
root.resizable(False, False)

# Functions
def translate_text():
    try:
        text = input_text.get("1.0", END).strip()
        src_lang = src_lang_combo.get()
        dest_lang = dest_lang_combo.get()

        if text == "":
            messagebox.showwarning("Warning", "Please enter text")
            return

        src_code = languages[src_lang]
        dest_code = languages[dest_lang]

        translated = GoogleTranslator(source=src_code, target=dest_code).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", END))
    messagebox.showinfo("Copied", "Text copied to clipboard")


def speak_text():
    text = output_text.get("1.0", END)
    if text.strip() == "":
        messagebox.showwarning("Warning", "No text to speak")
        return
    engine.say(text)
    engine.runAndWait()


# Labels
Label(root, text="Enter Text", font=("Arial", 12)).place(x=50, y=20)
Label(root, text="Translated Text", font=("Arial", 12)).place(x=50, y=240)

# Input Text
input_text = Text(root, height=5, width=70)
input_text.place(x=50, y=50)

# Output Text
output_text = Text(root, height=5, width=70)
output_text.place(x=50, y=270)

# Dropdowns
src_lang_combo = ttk.Combobox(root, values=list(languages.keys()), width=25)
src_lang_combo.place(x=50, y=170)
src_lang_combo.set("English")

dest_lang_combo = ttk.Combobox(root, values=list(languages.keys()), width=25)
dest_lang_combo.place(x=300, y=170)
dest_lang_combo.set("Urdu")

# Buttons
Button(root, text="Translate", command=translate_text, bg="lightblue").place(x=550, y=165)
Button(root, text="Copy", command=copy_text).place(x=200, y=420)
Button(root, text="Speak", command=speak_text).place(x=350, y=420)

root.mainloop()


