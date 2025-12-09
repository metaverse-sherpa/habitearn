## HabitEarn – Local Setup Quick Reference

1. **Choose Python 3.11.13**
   - Ensure Homebrew’s interpreter is available: `/opt/homebrew/opt/python@3.11/bin/python3.11`.

2. **Create the virtual environment (once per checkout)**
   ```bash
   /opt/homebrew/opt/python@3.11/bin/python3.11 -m venv .venv
   ```

3. **Activate the environment (every shell session)**
   ```bash
   source .venv/bin/activate
   ```
   - Confirm with `python --version` → `Python 3.11.13`.

4. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Environment variables**
   - Create `.env` next to `manage.py` (if it doesn’t exist):
     ```
     SECRET_KEY=your-dev-secret
     DEBUG=True
     DEPLOY=False
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

6. **Database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   - Visit `http://127.0.0.1:8000/`.

8. **Admin access (optional)**
   ```bash
   python manage.py createsuperuser
   ```
   - Log in at `http://127.0.0.1:8000/admin/`.

9. **Deactivate when done**
   ```bash
   deactivate
   ```

Keep `.venv/` ignored in git so you don’t sync the virtual environment.
