from flask import redirect, url_for
from core import create_app,init_app

if __name__ == '__main__':
    app = create_app()
    init_app()

    app.run(debug=True)
