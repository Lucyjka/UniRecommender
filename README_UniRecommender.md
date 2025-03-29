### UniRecommender
Aplikacja "Wybierz swoją przyszłość" oparta na technologiach AI, stworzona z użyciem modelu LLM Google Gemini.

Korzysta z bazy danych Krajowego Rejestru Uczelni Wyższych w Polsce, a na jej podstawie i własnego treningu tworzy rekomendacje na podstawie zapytań użytkownika.

# Konfiguracja
1. Wygeneruj klucz API ze strony Google 
2. Stwórz plik `.env`
3. Wpisz w nim: GEMINI_API_KEY="twoj_klucz_api"

# Wprowadzenie

Aplikacja "Wybierz swoją przyszłość" ma na celu pomóc przyszłym studentom znaleźć odpowiednie kierunki studiów, na podstawie wybranych preferencji. Te preferencje to: 
-> **Lokalizacja** (miasto)
-> **Profil studiów** (praktyczny/ogólnoakademicki/dowolny)
-> **Stopień studiów** (I stopnia, II stopnia, jednolite magisterskie)
-> **Rodzaj uczelni** (publiczna, niepubliczna, kościelna)
-> **Zainteresowania** (np. programowanie, sztuka lub inne własne)

Aplikacja najpierw zawęża wyniki na podstawie wybranych kryteriów, a następnie AI analizuje pozostałe dane, tak, aby dobrać najbardziej pasujące kierunki do zainteresowań użytkownika.

# Interfejs użytkownika
**Ekran powitalny**
Użytkownik może rozpocząć spersonalizowane wyszukiwanie poprzez kliknięcie przycisku "Rozpocznij ->".
![alt text](image.png)

**Wybór Studiów - Formularz główny**
![alt text](image-1.png)

-> Pole *Podaj miasto:* 
Użytkownik aplikacji ma możliwość wpisania wybranego przez siebie miasta. W przypadku błędnie wpisanego miasta, tj. literówki, braku znaków polskich np. "krakow", aplikacja domyślnie poprawi na poprawną nazwę Miasta.

-> Pole *Profil studiów:* - menu rozwijane
Możliwe opcje do wyboru: Dowolny, Praktyczny, Ogólnoakademicki

-> Pole *Stopień studiów:*
Możliwość wyboru z menu rozwijanego spośród: Pierwszego stopnia, Drugiego stopnia, Jednolite magisterskie

-> Pole *Rodzaj uczelni:*
Aplikacja oferuje wybór rodzaju uczelni spośród: Dowolna, Uczelnia publiczna, Uczelnia niepubliczna, Uczelnia kościelna

-> Pole *Podaj swoje zainteresowania:*
Istnieje możliwośc wyborów spośród gotowych, najczęstszych zainteresowań: Programowanie, Muzyka, Sztuka, Sport, bądź teź wpisania samemu innego zainteresowania

Aby sfinalizować wyszukiwania, użytkownik używa przycisku "Znajdź kierunki studiów".
Pojawia się pasek sygnalizujący przeszukiwanie danych:
![alt text](image-2.png)

A następnie użytkownik otrzymuje wyniki: 
![alt text](image-3.png)

# Etyka AI i Ochrona Danych Użytkownika 

**Bezstronność**: Algorytm nie faworyzuje żadnej uczelni.
**Transparentność**: Wyjaśnienie, jak działają rekomendacje.
**Ograniczenia**: AI może nie znać wszystkich niszowych kierunków.
**Bezpieczeństwo**: Brak logowania i śledzenia użytkowników, wprowadzone dane są przetwarzane lokalnie, brak gromadzenia historii wyszukiwań
**Odpowiedzialne użycie**: Aplikacja ta jest tylko i wyłącznie narzędziem pomocniczym. W celu upewnienia się co do ścieżki kształcenia zalecanym jest sprawdzenie dostępnej oferty studiów bezpośrednio na stronach uczelni. 

# Cel Aplikacji

Celem aplikacji jest pomoc w znalezieniu idealnego kierunku studiów. Obecnie wybór kierunków studiów jest bardzo szeroki na każdej uczelni, co może wprowadzać przyszłych studentów w zakłopotanie. Aplikacja może też pomóc osobom, które mniej więcej wiedzą na jaki kierunek chcą pójść, jednakże nie mają ochoty czy też czasu na przeglądanie wielu stron internetowych kilku/kilkunastu uczelni. Dodatkowo, wedle krytieriów Etyki AI aplikacja "Wybierz swoją przyszłość" dostarcza obiektywne rekomendacje, bez możliwości reklam poszczególnych uczelni. 


# Do kogo skierowana jest aplikacja "Wybierz swoją przyszłość"?

Aplikacja jest skierowana głównie do osób będących po maturach i stojących przed ciężkim i bardzo ważnym wyborem dalszej ścieżki kształcenia. Jednakże nie tylko maturzyści mogą korzystać z aplikacji "Wybierz swoją przyszłość"! Osoby chcące zmienić swój obecny kierunek studiów czy też znaleźć studia II stopnia, także mogą pomóc sobie w podjęciu tej decyzji. 

# Ważne uwagi

Aplikacja nie gwarantuje przyjęcia na studia! Wymaganym jest sprawdzenie wymagań na stronach uczelni. Wyniki uzyskane w trakcie zapytania należy traktować jako sugestię, a nie ostateczny wybór. Dodatkowo, pomimo że nasze dane są aktualizowane, uczelnie dopasowują kierunki do obecnych trendów na rynku, przez co niektóre kierunki mogą ulec zmianie.
