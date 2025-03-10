class Human_being:
    def __init__(self, name, gender, color, age, hubbies, sound):
        self.human_beingname = name
        self.human_beinggender = gender
        self.human_beingcolor = color
        self.human_beingage = age
        self.human_beinghubies = hubbies
        self.human_beingsound = sound

    def details(self):
     print(f"\n Name: {self.human_beingname}\n Gender: {self.human_beinggender}\n Color: {self.human_beingcolor}\n Age:{self.human_beingage}\n Hobbies:{self.human_beinghubies}\n Sound: {self.human_beingsound}")

       
 #class mother has inherited from class Human being            
class Mother(Human_being):
    def sound(num):
     print("Mezzo-sorano") 


mother = Mother("Rina", "Female", "Brown", 40, "Games and sports", "mezzo_sorano")
mother.details()


class Girl(Mother):
   def beaut(short):
      print("contralto")
 # Creating an instance of Girl
mother = Girl("Sarah", "female", "Dark skinned", 20, "Swimming", "contralto")
mother.details()


# Girl is 
class Boy(Girl):
   def woman(tall):
      print("baritone")
mother = Boy("Ronny", "Male", "Brown", 28, "Football", "Baritone")
mother.details()


class Man(Boy):
   def  mature(display):
      print("Bass")
mother = Man("Ricky", "Male", "Dark skinned", 30, "Music", "Bass")
mother.details()


class Baby(Man):
   def heart(sweet):
      print()
mother = Baby("Gady", "Male", "chocolate", 5, "Eating", "High_pitched")
mother.details()




                
                


    
        

