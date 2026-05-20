import sys

from PySide6.QtWidgets import QApplication

from login import LoginWindow
from database import connect_db

# Create Database
connect_db()

app = QApplication(sys.argv)

# App Style
app.setStyleSheet("""

QWidget {
    background-color: #1e1e1e;
    color: white;
    font-size: 16px;
}

QPushButton {
    background-color: #2d89ef;
    color: white;
    border-radius: 10px;
    padding: 10px;
}

QPushButton:hover {
    background-color: #1b5fbf;
}

QLineEdit {
    background-color: #2b2b2b;
    border: 2px solid #444;
    border-radius: 8px;
    padding: 8px;
    color: white;
}

QTableWidget {
    background-color: #2b2b2b;
    gridline-color: #555;
}

QHeaderView::section {
    background-color: #444;
    color: white;
    padding: 5px;
}

""")

window = LoginWindow()
window.show()

sys.exit(app.exec())
