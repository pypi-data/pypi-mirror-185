# Makefile to clustering using SW 

CC = gcc

EFILE =  SW
SHAREDLIB =  spclib

OBJ  =  RaggedArray.o aux1.o aux2.o edge.o distance.o io.o param.o timer.o utilities.o
#SW.c RaggedArray.c aux1.c aux2.c edge.c distance.c io.c param.c timer.c utilities.c
#-msse -msse2 -mfpmath=sse   -s -std=c99 -flto -mtune=native -march=native
$(EFILE): CFLAGS = -O3 -flto -std=c99
$(SHAREDLIB): CFLAGS = -O3 -std=c99 -fPIC
all: clean rmlib $(SHAREDLIB)

$(SHAREDLIB): $(OBJ) spclib.c
	$(CC) spclib.c $(OBJ) $(CFLAGS) -shared -o $(SHAREDLIB).so -lm

$(EFILE): $(OBJ) SW.c
	$(CC) SW.c $(OBJ) $(CFLAGS) -o $(EFILE) -lm 

aux1.o aux2.o edge.o distance.o io.o: SW.h
timer.o: timer.h
param.o: param.h
RaggedArray.o: RaggedArray.h
utilities.o: utilities.h

test_lib: spclib.c RaggedArray.o aux1.o aux2.o edge.o distance.o io.o param.o timer.o utilities.o
	gcc -Wall -pedantic -shared -fPIC -o spclib.so spc.c RaggedArray.o aux1.o aux2.o edge.o distance.o io.o param.o timer.o utilities.o

makelib: rmlib spclib clean

rmexec:
	rm -f $(EFILE)

rmlib:
	rm -f $(SHAREDLIB).so

clean: 
	@echo "Removing object files ..."
	@rm -f $(OBJ)
	@echo "Done"







