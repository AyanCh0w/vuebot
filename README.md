# Grade Information Retriever
This application retrieves grade information from a website using Selenium WebDriver and Flask.

## Requirements

Python 3.x
Flask
Selenium
Chrome WebDriver

## Setup

Install the required Python packages:

Copy `pip install flask selenium`

Download the appropriate Chrome WebDriver for your Chrome version and place it in the project directory or a directory included in your system's PATH.

## Usage

Run the Flask application:

Copy `python main.py`

Send a GET request to `http://localhost:5000/getGradeInfo` with the username and password form data.
The application will return a JSON response containing the class names and corresponding grades.

## Files

`main.py`: 
Sets up the Flask application and defines the /getGradeInfo route.


`api.py`:
Contains the getGradeInfo function that performs the following tasks:

1. Initializes a Chrome WebDriver instance.
2. Navigates to the website and logs in with the provided credentials.
3. Accesses the gradebook section.
4. Extracts the class names and grades.
5. Returns the formatted class data.
