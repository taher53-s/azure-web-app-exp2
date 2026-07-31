import os
from flask import Flask, render_template

app = Flask(__name__)

# Premium Configuration


@app.route('/')
def index():
    """Main landing page for the premium app."""
    features = [
        {"title": "Azure Ready", "description": "Pre-configured for Azure App Service deployment.", "icon": "☁️"},
        {"title": "Premium UI", "description": "Clean, modern design using Tailwind CSS.", "icon": "✨"},
        {"title": "Scalable", "description": "Built on Flask, ready for growth and customization.", "icon": "🚀"}
    ]
    return render_template('index.html', features=features)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', error="404 - Page Not Found"), 404

if __name__ == '__main__':
    # For local development
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
