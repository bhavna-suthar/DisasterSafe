DisasterSafe Local Package

FILES
- DisasterSafe.html       Main application
- report.html             Saved reports dashboard
- server.py               Local web server
- start.bat                Windows one-click launcher

HOW TO RUN
1. Keep all four files in the same folder.
2. Double-click start.bat.
3. The browser opens http://localhost:8000/DisasterSafe.html.
4. Submit reports normally.
5. Click Reports in the navbar or open http://localhost:8000/report.html.

IMPORTANT
The reports dashboard uses localStorage. Both pages must be served from the same localhost origin.
Reports that existed only in old file:// browser-history URLs cannot be automatically imported into localStorage.
Do not use this local demo as a production emergency database.
