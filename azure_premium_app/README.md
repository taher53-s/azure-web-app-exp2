# Premium Azure Python Web App

This is a professional Flask boilerplate pre-configured for **Azure App Service**.

## Features
- **Azure Ready**: Includes `requirements.txt` and optimized entry point.
- **Premium UI**: Modern landing page built with Tailwind CSS.
- **Scalable Structure**: Clean separation of concerns.

## Local Development
1. Create a virtual environment: `python -m venv venv`
2. Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python app.py`

## Azure Deployment Instructions

### Option 1: Azure CLI (Quickest)
1. Zip the contents of this folder.
2. Run: `az webapp up --sku B1 --name <your-app-name>`

### Option 2: Azure Portal
1. Create a new **Web App** in the Azure Portal.
2. Choose **Python 3.11** (or higher) as the runtime.
3. In the **Deployment Center**, select your source (e.g., GitHub or Local Git).
4. Azure will automatically detect `app.py` and install dependencies from `requirements.txt`.

### Configuration Note
Azure App Service for Linux uses **Gunicorn** by default. It will look for `app:app` or `application:app`. This project uses `app.py` with an `app` object, which matches Azure's default expectations.
