# Compiler
# Set the compiler to clang
CC = clang

# Directory for header files
INCLUDEDIR = include
# Directory for source files
SRCDIR = src
# Directory for object files
OBJDIR = build

# Flags
# Add debug info, show warnings, and include header directory
CFLAGS = -g -Wall -I$(INCLUDEDIR)

# Detect OS and set commands accordingly
ifeq ($(OS),Windows_NT)
	OUTPUT_CMD = symulacja.exe
	CLEAN_CMD = del /q $(OBJDIR)\* $(OUTPUT) *.ilk *.pdb
else
	OUTPUT_CMD = symulacja
	CLEAN_CMD = rm -rf $(OBJDIR) $(OUTPUT) *.ilk *.pdb
endif

# Output executable
# The name of the output binary file
OUTPUT = $(OUTPUT_CMD)

# Source files
# List of source files
SOURCES = $(SRCDIR)/main.c $(SRCDIR)/budynki.c $(SRCDIR)/cmentarz.c $(SRCDIR)/menu.c $(SRCDIR)/miasteczko.c $(SRCDIR)/mieszkaniec.c $(SRCDIR)/smierc.c $(SRCDIR)/symulacja.c $(SRCDIR)/zapisz_wczytaj.c

# Object files
# Object files corresponding to source files
OBJECTS = $(OBJDIR)/main.o $(OBJDIR)/budynki.o $(OBJDIR)/cmentarz.o $(OBJDIR)/menu.o $(OBJDIR)/miasteczko.o $(OBJDIR)/mieszkaniec.o $(OBJDIR)/smierc.o $(OBJDIR)/symulacja.o $(OBJDIR)/zapisz_wczytaj.o

# Default rule
# 'make' will build the executable by default
all: $(OUTPUT)

# Rule to build the final executable
# Link all object files to create the final executable
$(OUTPUT): $(OBJECTS)
# $@ is the target name (OUTPUT), $^ are all prerequisites (OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

# Rule to compile each .c file into a .o file
$(OBJDIR)/%.o: $(SRCDIR)/%.c
# Compile the source file ($<) into the object file ($@)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean rule to remove generated files
clean:
# Remove the build directory and the output binary
	$(CLEAN_CMD)