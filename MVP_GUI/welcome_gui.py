from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from app_gui import StudyChoiceApp

# Okno powitalne
class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Witamy!")
        self.resize(800, 800)
        self.setStyleSheet("background-color: #f4f4f9;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.welcome_label = QLabel("Wybierz swoją przyszłość!", self)
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        self.welcome_label.setStyleSheet("color: #333333; padding: 20px;")
        layout.addWidget(self.welcome_label)

        self.start_button = QPushButton("Rozpocznij")
        self.start_button.setFont(QFont('Arial', 21, QFont.Weight.Bold))
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #6699ff;
                color: white;
                border: none;
                padding: 15px 32px;
                font-size: 16px;
                border-radius: 12px;
                margin-top: 30px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.start_button.clicked.connect(self.open_study_choice)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.center_window()

    def center_window(self):
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)

# Przeniesienie do głównego okna aplikacji
    def open_study_choice(self):
        self.study_choice_window = StudyChoiceApp()
        self.study_choice_window.setGeometry(self.geometry())
        self.study_choice_window.show()
        self.animate_transition(self.study_choice_window)

# Animacja przejscia do okna z wyborem studiów
    def animate_transition(self, window):
        current_geometry = self.geometry()
        new_width = current_geometry.width()
        new_height = current_geometry.height()

        exit_animation = QPropertyAnimation(self, b"geometry")
        exit_animation.setDuration(600)
        exit_animation.setStartValue(current_geometry)
        exit_animation.setEndValue(QRect(current_geometry.x() - new_width, current_geometry.y(), new_width, new_height))
        exit_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        enter_animation = QPropertyAnimation(window, b"geometry")
        enter_animation.setDuration(600)
        enter_animation.setStartValue(QRect(current_geometry.x() + new_width, current_geometry.y(), new_width, new_height))
        enter_animation.setEndValue(current_geometry)
        enter_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        exit_animation.start()
        enter_animation.start()
        window.enter_animation = enter_animation
        self.exit_animation = exit_animation
        exit_animation.finished.connect(self.close)