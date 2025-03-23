import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

CONFIG_FILE = "config.txt"

def save_username(username):
    #saves letterboxd username to file
    with open(CONFIG_FILE, "w") as file:
        file.write(username)

def load_username():
    if os.path.exists(CONFIG_FILE): #check if file exists
        with open(CONFIG_FILE, "r") as file:
            return file.read().strip() #reads and removes whitespace
    return None #if no username is saved return none

import requests
from bs4 import BeautifulSoup

def get_movie_list(username):
    movies = []
    page_number = 1  # starts at page 1 of watchlist

    label.config(text="Searching for perfect movie...")
    label.update()

    while True:
        url = f"https://letterboxd.com/{username}/watchlist/page/{page_number}/"
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            # send get request to url
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Will raise an exception for 4xx/5xx HTTP status codes
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            break
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            break
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            break
        except requests.exceptions.RequestException as err:
            print(f"OOps! Something went wrong: {err}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        page_movies = [tag["alt"] for tag in soup.find_all("img", class_="image")]

        # if no movies on page, stop loop
        if not page_movies:
            break

        # add movies from this page to list
        movies.extend(page_movies)
        # move to next page
        page_number += 1

    label.config(text="Movie Picker Ready!")
    return movies if movies else ["No movies found!"]


def set_username():

    global username
    new_username = simpledialog.askstring("Letterboxd Username", "Enter your letterboxd username: ")

    if new_username:
        save_username(new_username)
        username = new_username
        messagebox.showinfo("Username saved", f"Username set to: {username}")

def pick_random_movie():
    if not username:
        messagebox.showerror("Error", "No username set! Click 'set username' first.")
        return
    
    movies = get_movie_list(username)

    if "No movies found!" in movies:
        messagebox.showerror("Error", "No movies found in the watchlist.")
    else:
        movie = random.choice(movies)
        messagebox.showinfo("Movie Picked!", f"🎬 Watch: {movie}")

username = load_username()


#-----------------------GUI------------------------#

root = tk.Tk()
root.title("Letterboxd Movie Picker")
root.geometry("400x300")
root.config(bg="#f0f0f0")  # Set background color of the window

# Center window on screen
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Title Label
title_label = tk.Label(root, text="Welcome to Movie Picker!", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Loading Label
label = tk.Label(root, text="Click the button to pick a movie!", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
label.pack(pady=10)

# Set Username Button
button_set = tk.Button(root, text="Set Username", command=set_username, font=("Helvetica", 12), bg="#007bff", fg="white", relief="raised", width=20, height=2)
button_set.pack(pady=10)

# Pick a Movie Button
button_pick = tk.Button(root, text="Pick a Movie 🎬", command=pick_random_movie, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised", width=20, height=2)
button_pick.pack(pady=10)

# Hover effect for the button (Change color when hovered)
def on_enter(e):
    button_pick.config(bg="#45a049")

def on_leave(e):
    button_pick.config(bg="#4CAF50")

button_pick.bind("<Enter>", on_enter)
button_pick.bind("<Leave>", on_leave)

# Run the main window loop
root.mainloop()