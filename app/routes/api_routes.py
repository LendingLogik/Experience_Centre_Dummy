# from flask import Blueprint, jsonify
# from app.utils.database import get_experience_data, get_visitor_stats, get_location_data

# bp = Blueprint('api', __name__, url_prefix='/api')

# @bp.route('/data')
# def get_data():
#     try:
#         data = get_experience_data()
#         return jsonify(data)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @bp.route('/stats')
# def get_stats():
#     try:
#         stats = get_visitor_stats()
#         return jsonify(stats)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @bp.route('/location/<location>')
# def get_location(location):
#     try:
#         data = get_location_data(location)
#         return jsonify(data)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
