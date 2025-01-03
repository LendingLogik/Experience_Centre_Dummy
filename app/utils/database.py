# app/utils/database.py

import MySQLdb
from MySQLdb import Error
from flask import current_app
import logging
from typing import Dict, List, Any

class Database:
    def __init__(self):
        self.connection = None
        
    def connect(self):
        try:
            if not self.connection:
                self.connection = MySQLdb.connect(
                    host=current_app.config['MYSQL_HOST'],
                    user=current_app.config['MYSQL_USER'],
                    passwd=current_app.config['MYSQL_PASSWORD'],
                    db=current_app.config['MYSQL_DB'],
                    port=current_app.config['MYSQL_PORT']
                )
            return self.connection
        except Error as e:
            logging.error(f"Error connecting to MySQL: {e}")
            raise

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query: str, params=None) -> List[Dict[str, Any]]:
        try:
            connection = self.connect()
            cursor = connection.cursor(MySQLdb.cursors.DictCursor)
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                
            if query.lower().startswith(('insert', 'update', 'delete')):
                connection.commit()
                return cursor.lastrowid
            
            return cursor.fetchall()
            
        except Error as e:
            logging.error(f"Error executing query: {e}")
            connection.rollback()
            raise
        finally:
            cursor.close()

def get_experience_data() -> Dict[str, Any]:
    """
    Fetch experience center data from the database
    Returns: Dictionary containing experience center data
    """
    try:
        db = Database()
        # Example query - modify according to your database schema
        query = """
        SELECT 
            e.id,
            e.name,
            e.location,
            e.visitor_count,
            e.timestamp
        FROM experience_center_data e
        ORDER BY e.timestamp DESC
        LIMIT 10
        """
        
        results = db.execute_query(query)
        
        # Process the results into the format needed for visualization
        processed_data = {
            'x': [],  # timestamps
            'y': [],  # visitor counts
            'locations': [],
            'names': []
        }
        
        for row in results:
            processed_data['x'].append(row['timestamp'])
            processed_data['y'].append(row['visitor_count'])
            processed_data['locations'].append(row['location'])
            processed_data['names'].append(row['name'])
            
        return processed_data
        
    except Exception as e:
        logging.error(f"Error fetching experience data: {e}")
        # Return dummy data in case of database error
        return {
            'x': [1, 2, 3, 4, 5],
            'y': [10, 15, 13, 17, 20],
            'locations': ['Location A', 'Location B', 'Location C', 'Location D', 'Location E'],
            'names': ['Experience 1', 'Experience 2', 'Experience 3', 'Experience 4', 'Experience 5']
        }
    finally:
        db.close()

# Additional helper functions for specific data needs
def get_visitor_stats() -> Dict[str, int]:
    """
    Get visitor statistics
    Returns: Dictionary containing visitor stats
    """
    try:
        db = Database()
        query = """
        SELECT 
            COUNT(*) as total_visitors,
            AVG(visitor_count) as avg_visitors
        FROM experience_center_data
        """
        
        results = db.execute_query(query)
        return results[0] if results else {'total_visitors': 0, 'avg_visitors': 0}
        
    except Exception as e:
        logging.error(f"Error fetching visitor stats: {e}")
        return {'total_visitors': 0, 'avg_visitors': 0}
    finally:
        db.close()

def get_location_data(location: str) -> List[Dict[str, Any]]:
    """
    Get data for a specific location
    Args:
        location: Location name
    Returns: List of data points for the location
    """
    try:
        db = Database()
        query = """
        SELECT *
        FROM experience_center_data
        WHERE location = %s
        ORDER BY timestamp DESC
        """
        
        return db.execute_query(query, (location,))
        
    except Exception as e:
        logging.error(f"Error fetching location data: {e}")
        return []
    finally:
        db.close()

# Create the necessary database tables if they don't exist
def init_database():
    try:
        db = Database()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS experience_center_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            visitor_count INT DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """
        
        db.execute_query(create_table_query)
        logging.info("Database tables initialized successfully")
        
    except Exception as e:
        logging.error(f"Error initializing database: {e}")
        raise
    finally:
        db.close()

# Function to insert sample data
def insert_sample_data():
    try:
        db = Database()
        sample_data = [
            ('Experience A', 'Location 1', 150),
            ('Experience B', 'Location 2', 200),
            ('Experience C', 'Location 3', 175),
            ('Experience D', 'Location 4', 225),
            ('Experience E', 'Location 5', 190)
        ]
        
        insert_query = """
        INSERT INTO experience_center_data (name, location, visitor_count)
        VALUES (%s, %s, %s)
        """
        
        for data in sample_data:
            db.execute_query(insert_query, data)
            
        logging.info("Sample data inserted successfully")
        
    except Exception as e:
        logging.error(f"Error inserting sample data: {e}")
        raise
    finally:
        db.close()
