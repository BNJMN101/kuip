# Discovery MVP

A small mobile-friendly Django app that combines:
- Opportunities (scholarships, internships, competitions, events)
- Discover (useful resources, services, recommendations)
- Requests (things people need help finding)

## Run locally

Use Python 3.11+ if available.

### Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations discover
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

If PowerShell blocks activation, run:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py makemigrations discover
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

## What works in this first MVP
- Browse posts in one feed
- Filter by Opportunities, Discover, or Requests
- Search titles and descriptions
- Create a post
- Optional deadline and source/contact link
- Basic server-side validation
- Django admin for managing posts

## Admin
Create an admin account:
```powershell
python manage.py createsuperuser
```
Then open http://127.0.0.1:8000/admin/

## Important limitations
This is a local prototype, not ready for public launch.
- No user accounts or ownership controls in the public interface yet.
- No comments, messaging, notifications, or automated verification.
- A source link does not mean a listing is verified.
- Before public deployment, add authentication, abuse reporting/moderation, privacy protections, tests, and production settings.

## Next build step
Run it locally first. Then we can add user accounts and report/moderation features without making the first version unnecessarily complicated.
