# Football Predictor Web App

A web-based football match predictor using Playwright for data extraction and machine learning for predictions.

## Features

- 🔮 **Match Prediction**: Analyze Forebet URLs for match predictions
- 📊 **Visual Probabilities**: Interactive probability bars
- 🎯 **Smart Recommendations**: Always provides actionable betting advice
- 📚 **Manual Learning**: Improve predictions by adding actual results
- 🌐 **Web Interface**: Clean, responsive design

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```

2. Run the app:
```bash
python app.py
```

3. Open http://localhost:8000

## Deployment

This app is configured for Railway deployment with Playwright support.

### Deploy to Railway:

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Dockerfile
3. Deploy and get your free `.railway.app` URL

## Usage

1. Paste a Forebet match URL
2. Click "Predict Match"
3. View probabilities and recommendation
4. Add actual results for learning (optional)

## API Endpoints

- `POST /predict` - Get match prediction
- `POST /learn` - Record actual result for learning
