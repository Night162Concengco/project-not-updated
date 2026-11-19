
from pyscript import document, display
Elements ={
    
    
    "H": ('Hydrogen', 1, 1.0078), 
     "C":('Carbon',6,12.011), 
     "N":('Nitrogen',7,14.007),
     "O":('Onxygen',8,15.999),
     "P":('Phosphorus',15,30.974),
    "S":('Sulfur',16,32.065),
     "Se":('Selenium',34,78.960),
    "F":('Fluorine',9,18.998),
     "Cl":('Chlorine',17,35.453),
     "Br":('Bromine',35,79.904),
       "I":('Iodine',53,126.90),
     "He":('Helium',2,4.0026),
    "Ne":('Neon',10,20.180),
     "Ar":('Argon',18,39.948),
     "Kr":('Krypton',36,83.798),
        "Xe":('Xenon',54,131.29),
     "Rn":('Radon',86,222)
        
        
        
        }


def Search_Element(e): 

    Arisu1 = document.getElementById("Arisu1").value

    result = Elements.get(Arisu1,('Nothing here..', "????", "????")) #result display

#get the corresponding values
    document.getElementById("symbol").innerText = Arisu1

    document.getElementById("name").innerText = result[0]

    document.getElementById("number").innerText = result[1]

    document.getElementById("mass").innerText = result[2]
