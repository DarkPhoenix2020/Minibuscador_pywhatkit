# importamos el modulo
import pywhatkit

banner = """

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<By:DarkPhoenix87>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    __  ____       _ ____                            __          
   /  |/  (_)___  (_) __ )__  ________________ _____/ /___  _____
  / /|_/ / / __ \/ / __  / / / / ___/ ___/ __ `/ __  / __ \/ ___/
 / /  / / / / / / / /_/ / /_/ (__  ) /__/ /_/ / /_/ / /_/ / /    
/_/  /_/_/_/ /_/_/_____/\__,_/____/\___/\__,_/\__,_/\____/_/     


Canal Youtube: https://www.youtube.com/channel/UConS1Dk6zZAOFuaSwTtLbqA

Github: https://github.com/DarkPhoenix2020 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<By:DarkPhoenix87>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""

print(banner)

def Buscar():

  #entrada por teclado y se almacena en la variable buscador
  buscador = input("Ingrese la palabra clave, a la cual desea hacer la busqueda: ")
  print("\n")
  
  # utilizaremos controles de excepciones
  try: 
     
  # realizara la busqueda en Google
    pywhatkit.search(buscador) 
    print("Busncando...") 

   
  except: 
     
    # imprime mensaje de error
    print("Ha ocurrido un error!")

Buscar()