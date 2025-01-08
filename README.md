# Country-Stats-Game
A Flask-based web game where players compare country statistics like GDP, population, GDP per capita, or area. The goal is to correctly choose which country has the higher value for the given statistic and build the longest streak possible.

I currently have it up on the web here: https://markperry87.pythonanywhere.com/

## Features
- Compare countries based on randomly chosen statistics.
- Tracks your streak of correct guesses
- Submit your high score and view the leaderboard.

### Prerequisites
- Python 3.8 or higher
- Flask
- Pandas

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Structure</title>
    <style>
        pre {
            font-family: monospace;
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Project Structure</h1>
    <pre>
country-stats-game/
├── app.py            # Main Flask application
├── cleaned_stats.csv # Data file with country statistics
├── high_scores.json  # JSON file to store high scores (created by the app)
├── templates/        # Directory for HTML templates
│   ├── game.html     # Game interface template
│   └── game_over.html# Game over template
└── README.md         # Project README file
    </pre>
</body>
</html>
