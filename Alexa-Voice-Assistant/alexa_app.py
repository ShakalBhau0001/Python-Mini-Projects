import pyttsx3
import pywhatkit
import pyjokes
import random
import wikipedia
import datetime as dt
import requests
import speech_recognition as sr
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

class AlexaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Voice Assistant")
        self.root.geometry("700x700")  
        self.root.configure(bg="cyan")      
        self.listener = sr.Recognizer()
        try:
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty('voices')
            print("Available Voices:")
            for idx, voice in enumerate(voices):
                print(f"{idx}: {voice.name}")
            if len(voices) > 1:
                self.engine.setProperty('voice', voices[1].id)
            else:
                self.engine.setProperty('voice', voices[0].id)
        except Exception as e:
            messagebox.showerror("TTS Error", f"Failed to initialize speech engine: {e}")
            self.root.quit()
            return

        self.stop_command = False
        self.check_internet_connection()
        self.create_gui_interface()
        
    def create_gui_interface(self):
        self.label = tk.Label(self.root, text="Click the microphone and speak", font=("Algerian", 15), wraplength=350, bg="cyan",fg="deeppink")
        self.label.pack(pady=20)
        try:
            pil_image = Image.open("Add-Your-Image-Path")
            self.mic_image = ImageTk.PhotoImage(pil_image)
            self.mic_button = tk.Button(self.root, image=self.mic_image, command=self.run_alexa, borderwidth=0)
            self.mic_button.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Image Error", f"Microphone image failed to load: {e}")
            self.root.quit()
            return

        self.exit_button = tk.Button(self.root, text="EXIT", command=self.root.quit, font=("Bodoni MT Black", 15), bg="cyan", fg="red")
        self.exit_button.pack(pady=10)

    def check_internet_connection(self):
        try:
            requests.get("https://www.google.com", timeout=5)
            self.internet_connected = True
        except requests.ConnectionError:
            self.internet_connected = False
            messagebox.showwarning("Connection Error", "No internet connection. Some features may not work.")

    def talk(self, text):
        try:
            self.label.config(text=text)
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Speech Error: {e}")
            messagebox.showwarning("Speech Failed", "Could not speak the response")

    def take_command(self):
        command = ""
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.listener.adjust_for_ambient_noise(source, duration=1)
                voice = self.listener.listen(source, timeout=5)
                command = self.listener.recognize_google(voice).lower()
                
                if 'alexa' in command:
                    command = command.replace('alexa', '').strip()
                if 'end' in command or 'exit' in command:
                    self.talk('Goodbye!')
                    self.root.quit()
        except sr.WaitTimeoutError:
            self.talk("I didn't hear anything. Please try again.")
        except Exception as e:
            print(f"Recognition Error: {e}")
            self.talk("I couldn't understand that. Please Say Again.")
        return command

    def manual_input(self, prompt):
        return simpledialog.askstring("Manual Input", prompt)

    def search_wikipedia(self, query, max_paragraphs=3):
        try:
            wikipedia.set_lang("en")
            return wikipedia.summary(query, sentences=max_paragraphs)
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Multiple matches found. Please be more specific. Options: {', '.join(e.options[:3])}"
        except wikipedia.exceptions.PageError:
            return None

    def read_info_alexa(self, text):
        for paragraph in text.split('\n'):
            if paragraph.strip():
                self.talk(paragraph.strip())

    def search_google(self):
        self.talk("What would you like me to search on Google?")
        query = self.take_command()
        if query:
            pywhatkit.search(query)
            self.talk(f"Searching Google for {query}")

    def run_alexa(self):
        if not self.internet_connected:
            self.talk("Internet connection required for this feature.")
            return

        command = self.take_command()
        if not command:
            return

        print("Processing command:", command)
        
        if 'wikipedia' in command:
            self.handle_wikipedia_search()
        elif 'youtube' in command:
            self.handle_youtube_playback()
        elif 'google' in command:
            self.search_google()
        elif 'date' in command or 'time' in command:
            self.handle_time_date()
        elif 'joke' in command:
            self.tell_joke()
        elif 'single' in command:
            self.relationship_status()
        elif 'goodbye' in command or 'bye' in command:
            self.exit_program()
        elif 'hello' in command:
            greetings = [
                "Hello love, how can I brighten your day?",
                "Hey there, sunshine ☀️ Ready to rule the world?",
                "Hi sweet soul, what can I do for you today?",
                "Greetings master, your wish is my command 🪄",
                "Welcome back, my favorite love 🧠❤️",
                "Hello dear, I missed your voice already!",
                "Hey hero, let's do something amazing!"
            ]
            self.talk(random.choice(greetings))
            
        else:
            self.talk("I didn't understand that command. Please try again.")

    def handle_wikipedia_search(self):
        self.talk('What topic would you like to search for?')
        topic = self.take_command()
        
        if not topic or 'search' in topic:
            topic = self.manual_input('Please enter the topic:')
        
        if topic:
            self.talk(f"Searching Wikipedia for {topic}...")
            info = self.search_wikipedia(topic)
            if info:
                self.read_info_alexa(info)
                self.talk("Wikipedia search complete.")
            else:
                self.talk("No information found for that topic.")

    def handle_youtube_playback(self):
        self.talk('What music would you like to hear?')
        song = self.take_command()
        
        if not song or 'search' in song:
            song = self.manual_input('Enter song name:')
        
        if 'random' in song or 'any' in song:
            genres = [
                'lofi', 'pop', 'rock', 'telugu',
                'jazz', 'hip hop', 'country',
                'arabic', 'love', 'electronic','romantic',
                'trance','persian','hindi','english','spanish',
                'french','korean','japanese','russian','tamil'
            ]
            song = random.choice(genres)
            self.talk(f"Playing random {song} music")
        
        if song:
            pywhatkit.playonyt(song)
            self.talk(f"Playing {song} on YouTube")

    def handle_time_date(self):
        current_time = dt.datetime.now().strftime('%I:%M %p')
        current_date = dt.datetime.now().strftime('%B %d, %Y')
        time_date_info = f"Current time is {current_time} and today's date is {current_date}"
        self.talk(time_date_info)

    def tell_joke(self):
        joke = pyjokes.get_joke()
        self.talk(joke)

    def relationship_status(self):
        self.talk("I'm in a committed relationship with Wi-Fi")

    def exit_program(self):
        self.talk("Shutting down. See You Soon!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlexaApp(root)
    root.mainloop()
