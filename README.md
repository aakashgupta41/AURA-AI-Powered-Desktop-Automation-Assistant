# AURA – Python Desktop Automation Assistant

AURA is a Python-based desktop automation assistant designed to perform common Windows desktop operations through simple user commands.

The project uses Python, PowerShell, subprocess management, web browser automation, and Pillow to interact with the Windows environment and automate everyday tasks.

## 🚀 Features

* 📝 Open Windows Notepad
* 🎨 Open Microsoft Paint
* ⭕ Draw a Circle in Paint
* ⬜ Draw a Square in Paint
* 🔺 Draw a Triangle in Paint
* ▭ Draw a Rectangle in Paint
* 🔎 Search Google directly from the assistant
* 🌐 Open any website using a URL
* 🖥️ Execute Windows applications through PowerShell
* ⌨️ Interactive command-line interface
* ❌ Gracefully exit the application

## 🛠️ Technologies Used

* **Python**
* **Pillow (PIL)** – Image creation and drawing
* **PowerShell** – Windows application execution
* **Subprocess** – System-level process management
* **Webbrowser** – Opening websites and Google searches
* **OS & Tempfile** – File and temporary-file management

## 📂 Project Structure

```text
AURA/
│
├── main.py
└── README.md
```

> `main.py` contains the main assistant logic and automation functions.

## ⚙️ Requirements

Before running the project, make sure you have:

* Windows OS
* Python 3.x
* Pillow library

Install Pillow using:

```bash
pip install Pillow
```

## ▶️ How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project folder:

```bash
cd AURA
```

Install the required dependency:

```bash
pip install Pillow
```

Run the application:

```bash
python main.py
```

## 💻 How It Works

When the application starts, AURA displays an interactive menu:

```text
========================================
Hello! I am AURA, your desktop assistant.
========================================

What would you like to do?

1. Open Notepad
2. Open MS Paint
3. Search Google
4. Open a Website
5. Exit
```

The user can either enter a menu number or use commands such as:

```text
notepad
paint
google
website
exit
```

### 🎨 Paint Automation

When Paint is selected, AURA provides additional options:

```text
1. Just open MS Paint empty
2. Draw a Circle
3. Draw a Square
4. Draw a Triangle
5. Draw a Rectangle
```

For drawing operations, Pillow creates the requested shape on a temporary PNG image. The generated image is then opened automatically in Microsoft Paint.

## 🔄 Example Workflow

```text
User
  ↓
AURA
  ↓
Reads command
  ↓
Identifies requested operation
  ↓
Executes Python / PowerShell operation
  ↓
Windows application or browser opens
```

For example:

```text
You: paint

AURA: You selected MS Paint.

1. Just open MS Paint empty
2. Draw a Circle
3. Draw a Square
4. Draw a Triangle
5. Draw a Rectangle

Your choice: 2

AURA: Opening MS Paint with your circle...
```

AURA generates the image and automatically opens it in Microsoft Paint.

## 🎯 Project Objective

The main objective of AURA is to explore how Python can interact with the Windows operating system and automate desktop-level tasks.

This project demonstrates practical usage of:

* Python functions
* Conditional statements
* Loops
* User input handling
* Exception handling
* File and temporary-file management
* Process execution
* PowerShell integration
* Web browser automation
* Image generation with Pillow

## 🔮 Future Improvements

The project can be extended into a more advanced desktop assistant by adding:

* 🎤 Voice command recognition
* 🗣️ Natural-language command processing
* 🤖 AI/LLM integration
* 🔊 Text-to-speech responses
* 📂 File and folder management
* 📸 Screenshot automation
* 🖥️ System information and monitoring
* 🔐 Application permission handling
* 📧 Email automation
* 📅 Calendar and reminder integration
* 🧠 Context-aware commands

## ⚠️ Current Limitations

AURA currently uses predefined commands and menu-based operations. It does not yet use an AI or natural-language-processing model to understand completely free-form instructions.

The project is currently designed for **Windows** because it relies on Windows applications such as Notepad, Microsoft Paint, and PowerShell.

## 👨‍💻 Learning Outcomes

Through this project, I explored how Python can be used beyond traditional programming exercises to interact with the operating system and automate real-world desktop tasks.

The project also provides a foundation for developing a more advanced AI-powered personal desktop assistant in the future.

## 📜 License

This project is open-source and available for educational and personal use.

---

### ⭐ Future Vision

> **AURA aims to evolve from a command-based desktop automation tool into an intelligent personal desktop assistant capable of understanding and executing natural-language commands.**
