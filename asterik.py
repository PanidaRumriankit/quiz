class Candidate:
    def __init__(self, name: str, age: int, followers: int = 0, genre: str = 'unknown', status: str = 'new'):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if not isinstance(followers, int):
            raise TypeError("followers must be an integer")
        if not isinstance(genre, str):
            raise TypeError("genre must be a string")
        if not isinstance(status, str):
            raise TypeError("status must be a string")
        if len(name.replace(' ', '')) == 0:
            raise ValueError("name must not be empty or has only spaces")
        if len(genre.replace(' ', '')) == 0:
            raise ValueError("genre must not be empty or has only spaces")
        if age <= 0:
            raise ValueError("age must not less than 0")
        if followers < 0:
            raise ValueError("followers must not less than 0")
        if status != 'new' and status != 'qualified' and status != 'accepted' and status != 'rejected':
            raise ValueError("status is incorrect")

        self.__name = name
        self.__age = age
        self.__followers = followers
        self.__genre = genre
        self.__status = status

    def add_status(self, new):
        self.__status = new

    @property
    def get_status(self):
        return self.__status

    def __str__(self):
        return f"Candidate: {self.__name}, {self.__age}, {self.__followers}, {self.__genre} ({self.get_status})"

def test_normal():
    # privacy_required = bool(int(input()))
    name = input()
    age = int(input())
    followers = int(input())
    genre = input()
    decision = input()
    try:
        c = Candidate(name, age, followers, genre)  # Initializes your class
        print(c)
        c.status = decision  # Sets a value
        print(c)
    except ValueError:  # Implement ValueError where needed
        print("ValueError caught")
    # if privacy_required:
    #     privacy_check()  # Runs a hidden function to make sure that you're using properties ;)

c = Candidate('Kenny', 18, 2000, 'dog game', 'new')

print(c)
