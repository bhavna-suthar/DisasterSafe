from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser

ROOT = Path(__file__).resolve().parent
PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

url = f"http://localhost:{PORT}/index.html"
print("DisasterSafe is running at:", url)
print("Reports dashboard:", f"http://localhost:{PORT}/report.html")
print("Keep this window open while using the app.")
webbrowser.open(url)
ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
