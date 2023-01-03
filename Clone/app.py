import os

from website import create_app
from waitress import serve

app = create_app()

if __name__ == '__main__':
    print("RUNNING WITH no WAITRESS")

    app.run(debug=True, host="0.0.0.0")
