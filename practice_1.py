name = input("what is your name?\n").strip().capitalize()
mail = input("what is your mail?\n").strip()
user_name = mail[:mail.index("@")]
domain = mail[mail.index("@") + 1:]
print(f"Hello {name}, this is a practice\n")
print(f"your user name is {user_name}, and your domain is {domain}")
