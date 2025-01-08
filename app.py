from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import random
import json
import os

app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"  # Needed for session handling

# Load the cleaned CSV file
data = pd.read_csv("cleaned_stats.csv")

# JSON file path for high scores
HIGH_SCORES_FILE = "high_scores.json"

def load_high_scores():
    """Load high scores from JSON file; return as list of dicts (e.g., [{'name': 'Alice', 'score': 5}, ...])."""
    if os.path.exists(HIGH_SCORES_FILE):
        with open(HIGH_SCORES_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_high_scores(high_scores):
    """Save the high scores list of dicts back to JSON."""
    with open(HIGH_SCORES_FILE, "w") as f:
        json.dump(high_scores, f)

@app.route("/")
def home():
    # Initialize streak if not set
    if "streak" not in session:
        session["streak"] = 0

    # List of possible stats to compare
    stats = ["GDP", "Population", "GDP_per_capita", "Area"]

    # Randomly select a stat for this round
    chosen_stat = random.choice(stats)

    # Randomly select two countries
    country_pair = data.sample(2).to_dict(orient="records")
    country1, country2 = country_pair[0], country_pair[1]

    # Store chosen_stat in session so we know which stat to compare in /check
    session["chosen_stat"] = chosen_stat

    return render_template(
        "game.html",
        country1=country1["Country"],
        country2=country2["Country"],
        variable=chosen_stat,              # Send the chosen stat to the template
        streak=session["streak"]           # Pass current streak to template
    )

@app.route("/check", methods=["POST"])
def check():
    selected_country = request.form["country"]
    other_country = request.form["other_country"]

    # Retrieve the chosen stat from the session
    chosen_stat = session.get("chosen_stat", "GDP_per_capita")

    try:
        # Get the chosen_stat values for the selected and other countries
        selected_value = data.loc[data["Country"] == selected_country, chosen_stat].values[0]
        other_value = data.loc[data["Country"] == other_country, chosen_stat].values[0]

        # Compare the values
        if selected_value > other_value:
            # Correct answer: increment the streak
            session["streak"] = session.get("streak", 0) + 1
            return redirect(url_for("home"))
        else:
            # Wrong answer: get final streak, reset it, and go to game over
            final_streak = session["streak"]
            session["streak"] = 0
            return render_template("game_over.html", final_streak=final_streak, scoreboard=None)
    except IndexError:
        return "Error: Country data is missing or incorrect.", 500

@app.route("/submit_score", methods=["POST"])
def submit_score():
    """Handle player name & final streak from the game over page and update high scores."""
    player_name = request.form.get("player_name")
    final_streak = int(request.form.get("final_streak", 0))

    # Load existing scores
    high_scores = load_high_scores()

    # Add new score
    high_scores.append({"name": player_name, "score": final_streak})

    # Sort by score descending
    high_scores.sort(key=lambda s: s["score"], reverse=True)

    # Keep only top 10
    high_scores = high_scores[:10]

    # Save updated scoreboard
    save_high_scores(high_scores)

    # Now show the game_over page again, but this time include the scoreboard
    return render_template("game_over.html", final_streak=final_streak, scoreboard=high_scores)

@app.route("/game_over")
def game_over():
    # This route might not be used now if we directly render `game_over.html` from /check,
    # but you can keep it for direct navigation or debugging.
    final_streak = session.get("streak", 0)
    return render_template("game_over.html", final_streak=final_streak, scoreboard=None)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)