import os
import subprocess
import webbrowser
import sys
import tempfile
from PIL import Image, ImageDraw

def draw_and_open_paint(shape):
    # Create a blank white image
    img = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw the requested shape
    if shape == 'circle':
        # Bounding box for the circle
        draw.ellipse([200, 100, 600, 500], outline="black", width=5)
    elif shape == 'square':
        # Bounding box for the square
        draw.rectangle([200, 100, 600, 500], outline="black", width=5)
    elif shape == 'rectangle':
        draw.rectangle([100, 200, 700, 400], outline="black", width=5)
    elif shape == 'triangle':
        # Points for the triangle
        draw.polygon([(400, 100), (200, 500), (600, 500)], outline="black", width=5)
        
    # Save the image to a temporary file
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, f"jarvis_{shape}.png")
    img.save(file_path)
    
    print(f"JARVIS: Opening MS Paint with your {shape}...")
    subprocess.Popen(["powershell", "-Command", f"Start-Process mspaint -ArgumentList '{file_path}'"])

def handle_paint_command():
    print("\nJARVIS: You selected MS Paint.")
    print("What would you like to do?")
    print(" 1. Just open MS Paint empty")
    print(" 2. Draw a Circle")
    print(" 3. Draw a Square")
    print(" 4. Draw a Triangle")
    print(" 5. Draw a Rectangle")
    
    choice = input("Your choice (1-5): ").strip()
    
    if choice == '1':
        print("JARVIS: Opening MS Paint...")
        subprocess.Popen(["powershell", "-Command", "Start-Process mspaint"])
    elif choice == '2':
        draw_and_open_paint('circle')
    elif choice == '3':
        draw_and_open_paint('square')
    elif choice == '4':
        draw_and_open_paint('triangle')
    elif choice == '5':
        draw_and_open_paint('rectangle')
    else:
        print("JARVIS: Invalid choice. Returning to main menu.")

def open_notepad():
    print("JARVIS: Opening Notepad...")
    subprocess.Popen("notepad.exe", shell=True)

def search_google():
    query = input("JARVIS: What would you like to search Google for? \nYou: ").strip()
    if query:
        print(f"JARVIS: Searching Google for '{query}'...")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    else:
        print("JARVIS: Search cancelled.")

def open_website():
    site = input("JARVIS: Enter the website URL (e.g., youtube.com): \nYou: ").strip()
    if site:
        print(f"JARVIS: Opening {site}...")
        if not site.startswith("http"):
            site = "https://" + site
        webbrowser.open(site)
    else:
        print("JARVIS: Action cancelled.")

def greet_user():
    print("========================================")
    print("Hello! I am JARVIS, your text-based desktop assistant.")
    print("========================================")

def main():
    greet_user()
    while True:
        try:
            print("\nWhat would you like to do?")
            print(" 1. Open Notepad")
            print(" 2. Open MS Paint")
            print(" 3. Search Google")
            print(" 4. Open a Website")
            print(" 5. Exit")
            
            command = input("\nYou: ").strip().lower()
            
            if not command:
                continue
                
            if command in ['5', 'exit', 'quit']:
                print("JARVIS: Goodbye! Have a great day.")
                sys.exit(0)
                
            elif command == '1' or 'notepad' in command:
                open_notepad()
                
            elif command == '2' or 'paint' in command:
                handle_paint_command()
                
            elif command == '3' or 'google' in command:
                search_google()
                    
            elif command == '4' or 'website' in command:
                open_website()
                
            else:
                print("JARVIS: I'm sorry, I don't understand that command. Please enter a number 1-5.")
                
        except KeyboardInterrupt:
            print("\nJARVIS: Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
