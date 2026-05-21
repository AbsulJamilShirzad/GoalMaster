from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from dashboard import DashboardWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" GoalMaster Login")
        self.setGeometry(500, 200, 300, 200)

        self.title = QLabel("Football Team Manager")
        self.title.setStyleSheet(
            "font-size: 28px; font-weight: bold; color:#00aaff;")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")

        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):

        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "1234":

            self.dashboard = DashboardWindow()
            self.dashboard.show()

            self.close()

        else:
            QMessageBox.warning(
                self,
                "Error",
                "Wrong Username or Password"
            )
