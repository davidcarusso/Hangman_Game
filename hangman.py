import os
import random


def random_word():
    with open("./data_file/data.txt", "r", encoding="utf-8") as f:
        palabra = [i.strip().upper() for i in f]
        return random.choice(palabra)    
      

def hangman():
        
    palabra = random_word()
    letra_palabra= set(palabra)
    letras_usadas= set()
    vidas= 6
        
    while len(letra_palabra)>0 and vidas > 0:        
        os.system("clear")
        
        print("¡¡¡Adivina la palabra!!!", end="\n\n")
        print("Letras usadas: ", " ".join(letras_usadas), end="\n\n")
        print(f"Te quedan {vidas} vidas", end="\n")
    
        #aca deberia sustituir "-" por la letra.
        palabra_lista = [i if i in letras_usadas else "-" for i in palabra]        
        print("Palabra: " + " ".join(palabra_lista) + "\n")
        print("\n")            
             
        
        #Ingresar una letra:
        letra= input("Elige una letra: ").upper()
        
        #remover y agregar letra, quitar vida.
        if letra not in letras_usadas: 
            letras_usadas.add(letra)
            if letra in letra_palabra:
                letra_palabra.remove(letra)
            else:
                vidas = vidas - 1
        else:
            print("Ya usaste esa letra.", end="\n") 
            
    if vidas == 0:
        os.system("clear")
        print(f"¡¡¡PERDISTE!!!\n\nLa palabra era: {palabra}" , end="\n\n")

    else:
        os.system("clear")
        print(f"¡¡¡GANASTE!!!\n\nLa palabra era: {palabra}")


if __name__ == "__main__":
    hangman()