class Dogs:
    #атрибуты класса: имя, приют, порода
    def __init__(self, breed, name, shelter):
        # breeds = [
        #     "Pug", "Bullterrier", "Canes", "Dalmatian", "Doberman", "Pekingese",
        #     "Poodle", "Rottweiler", "St.Bernard", "Dachshund", "Chow - chow", "Husky",
        #     "Shepherd", "Chihuahua", "Boxer"
        # ]
        self.breed = breed
        self.shelter = shelter
        self.name = name

    def __str__(self):
        return f"Собака {self.breed} с именем {self.name} живёт в {self.shelter}"

    #Сравнивает породу и приют двух собак
    def __eq__(self, other):
        return self.breed == other.breed and self.shelter == other.shelter

    #Сравнивает средний возраст пород
    def __gt__(self, other):
        return self.breed.avg_age > other.breed.avg_age
