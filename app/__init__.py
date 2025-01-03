from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import os
# from app.utils.database import init_database, insert_sample_data

# db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = os.environ.get('FLASK_SECRET_KEY')  # Make sure this is set
    
    # db.init_app(app)

    # with app.app_context():
    #     # Initialize database and create tables
    #     init_database()
        
    #     # Insert sample data (comment out in production)
    #     try:
    #         insert_sample_data()
    #     except Exception as e:
    #         app.logger.warning(f"Sample data may already exist: {e}")

    from app.routes import main_routes, dev_main_routes, api_routes, auth_routes
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(dev_main_routes.bp)
    # app.register_blueprint(salesforce_routes.app)
    # app.register_blueprint(api_routes.bp)
    # app.register_blueprint(auth_routes.bp)

    return app
