from googletrans import Translator
import os
from pyperclip import paste

notification_title = "Translated"
target_lang = "pt"

def translate(text, lang):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    return translation.text

def get_clipboard():
    return paste()

def show_notification(text):
    os.system("""
        osascript -e 'display notification "{}" with title "{}"'
        """.format(text, notification_title))

def main():
    clipboard = get_clipboard()
    if (clipboard):
        translated = translate(clipboard, target_lang)
        show_notification(translated)
    else :
        show_notification("No text in clipboard")

if __name__ == "__main__":
    main()