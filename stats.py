import sqlite3

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class StatsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Statistics")
        self.setGeometry(400, 200, 400, 300)

        layout = QVBoxLayout()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM players")
        total_players = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM matches")
        total_matches = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(goals) FROM players")

        total_goals = cursor.fetchone()[0]

        if total_goals is None:
            total_goals = 0

        cursor.execute("""
            SELECT name, goals
            FROM players
            ORDER BY CAST(goals AS INTEGER) DESC
            LIMIT 1
        """)

        top_scorer = cursor.fetchone()

        connection.close()

        if top_scorer:
            top_scorer_text = (
                f"{top_scorer[0]} ({top_scorer[1]} goals)"
            )
        else:
            top_scorer_text = "No Players"

        self.players_label = QLabel(
            f"Total Players: {total_players}"
        )

        self.matches_label = QLabel(
            f"Total Matches: {total_matches}"
        )

        self.goals_label = QLabel(
            f"Total Goals: {total_goals}"
        )

        self.top_scorer_label = QLabel(
            f"Top Scorer: {top_scorer_text}"
        )

        layout.addWidget(self.players_label)
        layout.addWidget(self.matches_label)
        layout.addWidget(self.goals_label)
        layout.addWidget(self.top_scorer_label)

        self.setLayout(layout)
