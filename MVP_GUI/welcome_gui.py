from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect
from PyQt6.QtGui import QFont, QPixmap, QPalette, QBrush, QTransform, QPainter
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
        # self.setStyleSheet("background-color: #f4f4f9;")

        # Ustawienie zdjęcia w tle
        self.set_background_image('tlo.jpg')

        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        text_layout = QVBoxLayout()

        self.welcome_label1 = QLabel('Wybierz', self)
        self.welcome_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label1.setFont(QFont('Helvetica', 40, QFont.Weight.Bold))
        self.welcome_label1.setStyleSheet("color: #282432; padding: 5px;")

        self.welcome_label2 = QLabel('SWOJĄ', self)
        self.welcome_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label2.setFont(QFont('Helvetica', 48, QFont.Weight.Bold))
        self.welcome_label2.setStyleSheet("color: #282432; padding: 8px;")
        
        self.welcome_label3 = QLabel('przyszłość!', self)
        self.welcome_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label3.setFont(QFont('Helvetica', 40, QFont.Weight.Bold))
        self.welcome_label3.setStyleSheet("color: #282432; padding: 5px;")
                
        text_layout.addWidget(self.welcome_label1)
        text_layout.addWidget(self.welcome_label2)
        text_layout.addWidget(self.welcome_label3)
        layout.addLayout(text_layout)
        
        # self.welcome_label = QLabel('Wybierz <br> swoją <br> przyszłość!', self)
        # self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.welcome_label.setFont(QFont('Helvetica', 40, QFont.Weight.Bold))
        # self.welcome_label.setStyleSheet("color: #282432; padding: 50px;")
        # layout.addWidget(self.welcome_label)

        # Rozpocznij 
        self.start_button = QPushButton("Rozpocznij ➔")
        self.start_button.setFont(QFont('Arial', 18, QFont.Weight.Bold))
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #AFC2C9;
                color: #282432;
                border: none;
                padding: 20px;
                border-radius: 12px;
                margin-top: 50px;
            }
            QPushButton:hover {
                background-color: #87969C;
            }
        """)
        self.start_button.clicked.connect(self.open_study_choice)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.center_window()

# Dostosowanie obrazu do wiekszych ekranów
    def set_background_image(self, image_path):
        original_pixmap = QPixmap(image_path)
        scaled_pixmap = original_pixmap.scaled(self.size(), 
        Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)

        mirrored_horizontal = scaled_pixmap.transformed(QTransform().scale(-1, 1))  # Odbicie w poziomie
        mirrored_vertical = scaled_pixmap.transformed(QTransform().scale(1, -1))  # Odbicie w pionie
        mirrored_both = scaled_pixmap.transformed(QTransform().scale(-1, -1))  # Odbicie w obu osiach
        
        # Tworzymy nowy obraz 
        combined_pixmap = QPixmap(scaled_pixmap.width() * 2, scaled_pixmap.height() * 2)
        painter = QPainter(combined_pixmap)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.drawPixmap(scaled_pixmap.width(), 0, mirrored_horizontal)# obraz po prawej
        painter.drawPixmap(0, scaled_pixmap.height(), mirrored_vertical) # obraz na dole
        painter.drawPixmap(scaled_pixmap.width(), scaled_pixmap.height(), mirrored_both) # prawy dolny rog
        painter.end()

        # Ustawiamy nowy obraz jako tło
        brush = QBrush(combined_pixmap)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, brush) 
        self.setPalette(palette)

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
        