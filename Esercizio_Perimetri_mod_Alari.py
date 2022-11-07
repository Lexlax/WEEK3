def perimetri(): # Qui con def indichiamo una funzione
        print("Salve, sono il tuo assistente virtuale per calcolare il perimetro di una figura geometrica")
        print(" 1) Quadrato \n 2) Rettangolo \n 3) Cerchio \n")

tentativi = 3
while (tentativi >= 0): # Questo while permette di effettuare i cicli ogni volta che si inserisce un valore valido
   perimetri()
   print ("Quale desidere Calcolare ") 
   scelta = int (input("- "))


   if scelta == 1: # In base alla scelta verrà calcolato un perimetro diverso 
     print ("Hai scelto il quadrato. Calcolo...")
     lato = int(input("inserisci il lato ")) 
     print ("Il perimetro del Quadrato è\n:", lato*4)
     contatore = 3
     break  
   elif scelta == 2:
     print ("Hai Scelto il Rettangolo. Calcolo...\n")
     base = int(input("Inserisci la base "))          
     altezza = int(input("Inserisci l'altezza "))
     print ("Il perimetro del Rettangolo è: ",base*2 + altezza*2)
     contatore = 3
     break
   elif scelta == 3:
     print ("Hai selezionato il Cerchio. Calcolo...")
     raggio = int(input("Inserisci il raggio "))
     pgreco = 2*math.pi  # Qui ho usato float altrimenti non restituirebbe i numeri dopo la virgola ho cambiato anche il π
     print ("Il perimetro del Cerchio è:", pgreco*raggio) # Grazie al floatho un numero reale come risulta>
     tentativi = 3
     break
   else:
     if tentativi == 3:      # Se la scelta è diversa da quella indicata iniziera a scalare il numero dei tentativi - ogni tentativo stampa quelli rimanenti. A zero si chiude
       print ("Inserire una scelta valida hai ancora ", tentativi)
       tentativi -=1
     elif tentativi ==2:
       print ("Inserire una scelta valida hai ancota", tentativi)
       tentativi -= 1
     elif tentativi == 1:
       print ("inserire una scelta validai hai ancora ", tentativi)
       tentativi -=1
     else: 
       tentativi = 0
       print ("+++++GETTORNI TERMINATI+++++\n   +++Alla prossima+++\n    +++++++++++++++++") #botta d'arte - frase di chiusura del programma per tentativi finiti
       break   
