def perimetro(): # on def si definisce il nome della Funzione che potrà essere richiamata anche al di fuori da qui
        print("Salve, sono il tuo assistente virtuale per calcolare il perimetro di una figura geometrica")
        print(" 1) Quadrato \n 2) Rettangolo \n 3) Cerchio \n")

        print("Quale desidere Calcolare ") 
        scelta = int(input(""))
        if scelta == 1: # In base alla sceltaverrà calcolato un perimetro diverso 
                print("Hai scelto il quadrato. Calcolo...")
                lato = int(input("inserisci il lato "))
                print("Il perimetro del Quadrato è\n:", lato*4)
        elif scelta == 2:
                print("Hai Scelto il Rettangolo. Calcolo...\n")
                base = int(input("Inserisci la base "))
                altezza = int(input("Inserisci l'altezza "))
                print("Il perimetro del Rettangolo è: ",base*2 + altezza*2)
        elif scelta == 3:
                print("Hai selezionato il Cerchio. Calcolo...")
                raggio = int(input("Inserisci il raggio "))
                pgreco = float(3.14*2) # Qui ho usato float altrimenti non restituirebbe i numeri dopo la virgola
                print("Il perimetro del Cerchio è:", pgreco*raggio) # Grazie al floatho un numero reale come risultato

        else:            # Se la scelta è diversa da quella indicata apparirà il messaggio qui sotto
                print("Inserire una scelta valida")
perimetro()   
