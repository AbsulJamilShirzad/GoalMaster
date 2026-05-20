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


class PlayersWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Players Management")
        self.setGeometry(400, 200, 700, 500)

        # Title
        self.title = QLabel("Players Management")

        # Inputs
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Player Name")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Player Age")

        self.position_input = QLineEdit()
        self.position_input.setPlaceholderText("Player Position")

        self.number_input = QLineEdit()
        self.number_input.setPlaceholderText("Jersey Number")

        self.goals_input = QLineEdit()
        self.goals_input.setPlaceholderText("Goals")

        # Buttons
        self.add_button = QPushButton("Add Player")

        self.delete_button = QPushButton(
            "Delete Selected Player"
        )

        self.update_button = QPushButton(
            "Update Selected Player"
        )

        # Table
        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Name",
            "Age",
            "Position",
            "Number",
            "Goals"
        ])

        # Button Actions
        self.add_button.clicked.connect(self.add_player)

        self.delete_button.clicked.connect(
            self.delete_player
        )

        self.update_button.clicked.connect(
            self.update_player
        )

        self.table.cellClicked.connect(
            self.select_player
        )

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(self.title)

        layout.addWidget(self.name_input)
        layout.addWidget(self.age_input)
        layout.addWidget(self.position_input)
        layout.addWidget(self.number_input)
        layout.addWidget(self.goals_input)

        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.update_button)

        layout.addWidget(self.table)

        self.setLayout(layout)

        # Load Players
        self.load_players()

    def add_player(self):

        name = self.name_input.text()
        age = self.age_input.text()
        position = self.position_input.text()
        number = self.number_input.text()
        goals = self.goals_input.text()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO players
            (name, age, position, number, goals)
            VALUES (?, ?, ?, ?, ?)
        """, (
            name,
            age,
            position,
            number,
            goals
        ))

        connection.commit()
        connection.close()

        self.load_players()

        self.name_input.clear()
        self.age_input.clear()
        self.position_input.clear()
        self.number_input.clear()
        self.goals_input.clear()

    def load_players(self):

        self.table.setRowCount(0)

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM players")

        players = cursor.fetchall()

        connection.close()

        for row_number, player in enumerate(players):

            self.table.insertRow(row_number)

            self.table.setItem(
                row_number,
                0,
                QTableWidgetItem(player[1])
            )

            self.table.setItem(
                row_number,
                1,
                QTableWidgetItem(player[2])
            )

            self.table.setItem(
                row_number,
                2,
                QTableWidgetItem(player[3])
            )

            self.table.setItem(
                row_number,
                3,
                QTableWidgetItem(player[4])
            )

            self.table.setItem(
                row_number,
                4,
                QTableWidgetItem(player[5])
            )

    def delete_player(self):

        current_row = self.table.currentRow()

        if current_row >= 0:

            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            cursor.execute("SELECT id FROM players")

            players = cursor.fetchall()

            player_id = players[current_row][0]

            cursor.execute(
                "DELETE FROM players WHERE id=?",
                (player_id,)
            )

            connection.commit()
            connection.close()

            self.load_players()

    def select_player(self):

        current_row = self.table.currentRow()

        self.name_input.setText(
            self.table.item(current_row, 0).text()
        )

        self.age_input.setText(
            self.table.item(current_row, 1).text()
        )

        self.position_input.setText(
            self.table.item(current_row, 2).text()
        )

        self.number_input.setText(
            self.table.item(current_row, 3).text()
        )

        self.goals_input.setText(
            self.table.item(current_row, 4).text()
        )

    def update_player(self):

        current_row = self.table.currentRow()

        if current_row >= 0:

            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            cursor.execute("SELECT id FROM players")

            players = cursor.fetchall()

            player_id = players[current_row][0]

            name = self.name_input.text()
            age = self.age_input.text()
            position = self.position_input.text()
            number = self.number_input.text()
            goals = self.goals_input.text()

            cursor.execute("""
                UPDATE players
                SET name=?,
                    age=?,
                    position=?,
                    number=?,
                    goals=?
                WHERE id=?
            """, (
                name,
                age,
                position,
                number,
                goals,
                player_id
            ))

            connection.commit()
            connection.close()

            self.load_players()
