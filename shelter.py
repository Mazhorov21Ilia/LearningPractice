class Shelter:
    def __init__(self, address: str, create_date: str, owner: str):
        self.address = address
        self.create_date = create_date
        self.owner = owner

    def __str__(self):
        return self.address