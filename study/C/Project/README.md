# Symulacja miasteczka

## Krótki opis projektu:

Program symuluje rozrost miasteczka, pozwalając użytkownikowi zarządzać jego rozwojem. Po uruchomieniu programu użytkownik ma możliwość wprowadzenia początkowej liczby mieszkańców oraz budżetu. Następnie, w menu, dostępne są następujące opcje:
1.	Kontynuuj symulację – użytkownik podaje liczbę lat, które mają zostać zasymulowane, oraz tempo symulacji (czas trwania roku w milisekundach). W trakcie symulacji wyświetlane są podstawowe informacje o miasteczku.
2.	Zobacz podstawowe informacje o miasteczku – wyświetla aktualne dane dotyczące miasteczka, takie jak liczba mieszkańców, budżet, itp.
3.	Zobacz listę mieszkańców – wyświetla listę wszystkich żyjących mieszkańców, wraz z ich podstawowymi informacjami.
4.	Zobacz cmentarz – prezentuje listę grobów z informacjami o zmarłych oraz latach ich likwidacji.
5.	Zapisz – zapisuje aktualny stan miasteczka do pliku binarnego.
6.	Wczytaj – wczytuje dane miasteczka z wcześniej zapisanego pliku binarnego.
7.	Zakończ program – kończy działanie programu.

## Wymagania

Aby uruchomić projekt, potrzebujesz:
- Systemu operacyjnego z zainstalowanym kompilatorem Clang lub GCC.
- Narzędzia `make`.

## Sposób użycia

1. Sklonuj repozytorium lub skopiuj pliki projektu na swój komputer.
2. W terminalu przejdź do katalogu projektu.
3. Wykonaj polecenie:
    `make`
To polecenie skompiluje program i stworzy plik wykonywalny o nazwie symulacja.
4. Aby uruchomić program, wpisz w terminalu:
    `symulacja.exe` (Windows)
    `./symulacja` (Linux/macOS)
5. Aby wyczyścić pliki wygenerowane podczas kompilacji, użyj:
    `make clean`

## Struktura projektu
```
.
├── .vscode                # Ustawienia dla Visual Studio Code
│   └── settings.json      # Plik z ustawieniami edytora
├── build/                 # Katalog na pliki obiektowe (generowany automatycznie)
├── include/               # Katalog z plikami nagłówkowymi
│   └── budynki.h
│   └── cmentarz.h
│   └── menu.h
│   └── miasteczko.h
│   └── mieszkaniec.h
│   └── smierc.h
│   └── symulacja.h
│   └── zapisz_wczytaj.h
├── src/                   # Katalog z plikami źródłowymi
│   └── budynki.c
│   └── cmentarz.c
│   └── main.c             # Główny plik źródłowy
│   └── menu.c
│   └── miasteczko.c
│   └── mieszkaniec.c
│   └── smierc.c
│   └── symulacja.c
│   └── zapisz_wczytaj.c
├── imiona.txt             # Plik z przykładowymi imonami oraz nazwiskami
├── Makefile               # Skrypt budujący projekt
└── symulacja.exe          # Plik wykonywalny (po kompilacji)
```

## Autor

Przemysław Kaźmierczak