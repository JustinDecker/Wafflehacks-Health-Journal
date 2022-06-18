import pygame
from datetime import datetime

class Jentry:
    #Variables
    today = datetime.now().strftime("%x")
    mood = 0
    social = 0
    energy = 0
    freetime = 0
    exercise = 0
    diet = 0
    sleep = 0
    menstruation = False
    journal = ""
    

    #Constructor
    def __Jentry__(self, mood, social, energy, freetime, exercise, diet, sleep, menstruation, journal):
        self.today = datetime.now().strftime("%x") # --> MM/dd/yy
        self.mood = int(mood)
        self.social = int(social)
        self.energy = int(energy)
        self.freetime = int(freetime)
        self.exercise = int(exercise)
        self.diet = int(diet)
        self.sleep = int(sleep)
        self.menstruation = bool(menstruation == "True")
        self.journal = str(journal)
    
    #Getters
    def get_date(self):
        return self.today

    def get_mood(self):
        return self.mood
        
    def get_social(self):
        return self.social

    def get_energy(self):
        return self.energy

    def get_freetime(self):
        return self.freetime

    def get_exercise(self):
        return self.exercise
    
    def get_diet(self):
        return self.diet

    def get_sleep(self):
        return self.sleep
    
    def get_menstruation(self):
        return self.menstruation

    def get_journal(self):
        return self.journal
    
    #Setters
    
    #Methods
    def get_log(self):
        log = self.today + "|" + self.mood + "|" + self.social + "|" + self.energy + "|" + self.freetime + "|" + self.energy + "|" + self.diet + "|" + self.sleep + "|" + self.menstruation + "|" + self.journal
        return log

    def get_value(self, value_to_get):
        if (value_to_get == "Date"):
            return self.get_date
        elif (value_to_get == "Mood"):
            return self.get_mood
        elif (value_to_get == "Social"):
            return self.get_social
        elif (value_to_get == "Energy"):
            return self.get_energy
        elif (value_to_get == "Freetime"):
            return self.get_freetime
        elif (value_to_get == "Energy"):
            return self.get_energy
        elif (value_to_get == "Diet"):
            return self.get_diet
        elif (value_to_get == "Sleep"):
            return self.get_sleep
        elif (value_to_get == "Menstruation"):
            return self.get_menstruation
        elif (value_to_get == "Journal"):
            return self.get_journal