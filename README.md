# Crypto Coin Scraper API

This Django Rest Framework API allows users to scrape data from various cryptocurrency websites using Celery for background task processing. It provides endpoints to start scraping tasks for a list of crypto coins and check the status and results of these tasks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)


## Features

- Submit scraping jobs for multiple crypto coins concurrently
- Check the status and results of scraping jobs using job IDs
- Background task processing using Celery
- Integration with Django Admin for managing scraping tasks and job results

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
## Install dependencies:
pip install -r requirements.txt

## Run the development server:
python manage.py runserver

Usage
Access the Django Admin interface at http://localhost:8000/admin/ to manage scraping tasks and view job results.
Use API endpoints to start scraping tasks and check scraping status and results.
API Endpoints
POST /api/taskmanager/start_scraping/: Start scraping tasks for a list of crypto coins.
GET /api/taskmanager/scraping_status/<job_id>/: Check the status and results of scraping tasks for a specific job ID.
Screenshots
Django Admin Screenshots
Screenshot 1: Scraping Tasks
Screenshot 2: Scraping Job Results
Postman Screenshots
Screenshot 1: Start Scraping Task
Screenshot 2: Scraping Status
