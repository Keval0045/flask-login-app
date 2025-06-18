
# Flask Login App

This is a simple Flask web application demonstrating user authentication using Flask-Login.  
The app supports user registration, login, logout, and a protected dashboard page.

---

## Features

- User Registration (username + password)  
- User Login and Logout  
- Protected Dashboard accessible only to logged-in users  
- Password hashing using Werkzeug  
- Flask-Login integration for session management

---

## Project Structure

```
flask-login-app/
│
├── app.py                  # Main Flask app file
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── README.md               # This file
```

---

## Prerequisites

- Python 3.10+ installed  
- Virtual environment tool (`venv` recommended)  
- Git installed if using version control

---

## Setup and Installation

1. Clone the repository:  
```bash
git clone <your-repo-url>
cd flask-login-app
```

2. Create and activate a virtual environment:  
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:  
```bash
pip install -r requirements.txt
```

4. Run the Flask app locally:  
```bash
python app.py
```

5. Open your browser and go to:  
```
http://127.0.0.1:5000
```

---

## Usage

- Navigate to `/register` to create a new user account.  
- Navigate to `/login` to sign in.  
- Once logged in, access the `/dashboard` page.  
- Use the logout link to sign out.

---

## Deployment on Azure Web App

1. Set deployment user credentials (one-time):  
```bash
az webapp deployment user set --user-name <your-username> --password <your-password>
```

2. Configure local git deployment for your app:  
```bash
az webapp deployment source config-local-git --name <app-name> --resource-group <resource-group-name>
```

3. Add Azure remote git URL to your repo:  
```bash
git remote add azure <deployment-git-url>
```

4. Push your code to Azure (make sure to push to `master` branch):  
```bash
git push azure main:master
```

5. After deployment, browse to your Azure app URL, e.g.:  
```
https://<app-name>.azurewebsites.net
```

---

## Challenges Faced and Solutions

### 1. Deployment branch mismatch error  
- **Problem:** Pushing to `main` branch caused deployment failure since Azure expected `master`.  
- **Solution:** Used `git push azure main:master` to explicitly push local `main` branch to remote `master`.

### 2. Missing Python dependencies on Azure  
- **Problem:** Azure didn’t have Flask-Login installed, causing import errors.  
- **Solution:** Added `requirements.txt` listing all dependencies and ensured Azure ran `pip install -r requirements.txt` during deployment.

### 3. Blank page after login on Azure  
- **Problem:** After deployment, only a single "Flask login app running!" message showed.  
- **Solution:** Added full Flask app code with proper routes and HTML templates to enable full functionality.

### 4. Missing logout button on dashboard  
- **Problem:** UI lacked logout link to allow users to sign out.  
- **Solution:** Added logout button in dashboard template linking to `/logout`.

### 5. Module not found error locally  
- **Problem:** `ModuleNotFoundError: No module named 'flask_login'` during local runs.  
- **Solution:** Installed missing packages inside virtual environment with `pip install flask-login`.

---

## Requirements File (`requirements.txt`)

```
Flask==2.3.2
Flask-Login==0.6.2
Werkzeug==2.3.7
```

---

## Author

Keval Trivedi

---
