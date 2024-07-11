# Django Blog Project

## Overview

Welcome to the Django Blog Project! This project is a blog application built with Django, designed to showcase various aspects of web development, including article creation, subscription functionality, and contact forms. The project is visually appealing and incorporates modern web development practices.

## Features

- **Latest Posts:** Display the latest three blog posts on the homepage.
- **Detailed Post View:** View detailed content of each blog post.
- **Chart Data:** Visualize data about writers and their articles.
- **Contact Form:** Submit contact inquiries through a form.
- **Newsletter Subscription:** Subscribe to a newsletter for updates.
- **CSRF Protection:** Ensures secure form submissions.

## Technologies Used

- Django
- HTML/CSS
- Bootstrap
- JavaScript
- Django Chart.js

## Setup Instructions

### Prerequisites

- Python 3.6+
- Django 3.0+
- Virtualenv

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/django-blog.git
    cd django-blog
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### Configuration

- **Database:** The project uses the default SQLite database. You can change the database settings in `settings.py`.
- **Static Files:** Ensure you collect static files by running:
    ```bash
    python manage.py collectstatic
    ```

## Usage

1. **Homepage:** Navigate to `http://127.0.0.1:8000/` to view the latest blog posts.
2. **Post Detail:** Click on a post title to view its detailed content.
3. **Subscribe to Newsletter:** Enter your email and click "Subscribe" to join the newsletter.
4. **Contact Form:** Navigate to the contact page and submit your inquiries.
5. **Admin Panel:** Access the admin panel at `http://127.0.0.1:8000/admin/` to manage posts, writers, and subscribers.

## Code Overview

### Views

- **index:** Displays the latest blog posts.
- **post:** Shows detailed content of a specific post.
- **chart_data:** Provides data for visualizing writer statistics.
- **blog_list:** Lists all blog posts.
- **about_page:** Renders the about page.
- **contact_submission:** Handles contact form submissions.
- **subscribe:** Manages newsletter subscription.

### Models

- **Post:** Represents a blog post.
- **Writer:** Represents an article writer.
- **Article:** Represents an article written by a writer.
- **ContactSubmission:** Stores contact form submissions.
- **NewsletterUser:** Stores newsletter subscribers.

### Templates

- **base.html:** Base template with common layout.
- **index.html:** Homepage template.
- **post.html:** Post detail template.
- **blog_list.html:** Blog list template.
- **about.html:** About page template.
- **contact.html:** Contact form template.

## Troubleshooting

### CSRF Verification Failed

If you encounter a CSRF verification error, ensure the following:

- `{% csrf_token %}` is included in all POST forms.
- Your browser accepts cookies.
- Clear your browser cache and cookies.

### Common Issues

- **Database Migration Issues:** Ensure all migrations are applied and the database is up to date.
- **Static Files Not Loading:** Run `python manage.py collectstatic` and ensure your static files are correctly configured.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

