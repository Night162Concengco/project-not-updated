
from js import document
from pyodide.ffi import create_proxy

club_members = [
    "Athena Aria",
    "Matt Nicolas",
    "Lily Cawthon",
    "Jenny Parker",
    "kelly bridge"
]

def add_member(event):
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()
    club_members.append(full_name)
    document.getElementById("result").innerText = f"Congratulations {full_name}! You are now part of the ICT club."
    document.getElementById("members-list").innerText = ", ".join(club_members)
    document.getElementById("member-count").innerText = f"Official Club Members: {len(club_members)} STUDENTS"
    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""
def setup(event=None):
    document.getElementById("members-list").innerText = ", ".join(club_members)
    document.getElementById("member-count").innerText = f"Official Club Members: {len(club_members)} STUDENTS"
    button = document.getElementById("btn-submit")
    button.addEventListener("click", create_proxy(add_member))
setup()

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



club_members = [
    "Athena Ari",
    "Brian Bo",
    "Carter Cu",
]

def check_membership(event):
  
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()

   
    full_name_lower = full_name.lower()
    members_lower = list(map(str.lower, club_members))

  
    is_member = full_name_lower in members_lower


    messages = [
        f"Sorry, {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]

   
    document.getElementById("result").innerText = messages[is_member]

def setup():
    button = document.getElementById("btn-submit")
    button.addEventListener("click", create_proxy(check_membership))

setup()










