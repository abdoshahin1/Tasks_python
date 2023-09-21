# practice app about check your member
member_list=["Ahmed","Ali","Abdo","Mohammed","Omer","Hanaa","Fatema","Yassmeen"]
name=input("write your name:\n").strip().capitalize()
gender=input("what is your gender?\n").strip().lower()
if name in member_list :
    if gender == "male" :
        print(f"Hello Mr.{name}, you are member in this list.")
    elif gender == "female" :
        print(f"Hello Mis.{name}, you are member in this list.")
    else :
        print("fuck you, you are a fucking gay.")
    change=input("Delete or Update your name: ").strip().lower()
    if change == "update" :
        new_name=input("what is your new name?\n").strip().capitalize()
        member_list[member_list.index(name)]=new_name
        print("updating name")
        print("your name updated")
        print(member_list)
    elif change == "delete" :
        member_list.remove(name)
        print("your name removed.")
        print(member_list)
    else : 
        print("your option is not available.")
else :
    print("you are not member.")
    answer=input("Are you want to be member y|n: ").strip().capitalize()
    if answer == "yes" or answer =="Y" :
        member_list.append(name)
        print(member_list)
        print(f"Hello {name}, in out group.")
    else :
        print("thanks.")
        print("Note:")
        print("fuck you hhahhahhahah")