from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from players import PlayersWindow
from matches import MatchesWindow
from stats import StatsWindow


class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GoalMaster Dashboard")
        self.setGeometry(500, 200, 400, 300)

        # Title
        self.title = QLabel("GoalMaster Dashboard")

        # Buttons
        self.players_button = QPushButton("Players")
        self.matches_button = QPushButton("Matches")
        self.stats_button = QPushButton("Statistics")
        self.exit_button = QPushButton("Exit")

        # Button Actions
        self.players_button.clicked.connect(
            self.open_players
        )

        self.stats_button.clicked.connect(
            self.open_stats
        )

        self.matches_button.clicked.connect(
            self.open_matches
        )

        self.exit_button.clicked.connect(
            self.close
        )

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.players_button)
        layout.addWidget(self.matches_button)
        layout.addWidget(self.stats_button)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def open_players(self):

        self.players_window = PlayersWindow()
        self.players_window.show()

    def open_matches(self):

        self.matches_window = MatchesWindow()
        self.matches_window.show()

    def open_stats(self):

        self.stats_window = StatsWindow()
        self.stats_window.show()
