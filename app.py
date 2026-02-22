from flask import Flask, render_template_string
import os
import datetime
import platform
import psutil # Ta biblioteka pokaże nam zużycie zasobów

app = Flask(__name__)

# Szablon strony HTML (wbudowany w kod dla uproszczenia)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Docker Monitor</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; padding: 20px; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        .stat { font-weight: bold; color: #e74c3c; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Monitor Kontenera Flask</h1>
        <p>System: <span class="stat">{{ system_info }}</span></p>
        <p>Czas serwera: <span class="stat">{{ current_time }}</span></p>
        <p>Zużycie CPU: <span class="stat">{{ cpu_usage }}%</span></p>
        <p>Klucz API z Jenkinsa: <span class="stat">{{ api_key }}</span></p>
        <hr>
        <h3>Pliki w katalogu /app:</h3>
        <ul>
            {% for file in files %}
                <li>{{ file }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    info = {
        "system_info": platform.system() + " " + platform.release(),
        "current_time": datetime.datetime.now().strftime("%H:%M:%S"),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "api_key": os.getenv('MY_API_KEY', 'Brak klucza!'),
        "files": os.listdir('.')
    }
    return render_template_string(HTML_TEMPLATE, **info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
