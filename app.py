from flask import Flask, render_template, request, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from predictor import ImprovedPredictor

app = Flask(__name__)
predictor = ImprovedPredictor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Run prediction
        prediction = predictor.analyze_match(url, silent=True)
        
        if not prediction:
            return jsonify({'error': 'Failed to analyze match'}), 500
        
        # Format response
        response = {
            'success': True,
            'match': {
                'home_team': prediction.home_team,
                'away_team': prediction.away_team
            },
            'prediction': {
                'home_prob': round(prediction.home_prob, 1),
                'away_prob': round(prediction.away_prob, 1),
                'draw_prob': round(prediction.draw_prob, 1),
                'recommended_bet': prediction.recommended_bet,
                'confidence': prediction.confidence,
                'reasoning': prediction.reasoning
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/learn', methods=['POST'])
def learn():
    try:
        data = request.get_json()
        url = data.get('url')
        result = data.get('result')
        
        if not url or not result:
            return jsonify({'error': 'URL and result are required'}), 400
        
        # Get prediction first
        prediction = predictor.analyze_match(url, silent=True)
        if prediction and prediction.recommended_bet:
            predictor.record_result(prediction, result)
            return jsonify({'success': True, 'message': 'Result recorded for learning'})
        else:
            return jsonify({'error': 'No prediction to learn from'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
