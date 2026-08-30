# Movie Browser 
Live at : https://moviebrowser-1.onrender.com

A full-stack Django web application that ingests movie data from an external API, stores it in a local SQLite database, and provides users with browsing, search, and watchlist management capabilities.

## Features

* **Data Ingestion & Storage:** Fetches movies and cast details from an external API and stores them locally using Django's ORM (`get_or_create`) to prevent duplicates.
* **User Authentication:** Secure registration, login, and logout flows using Django's built-in authentication system.
* **Personalized Watchlist:** Authenticated users can add or remove movies from their personal watchlist.
* **Search & Pagination:** Browse the movie catalog with server-side pagination and a case-insensitive search bar (`icontains`).
* **Relational Database Design:** Utilizes `ManyToManyField` for linking Movies to Cast members and Movies to Users (Watchlists).
* **Robust Error Handling:** Uses `get_object_or_404` for safe database queries and gracefully handles missing API data.

## Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite (Development)
* **Frontend:** Django Templates (HTML), CSS
* **Authentication:** Django Session Auth

## Prerequisites

* Python 3.8+
* `pip` (Python package installer)

## Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nitin5117/MovieBrowser/>
   cd TASK3
