import sqlite3

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem
)


class MatchesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matches Management")
        self.setGeometry(400, 200, 700, 500)

        # Title
        self.title = QLabel("Matches Management")

        # Inputs
        self.opponent_input = QLineEdit()
        self.opponent_input.setPlaceholderText(
            "Opponent Team"
        )

        self.score_input = QLineEdit()
        self.score_input.setPlaceholderText(
            "Score Example: 3-1"
        )

        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText(
            "Match Date"
        )

        # Buttons
        self.add_button = QPushButton("Add Match")

        self.delete_button = QPushButton(
            "Delete Selected Match"
        )

        # Table
        self.table = QTableWidget()

        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels([
            "Opponent",
            "Score",
            "Date"
        ])

        # Button Actions
        self.add_button.clicked.connect(
            self.add_match
        )

        self.delete_button.clicked.connect(
            self.delete_match
        )

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(self.title)

        layout.addWidget(self.opponent_input)
        layout.addWidget(self.score_input)
        layout.addWidget(self.date_input)

        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)

        layout.addWidget(self.table)

        self.setLayout(layout)

        # Load Matches
        self.load_matches()

    def add_match(self):

        opponent = self.opponent_input.text()
        score = self.score_input.text()
        date = self.date_input.text()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO matches
            (opponent, score, date)
            VALUES (?, ?, ?)
        """, (
            opponent,
            score,
            date
        ))

        connection.commit()
        connection.close()

        self.load_matches()

        self.opponent_input.clear()
        self.score_input.clear()
        self.date_input.clear()

    def load_matches(self):

        self.table.setRowCount(0)

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM matches")

        matches = cursor.fetchall()

        connection.close()

        for row_number, match in enumerate(matches):

            self.table.insertRow(row_number)

            self.table.setItem(
                row_number,
                0,
                QTableWidgetItem(match[1])
            )

            self.table.setItem(
                row_number,
                1,
                QTableWidgetItem(match[2])
            )

            self.table.setItem(
                row_number,
                2,
                QTableWidgetItem(match[3])
            )

    def delete_match(self):

        current_row = self.table.currentRow()

        if current_row >= 0:

            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            cursor.execute("SELECT id FROM matches")

            matches = cursor.fetchall()

            match_id = matches[current_row][0]

            cursor.execute(
                "DELETE FROM matches WHERE id=?",
                (match_id,)
            )

            connection.commit()
            connection.close()

            self.load_matches()
