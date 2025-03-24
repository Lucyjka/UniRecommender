from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QComboBox, QTextEdit, QCheckBox, QApplication, QProgressBar)
from application import get_recommendations
from PyQt6.QtCore import QThread, pyqtSignal


# Klasa wątku - obsługuje rekomendacje w tle
class RecommendationThread(QThread):
    results_ready = pyqtSignal(list)
    error_signal = pyqtSignal(str)

    def __init__(self, city, profile, level, institution_kind, interests):
        super().__init__()
        self.city = city
        self.profile = profile
        self.level = level
        self.institution_kind = institution_kind
        self.interests = interests

    def run(self):
        try:
            results = get_recommendations(self.city, self.profile, self.level, self.institution_kind, self.interests)

            if isinstance(results, str):
                results = [results]

            self.results_ready.emit(results)
        except Exception as e:
            self.error_signal.emit(str(e))


# Okno wyboru studiów
class StudyChoiceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Wybór Studiów")
        self.resize(800, 800)

        # bez niczego jest dark
        self.setStyleSheet("background-color: #F6F2EF; color: #282432;")# light 
        self.center_window()

        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(15)  # Odstęp między widgetami
        layout.setContentsMargins(35, 25, 35, 25)  # Marginesy wokół układu

        # Nagłówek
        header = QLabel("Wybierz swoją ścieżkę kariery!", self)
        header.setFont(QFont('Helvetica', 18, QFont.Weight.Bold))
        
        # light
        # header.setStyleSheet("color: #F6F2EF; background-color: #282432; padding: 10px; border-radius:20px;")
        # dark
        header.setStyleSheet("color: #282432; background-color: #AFC2C9; padding: 10px; border-radius:20px;")
        
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)


        # Wiersz 1: Miasto i Profil studiów
        city_profile_layout = QHBoxLayout()
        city_profile_layout.setSpacing(20)  # Odstęp między polami

        # Miasto
        city_layout = QVBoxLayout()
        city_layout.setSpacing(0)
        self.city_label = QLabel("Podaj miasto:")
        self.city_label.setFont(QFont('Helvetica', 14))
        city_layout.addWidget(self.city_label)
        self.city_input = QLineEdit()
        self.city_input.setFont(QFont('Helvetica', 12))
        self.city_input.setSizePolicy(self.city_input.sizePolicy().horizontalPolicy(),
                                      self.city_input.sizePolicy().verticalPolicy())
        city_layout.addWidget(self.city_input)
        city_profile_layout.addLayout(city_layout, 1)

        # Profil studiów
        profile_layout = QVBoxLayout()
        profile_layout.setSpacing(0)
        self.profile_label = QLabel("Profil studiów:")
        self.profile_label.setFont(QFont('Helvetica', 14))
        profile_layout.addWidget(self.profile_label)
        self.profile_input = QComboBox()
        self.profile_input.setFont(QFont('Helvetica', 12))
        self.profile_input.addItems(["Dowolny", "Praktyczny", "Ogólnoakademicki"])
        self.profile_input.setSizePolicy(self.profile_input.sizePolicy().horizontalPolicy(),
                                         self.profile_input.sizePolicy().verticalPolicy())
        profile_layout.addWidget(self.profile_input)
        city_profile_layout.addLayout(profile_layout, 1)

        layout.addLayout(city_profile_layout)


        # Wiersz 2: Stopień studiów i Rodzaj uczelni
        level_inst_layout = QHBoxLayout()
        level_inst_layout.setSpacing(20)  # odstęp między polami

        # Stopień studiów
        level_layout = QVBoxLayout()
        level_layout.setSpacing(0)
        self.level_label = QLabel("Stopień studiów:")
        self.level_label.setFont(QFont('Helvetica', 14))
        level_layout.addWidget(self.level_label)
        self.level_input = QComboBox()
        self.level_input.setFont(QFont('Helvetica', 12))
        self.level_input.addItems(["Pierwszego stopnia", "Drugiego stopnia", "Jednolite magisterskie"])
        level_layout.addWidget(self.level_input)
        level_inst_layout.addLayout(level_layout)

        # Rodzaj uczelni
        institution_layout = QVBoxLayout()
        institution_layout.setSpacing(0)
        self.institution_label = QLabel("Rodzaj uczelni:")
        self.institution_label.setFont(QFont('Helvetica', 14))
        institution_layout.addWidget(self.institution_label)
        self.institution_input = QComboBox()
        self.institution_input.setFont(QFont('Helvetica', 12))
        self.institution_input.addItems(
            ["Dowolna", "Uczelnia publiczna", "Uczelnia niepubliczna", "Uczelnia kościelna"])
        institution_layout.addWidget(self.institution_input)
        level_inst_layout.addLayout(institution_layout)

        layout.addLayout(level_inst_layout)


        # Zainteresowania
        interest_layout = QVBoxLayout()
        interest_layout.setSpacing(0)
        self.interest_label = QLabel("Podaj swoje zainteresowania:")
        self.interest_label.setFont(QFont('Helvetica', 14))
        interest_layout.addWidget(self.interest_label)
        self.interest_input = QLineEdit()
        self.interest_input.setFont(QFont('Helvetica', 12))
        self.interest_input.setPlaceholderText("Wpisz swoje zainteresowania lub wybierz z poniższych")
        interest_layout.addWidget(self.interest_input)

        # Dodanie checkboxów z przykładowymi zainteresowaniami
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setSpacing(20)

        # Lista do przechowywania checkboxów
        self.interest_checkboxes = []

        # Funkcja obsługująca zmianę stanu checkboxa
        def on_interest_checkbox_toggled(checkbox, checked):
            if checked:
                for cb in self.interest_checkboxes:
                    if cb is not checkbox:
                        cb.blockSignals(True)
                        cb.setChecked(False)
                        cb.blockSignals(False)
                self.interest_input.setText(checkbox.text())
            else:
                if not any(cb.isChecked() for cb in self.interest_checkboxes):
                    self.interest_input.clear()

        # Checkbox 1: Programowanie
        checkbox1 = QCheckBox("Programowanie 🖥️")
        checkbox1.setFont(QFont('Helvetica', 12))
        checkbox1.toggled.connect(lambda checked, cb=checkbox1: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox1)
        checkbox_layout.addWidget(checkbox1)

        # Checkbox 2: Muzyka
        checkbox2 = QCheckBox("Muzyka 🎵")
        checkbox2.setFont(QFont('Helvetica', 12))
        checkbox2.toggled.connect(lambda checked, cb=checkbox2: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox2)
        checkbox_layout.addWidget(checkbox2)

        # Checkbox 3: Sztuka
        checkbox3 = QCheckBox("Sztuka 🎨")
        checkbox3.setFont(QFont('Helvetica', 12))
        checkbox3.toggled.connect(lambda checked, cb=checkbox3: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox3)
        checkbox_layout.addWidget(checkbox3)

        # Checkbox 4: Sport
        checkbox4 = QCheckBox("Sport ⚽")
        checkbox4.setFont(QFont('Helvetica', 12))
        checkbox4.toggled.connect(lambda checked, cb=checkbox4: on_interest_checkbox_toggled(cb, checked))
        self.interest_checkboxes.append(checkbox4)
        checkbox_layout.addWidget(checkbox4)

        # Styl dla checkboxów
        checkbox_style = """
            QCheckBox::indicator {
                background-color: #FDFDFB;
                border: 2px solid #AFC2C9;
                border-radius: 1px;
            }
            QCheckBox::indicator:checked {
                background-color: #7B9EA8;
                border: 2px solid #7B9EA8; 
                border-radius: 1px;
            }
        """

        checkbox1.setStyleSheet(checkbox_style)
        checkbox2.setStyleSheet(checkbox_style)
        checkbox3.setStyleSheet(checkbox_style)
        checkbox4.setStyleSheet(checkbox_style)

        interest_layout.addLayout(checkbox_layout)
        layout.addLayout(interest_layout)


        # Przycisk wyszukiwania 
        # background-color: #282432;  color: #F6F2EF; # light
        # background-color: #AFC2C9; color: #000000; # dark
        self.search_button = QPushButton("Znajdź kierunki studiów")
        self.search_button.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #AFC2C9; 
                color: #000000; 
                border: none;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #87969C;
            }
        """)
        self.search_button.clicked.connect(self.search)
        layout.addWidget(self.search_button)

        # Pasek ładowania
        progress_layout = QVBoxLayout()
        progress_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(0)
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        layout.addLayout(progress_layout)


        # Pole do wyświetlania wyników
        self.result_label = QLabel("Wyniki:")
        self.result_label.setFont(QFont('Helvetica', 14, ))
        layout.addWidget(self.result_label)
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setFont(QFont('Helvetica', 14))
        self.result_text.setStyleSheet("color: #282432; background-color: #FDFDFB; padding: 16px; border: 1px solid #AFC2C9; border-radius:20px;")
        layout.addWidget(self.result_text)


        # Styl pól wejsciowych
        input_style = """
            QLineEdit, QComboBox, QTextEdit, QHBoxLayout {
                background-color: #FDFDFB;  /* Jasne tło dla kontrastu */
                border: 1px solid #AFC2C9;  /* Delikatna ramka */
                border-radius: 8px;  /* Zaokrąglone rogi */
 
            }
            QLineEdit:focus, QComboBox:focus, QTextEdit:focus {
                border: 2px solid #7B9EA8;  /* Podkreślenie aktywnego pola */
                background-color: #FFFFFF;
            }
        """

        # Zastosowanie stylu do pól wejściowych
        self.city_input.setStyleSheet(input_style)
        self.profile_input.setStyleSheet(input_style)
        self.level_input.setStyleSheet(input_style)
        self.institution_input.setStyleSheet(input_style)
        self.interest_input.setStyleSheet(input_style)
        self.result_text.setStyleSheet(input_style)

        self.setLayout(layout)

    def center_window(self):
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)

    def search(self):
        city = self.city_input.text()
        profile = self.profile_input.currentText()
        level = self.level_input.currentText()
        institution_kind = self.institution_input.currentText()
        interests = self.interest_input.text()

        # Czyszczenie poprzednich wyników
        self.result_text.clear()

        # Pasek ładowania
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(30)

        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self.increment_progress)
        self.progress_timer.start(500)

        self.thread = RecommendationThread(city, profile, level, institution_kind, interests)
        self.thread.results_ready.connect(self.finish_search)
        self.thread.error_signal.connect(self.show_error)
        self.thread.start()



    def increment_progress(self):
        if self.progress_bar.value() < 90:
            self.progress_bar.setValue(self.progress_bar.value() + 5)

    def finish_search(self, results):
        self.progress_timer.stop()
        self.progress_bar.setValue(100)
        self.progress_bar.setVisible(False)

        # Formatowanie wyników
        if all(isinstance(item, str) and len(item) == 1 for item in results):
            formatted_results = "".join(results)
        else:
            formatted_results = "\n".join(map(str, results))

            # Wyświetlanie wyników
            # pogrubienie kierunkow i uczelni
            formatted_results = formatted_results.replace("Kierunek:", "<b><br><br>Kierunek:</b>").replace("Uczelnie:","<b><br>Uczelnie:</b>")
            # dodatkowa uwaga
            formatted_results += "<br><br><i>Proszę pamiętać, że wyniki mogą się różnić w zależności od dostępnych danych.</i>"
            # nowa linia dla uwagi
            formatted_results = formatted_results.replace("Uwaga:", "<br><br><b>UWAGA!</b>")
            # gdy "Nie znaleziono odpowiednich kierunków.." dodajemy nowa linie
            formatted_results = formatted_results.replace("Nie znaleziono", "<br><br>Nie znaleziono")
            # gdy znajduje ** w odpowiedzi (nieudane pogrubienie tekstu w result) to usuwa
            formatted_results = formatted_results.replace("**", "")
            formatted_results = formatted_results.replace("*", "")

        self.result_text.setHtml(formatted_results)

    def show_error(self, error_message):
        self.progress_timer.stop()
        self.progress_bar.setValue(100)
        self.progress_bar.setVisible(False)
        self.result_text.setHtml(f"<b style='color:red;'>Błąd:</b> {error_message}")
