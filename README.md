# Django Bitcoin Price Chart Documentation

Welcome to the documentation for the Django Bitcoin Price Chart project. This documentation will guide you through the process of setting up and working with a Django project that displays a Bitcoin price chart. This project will use Django, Python, and a third-party API to fetch Bitcoin price data and present it in a chart format.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Fetching Bitcoin Price Data](#fetching-bitcoin-price-data)
6. [Chart Rendering](#chart-rendering)
7. [Frontend](#frontend)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Additional Resources](#additional-resources)

## Getting Started

To get started with the Django Bitcoin Price Chart project, follow these steps:

1. Install Python: Django requires Python to be installed on your system. You can download Python from the official Python website: https://www.python.org/downloads/

2. Install Django: Once you have Python installed, you can install Django using pip, the package installer for Python. Open your command line interface and run the following command:

   ```
   pip install Django
   ```

3. Clone the Repository: Clone the Django Bitcoin Price Chart repository from GitHub to your local machine:

   ```
   git clone https://github.com/BitJager94/DjangoBitcoinPrice.git
   ```

4. Navigate to the Project Directory: Use the `cd` command to navigate to the project directory:

   ```
   cd django-bitcoin-price-chart
   ```

5. Start the Development Server: Start the Django development server with the following command:

   ```
   python manage.py runserver
   ```

8. Open the Application: Open your web browser and visit `http://localhost:8000` to see the Bitcoin price chart.

## Project Structure

The Django Bitcoin Price Chart project has the following directory structure:

```
DjangoBitcoinPrice/
    DjangoWebsiteDemo/
        templates/
            index.html
        controllers
            public.py
        tests/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py 
    .gitignore
    manage.py
    README.md
```

- The `DjangoBitcoinPrice/` directory contains the Django app that handles the Bitcoin price chart functionality.
- The `DjangoWebsiteDemo/` directory contains the project-level configuration files.

## Installation

The installation process is covered in the "Getting Started" section. Please refer to that section for installation instructions.

## Configuration

The project utilizes the following configuration files:

- `DjangoWebsiteDemo/settings.py`: This file contains the Django project settings, including database configuration, installed apps, and other project-specific settings.
- `DjangoWebsiteDemo/urls.py`: This file defines the project-level URL patterns.

Please review these files to configure the project according to your needs.

## Fetching Bitcoin Price Data

To fetch Bitcoin price data, the project uses a third-party API. The documentation for the API can be found at [API Documentation](https://example-api.com/docs).

Refer to the `DjangoWebsiteDemo/templates/index.html` file in the project for an example of how to fetch and process Bitcoin price data using the API.

## Chart Rendering

The project utilizes a charting library to render the Bitcoin price chart. The library used is [Chart.js](https://www.chartjs.org/).

To customize the chart appearance or add additional features, refer to the Chart.js documentation.

## Frontend

The frontend of the Django Bitcoin Price Chart project is built using HTML, CSS, and JavaScript. The project includes templates located in the `DjangoWebsiteDemo/templates/` directory.

To modify the frontend, you can edit the existing templates or create new ones according to your requirements.


## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/): Official Django documentation.
- [Chart.js Documentation](https://www.chartjs.org/docs/latest/): Official Chart.js documentation.
- [Python Documentation](https://docs.python.org/): Official Python documentation.

Please refer to these resources for more information on Django, Chart.js, and Python.