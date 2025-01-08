<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Country-Stats-Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        pre {
            font-family: monospace;
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        h1, h2, h3 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Country-Stats-Game</h1>
    <p>
        A Flask-based web game where players compare country statistics like GDP, population, GDP per capita, or area. 
        The goal is to correctly choose which country has the higher value for the given statistic and build the longest streak possible.
    </p>
    <p>
        I currently have it up on the web here: 
        <a href="https://markperry87.pythonanywhere.com/" target="_blank">https://markperry87.pythonanywhere.com/</a>
    </p>

    <h2>Features</h2>
    <ul>
        <li>Compare countries based on randomly chosen statistics.</li>
        <li>Tracks your streak of correct guesses.</li>
        <li>Submit your high score and view the leaderboard.</li>
    </ul>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.8 or higher</li>
        <li>Flask</li>
        <li>Pandas</li>
    </ul>

    <h2>Project Structure</h2>
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
