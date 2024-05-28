from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from ab_testing.routes import initialize_routes
initialize_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
