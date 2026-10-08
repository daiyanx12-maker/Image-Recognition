class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __lt__(self, other):
        return len(self.name) < len(other.name)

    def __add__(self, other):
        return len(self.__password) + len(other.__password)

    def __mul__(self, other):
        return len(self.__password) * len(other.__password)

    def __gt__(self, other):
        return len(self.__password) > len(other.__password)

    def __le__(self, other):
        return len(self.__password) <= len(other.__password)


u1 = User("Daiyan", "123")
u2 = User("daiyan", "5678")
u3 = User("Sami", "99999")

print("Initialized:", u1.name, "Password length:", len(u1._User__password))
print("u1 == u2 ?", u1 == u2)
print("u1 < u3 ?", u1 < u3)
print("u1 + u2:", u1 + u2)
print("u1 * u2:", u1 * u2)
print("u3 > u1 ?", u3 > u1)
print("u2 <= u1 ?", u2 <= u1)
