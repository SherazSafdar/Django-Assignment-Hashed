# Django Advertisement System

Django Advertisement System is a web application that allows users to create and manage advertisements with location-based restrictions. Similar to popular ad systems like Facebook and Instagram.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Admin can create ads with start and end dates.
- Ads can be assigned to multiple locations, each with a maximum number of daily visitors.
- Daily visitor count limits for each location to control ad visibility.
- Automatic blocking and unblocking of ads based on daily visitor counts.
- Advanced APIs for CRUD operations on ads, locations, and visit counts.

## Requirements

- asgiref==3.7.2
- backports.zoneinfo==0.2.1
- Django==4.2.8
- djangorestframework==3.14.0
- psycopg2==2.9.9
- pytz==2023.3.post1
- sqlparse==0.4.4
- typing-extensions==4.9.0


## Installation

1. Clone the repository:

git clone https://github.com/SherazSafdar/ToDo-App-Django


2. Change to the project directory:


3. Create and activate a virtual environment :
python -m venv venv
source venv/bin/activate # On macOS and Linux
.\venv\Scripts\activate # On Windows


4. Install project dependencies from the requirements.txt file:
pip install -r requirements.txt


## Configuration

1. Create a `.env` file in the project directory and configure environment variables such as database credentials:



## Contact

- Sheraz Safdar
- sherazsafdar00@gmail.com

Feel free to reach out if you have any questions or need assistance.
