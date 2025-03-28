
# Movie Picker App

A simple Python application that randomly picks a movie from your Letterboxd watchlist. It scrapes your watchlist, navigates through all the pages, and randomly selects a movie for you to watch. This app is packaged as a standalone executable, so you can run it directly on your desktop.

## Features:
- Scrapes your **Letterboxd** watchlist.
- Navigates through multiple pages of the watchlist.
- Picks a random movie from the list.
- Simple and intuitive **GUI** built with **Tkinter**.
- **Set your Letterboxd username** and pick a movie with one click.

## Installation Instructions

### **Option 1: Running the Script with Python**
To run the app directly with Python, follow these steps:

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/movie-picker.git
   cd movie-picker
2. **Set up VENV**
    python -m venv .venv
    .\.venv\Scripts\Activate  # On Windows
    # or
    source .venv/bin/activate  # On Mac/Linux

3. **Install Dependencies**
    pip install -r requirements.txt

4. **Run App**
    python movie_picker.py


Option 2: Running the Executable
If you prefer to use the standalone executable, follow these steps:

Download the Executable:
Download the movie_picker.exe file from the releases section or from wherever the executable is provided.

Set Your Letterboxd Username:
Open the app, click the "Set Username" button, and enter your Letterboxd username.

Pick a Movie:
After setting the username, click the "Pick a Movie" button, and the app will randomly select a movie from your watchlist.

Usage
Set Username:

Click the "Set Username" button to enter your Letterboxd username.

This will save your username, so you don't need to enter it every time.

Pick a Movie:

After setting your username, click the "Pick a Movie 🎬" button to randomly pick a movie from your watchlist.

Loading Indicator:

While the app is scraping your watchlist, a loading message will appear.

Once finished, the app will display a random movie or show an error message if no movies were found.

Troubleshooting
If the app is not finding movies, make sure your Letterboxd watchlist is publicly accessible.

Ensure that your username is entered correctly.

If you encounter any issues, feel free to open an issue on the GitHub issues page.
