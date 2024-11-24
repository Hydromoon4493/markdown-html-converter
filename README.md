# Text to HTML/Markdown Converter

This is a simple web application built using **Flask** that allows users to convert plain text into both HTML and Markdown formats. The application provides a form where you can enter text, and upon submission, it will display the converted HTML and Markdown outputs.

## Features

- **Text Input**: Enter any plain text into the text area.
- **HTML Conversion**: Converts the entered text into simple HTML format.
- **Markdown Conversion**: Converts the entered text into Markdown format.
- **Dynamic Output**: The converted HTML and Markdown outputs are displayed dynamically on the same page after form submission.

## Requirements

To run this application, you need the following:
- Python 3.x
- Flask
- Markdown library (for converting to Markdown)

## Installation and Setup

### Step 1: Clone or Download the Repository

If you're using Git, clone the repository:
    'git clone https://github.com/Hydromoon4493/markdown-html-converter'

Alternatively, download the ZIP file and extract it to a folder.

### Step 2: Set Up a Virtual Environment (Optional, but recommended)

A virtual environment helps keep project dependencies isolated. Follow these steps to create and activate it:

1. Open your terminal/command prompt and navigate to the project directory.
2. Create a virtual environment:

On **Windows**:
    'python -m venv venv'

On **Mac/Linux**:
    'python3 -m venv venv'

3. Activate the virtual environment:

On **Windows**:
    '.\venv\Scripts\activate'

On **Mac/Linux**:
    'source venv/bin/activate'

### Step 3: Install Dependencies

With your virtual environment activated, install the required libraries using `pip`:
    'pip install flask markdown'

This will install both **Flask** (for the backend server) and **Markdown** (for converting the text to Markdown format).

### Step 4: Run the Flask Server

To start the Flask server, run the following command in your terminal:
    'python app.py'

This will start a local server. The terminal will display something like:
    'Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)'

### Step 5: Access the Web Application

Open your web browser and navigate to:
    'http://127.0.0.1:5000/'

This will open the **Text to HTML/Markdown Converter** application where you can enter text and see the HTML and Markdown output.

## How to Use

1. **Enter text** in the text area on the main page.
2. **Click the "Convert" button** to convert the text to both HTML and Markdown formats.
3. The page will display the converted HTML and Markdown below the input form.

## Files

- `app.py`: The main Flask application that handles routes and the conversion logic.
- `templates/index.html`: The HTML template that displays the user interface.
- `README.md`: This file that provides instructions on how to set up and run the project.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request.

## License

This project is open-source and available under the MIT License.

---

Enjoy converting your text to HTML and Markdown formats!
