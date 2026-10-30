# Kuip

Kuip is a community platform where people share and find useful things: opportunities, helpful resources, and requests for help. It's built for everyday people and university students in Nigeria, so a useful internship, scholarship or tip can reach the people who need it.

This is the first working MVP, built with Django.

## What works today

- Public welcome page that explains what Kuip is
- Sign up with a username, email and password (passwords are hashed, with Django's standard strength checks)
- Log in with either your username or your email
- Log out
- A feed of community posts with search and category filters (Opportunities, Discover, Requests)
- Create, view, edit and delete your own posts
- Every post is linked to its author, and only the author can edit or delete it
- Logged-out visitors are redirected to the login page for any private page
- Automated tests for login protection and post ownership

## Tech stack

- Python and Django
- SQLite (local development)
- HTML and CSS, using Django templates
- Django's built-in authentication

## Run it locally

You need Python 3.10 or newer and Git.

```powershell
git clone https://github.com/BNJMN101/kuip.git
cd kuip
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ and create an account from the sign-up page.

On Mac or Linux, activate the virtual environment with `source .venv/bin/activate` instead.

`python manage.py migrate` creates your local database. The database file is not stored in the repo, so every machine starts with an empty one.

## Run the tests

```powershell
python manage.py test
```

## Project layout

- `config/`: project settings and the main URL list
- `accounts/`: sign up, log in, log out
- `discover/`: the feed and posts
- `templates/`: HTML pages
- `static/`: CSS and images

## Notes

- This is an early MVP for local development, not production.
- The secret key in `config/settings.py` can be overridden with the `DJANGO_SECRET_KEY` environment variable. Set a real one before deploying anywhere.

## Roadmap

- Comments on posts
- User profiles and saved posts
- A redesigned, multi-page welcome site
- Sign in with Google