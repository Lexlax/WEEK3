import socket #
import random #

pacchetti = int(input ("Inserire in numero di pacchetti ")) # Variabie a scelta dall'utente per indicate il numero di pacchetti
address = input ("Inserisci l'indirizzo ") # Variabile a scelta dall'utente per indicare l'indirizzo
port = int (input ("Inserisci la porta ")) # Variabile a scelta dall'utente per indicare la porta
p = 0 # variabile iniziallizzata a 0 per il cilco while "p<=pacchetti"
while 1: # Ciclo che 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creazione nuovo socket "s" con i parametri AF_INET per ipv4 e SOCK_DGRAM per connessione UDP
    s.bind((address, port)) # Collegamento della vaiabile "s" alla porta e all'indirizzo
    data= random.randbytes(1024) # Creazione della variabile data con il peso dei pacchetti
    target= (str (address), int (port)) 
    while (p<pacchetti): #Ciclo per concludere al raggiungimento dei pacchetti inseriti in precedenza
             s.sendto(data, target) # Sendto permette di collegare un socket con un altro. In questo caso invia i pacchetti all'IP
             p=p+1 # Incremento della variabile "p" per il controllo del ciclo
    s.close()
    quit()




