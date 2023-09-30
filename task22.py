# class Game:
#     def __init__(self,name,developer,year,price):
#         self.name = name
#         self.developer = developer
#         self.year = year
#         self.price = price
#     def price_in_pounds(self):
#         return float((self.price * 15) + 30)

# game_one = Game("Ys", "Falcom", 2010, 50)

# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# class User:
#     def __init__(self,fname,mname,age,gender):
#         self.fname = fname
#         self.mname = mname
#         self.age = age
#         self.gender = gender.lower()
#     def full_details(self):
#         if self.gender == "male":
#             return f"Hello Mr {self.fname} {self.mname[0].capitalize()}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"
#         else:
#             return f"Hello Mrs {self.fname} {self.mname[0].capitalize()}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"


# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.full_details()) 
# print(user_two.full_details()) 

# class Message:
#     @classmethod
#     def print_message(cls):
#         return "Hello From Class Message"

# print(Message.print_message())


# class Games:
#     def __init__(self,list_games):
#         self.list_games = list_games
#     def show_games(self):
#         if type(self.list_games) == int: # self.list_games.__class__ is type that i want => to know the type of input
#             print(f"I Have {self.list_games} Games")
#         elif type(self.list_games) == list:
#             print("I Have Many Games:")
#             for game in self.list_games:
#                 print(f"-- {game}")
#         else:
#             print(f"I Have One Game Called \"{self.list_games}\"")

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()
# my_games_names.show_games()
# my_games_count.show_games()


# class Members:
#     def __init__(self,n,p):
#         self.name = n
#         self.permission = p
#     def show_info(self):
#         return f"Your Name Is {self.name} And You Are {self.permission}"

# class Admins(Members):
#     def __init__(self,n,p):
#         super().__init__(n,p)

# class Moderators(Admins):
#     def __init__(self,n,p):
#         super().__init__(n,p)

# member_one = Admins("Osama", "Admin")
# member_two = Moderators("Ahmed", "Moderator")

# print(member_one.show_info())
# print(member_two.show_info())

# class A:
#     def __init__(self, one):
#         self.one = one

# class B:
#     def __init__(self, two):
#         self.two = two

# class C:
#     def __init__(self, three):
#         self.three = three

# class Text:
#     def __init__(self,one,two,three):
#         A.__init__(self,one)
#         B.__init__(self,two)
#         C.__init__(self,three)
#     def show_name(self):
#         return f"the name is {self.one}{self.two}{self.three}"
# the_name = Text("El", "ze", "ro")
# print(the_name.show_name())
