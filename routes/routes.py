from flask import Blueprint, request, jsonify
import numpy as np

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    result = len(text)
    return jsonify({
        'input_length': result,
        'message': 'This is a simple AI API with many dependencies.'
    })

@api_bp.route('/api/random', methods=['GET'])
def random():
    return jsonify({
        'random_number': np.random.rand(),
        'message': 'Random number generated using NumPy.'
    })

@api_bp.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({
        'echo': data,
        'message': 'This endpoint echoes the input data.'
    })

@api_bp.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'The API is up and running.'
    })

