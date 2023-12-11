class Breeds:
    def __init__(self, name: str, avg_age: float, height: float):
        # breeds = [
        #     "Pug", "Bullterrier", "Canes", "Dalmatian", "Doberman", "Pekingese",
        #     "Poodle", "Rottweiler", "St.Bernard", "Dachshund", "Chow - chow", "Husky",
        #     "Shepherd", "Chihuahua", "Boxer"
        # ]
        self.name = name
        self.avg_age = avg_age
        self.height = height

    def __str__(self):
        return f"{self.name}"
