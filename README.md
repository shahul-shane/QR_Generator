# **CodePlay Chronicles**
# QR Code Generator with Flask

Welcome to the QR Code Generator project, part of the **CodePlay Chronicles** series! This simple yet effective application allows you to generate QR codes for any text or URL. It's designed to practice Flask and Python's QR code generation capabilities.

## Project Overview

While this project may seem straightforward/silly as its very common and simple, it serves as an excellent exercise in understanding Flask and QR code generation. By working on this, you'll gain hands-on experience with Flask's routing, templates, and form handling, as well as Python's `qrcode` library for creating QR codes.

## Features

- **Generate QR Codes**: Input any text or URL to create a corresponding QR code.
- **User-Friendly Interface**: A simple web interface to input data and display the generated QR code.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: Download and install Python from the [official website](https://www.python.org/downloads/).
- **Virtual Environment (optional but recommended)**: Use `venv` to create an isolated environment for the project.

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone <repository_url>
   cd qr-code-generator
   
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv

4. **Activate the Virtual Environment**:
   **On Windows**:
   ```bash
   venv\Scripts\activate
   
   **On mac**:
   ```bash
   source venv/bin/activate

5. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

6. **Run the Application**:
   ```bash
   python main.py

The application will start, and you can access it at http://127.0.0.1:5000/.

#### *Usage*
- 1.Open your web browser and navigate to http://127.0.0.1:5000/.
- 2.Enter the text or URL you want to encode into a QR code.
- 3.Click the "Generate QR Code" button.
- 4.The generated QR code will be displayed on the page.

#### *Conclusion*
This project, though simple, provides valuable insights into building web applications with Flask and generating QR codes using Python. It's an excellent starting point for those looking to practice and enhance their Flask skills.
    
