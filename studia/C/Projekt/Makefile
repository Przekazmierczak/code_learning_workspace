# Wykryj OS i ustaw odpowiednio komendy
ifeq ($(OS),Windows_NT)
	OUTPUT_CMD = symulacja.exe
	CREATE_DIR = @if not exist $(OBJDIR) mkdir $(OBJDIR)
	CLEAN_CMD = del /q $(OBJDIR)\* $(OUTPUT) *.ilk *.pdb
	REMOVE_DIR = @if exist $(OBJDIR) rmdir /S /Q $(OBJDIR)
else
	OUTPUT_CMD = symulacja
	CREATE_DIR = mkdir -p $(OBJDIR)
	CLEAN_CMD = rm -rf $(OBJDIR) $(OUTPUT) *.ilk *.pdb
	REMOVE_DIR = rm -rf $(OBJDIR)
endif

# Ustaw compilator pod clang
CC = clang

# Folder dla plików typu header
INCLUDEDIR = include
# Folder dla plików źródłowych
SRCDIR = src
# Folder dla plików obiektowych
OBJDIR = build

# Flags
CFLAGS = -g -Wall -I$(INCLUDEDIR)


# Nazwa pliku binarnego
OUTPUT = $(OUTPUT_CMD)

# Lista plików źródłowych
SOURCES = $(SRCDIR)/main.c $(SRCDIR)/budynki.c $(SRCDIR)/cmentarz.c $(SRCDIR)/menu.c $(SRCDIR)/miasteczko.c $(SRCDIR)/mieszkaniec.c $(SRCDIR)/smierc.c $(SRCDIR)/symulacja.c $(SRCDIR)/zapisz_wczytaj.c

# Lista plików obiektowych
OBJECTS = $(OBJDIR)/main.o $(OBJDIR)/budynki.o $(OBJDIR)/cmentarz.o $(OBJDIR)/menu.o $(OBJDIR)/miasteczko.o $(OBJDIR)/mieszkaniec.o $(OBJDIR)/smierc.o $(OBJDIR)/symulacja.o $(OBJDIR)/zapisz_wczytaj.o

# Podstawowe zasady
all: $(OUTPUT)

# Stwórz finalny plik wykonywalny
$(OUTPUT): $(OBJECTS)
# $@ oznacza nazwę celu (OUTPUT), a $^ to wszystkie pliki zależne (OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

# Stworzenie plików obiektowych .o z plików źródłowych .c
$(OBJDIR)/%.o: $(SRCDIR)/%.c
# Stwórz folder na pliki źródłowe
	$(CREATE_DIR)
# Kompilacja pliku źródłowego ($<) do pliku obiektowego ($@)
	$(CC) $(CFLAGS) -c $< -o $@

# Usuń stworzone pliki
clean:
	$(CLEAN_CMD)
	$(REMOVE_DIR)