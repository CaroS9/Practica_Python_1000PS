"""Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo,
“Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función."""

def convertirEspaciado():
  texto=input("Ingresa un texto: ")
  texto=list(texto)
  for i in range(1,len(texto)+1,2):
    texto.append(" ")
    
  return print(texto)
# NO SE QUE FUNCION USAR !!
