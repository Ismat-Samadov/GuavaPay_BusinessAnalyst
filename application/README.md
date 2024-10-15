# GuavaPay Business Analyst Application

This is a Flask-based web application designed to manage commissions for Operations and Customer Support teams. The app allows users to set up and maintain standalone and group commissions, differentiated by time period, currency, and geo zones.

## Project Structure
```
├── application
│   ├── app.py                # Main Flask app
│   ├── Dockerfile            # Docker configuration
│   ├── fly.toml              # Fly.io configuration
│   ├── requirements.txt      # Dependencies
│   ├── static/               # Static assets (CSS, JS)
│   ├── templates/            # HTML templates
├── payload.json              # Example API request
├── response.json             # Example API response
```

## Features
- Set up standalone/group commissions.
- Time period, currency, geo zone differentiation.
- Responsive UI.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ismat-Samadov/GuavaPay_BusinessAnalyst.git
   cd GuavaPay_BusinessAnalyst/application
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   python app.py
   ```

4. Access the app:
   ```
   http://127.0.0.1:5000
   ```

## Deployment (Fly.io)

1. Install Fly.io CLI:
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. Login and deploy:
   ```bash
   flyctl auth login
   flyctl deploy
   ```

## Usage
- Navigate to the web interface and fill out the commission form.
- Submit to create and view commission structures.

## License
MIT
