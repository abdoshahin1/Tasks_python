# this app make to add skills to system
import sqlite3
user_id = 1

# connect into the database and set the curser
db = sqlite3.connect("app_data.db")
cr = db.cursor()


# show the message to user
option = """Hello sir, i wish my app was helpful for you.
1- s => Show all skills
2- a => Add skill to database
3- u => Update skill from database
4- d => Delete skill from database
5- q => Quit."""
print(option)

# get the input from user
choose = input("please enter the character from above : ").strip().lower()

# make func to commit and close the database
def save_info() -> None:
    db.commit()
    db.close()
    print("the connection into database is closed.")

# make the fun to do the job of the character
def job(char) -> str:
    cr.execute("CREATE TABLE IF NOT EXISTS skills(user_id integer, skill_name text, progress integer)")
    if char == "s":
        answer = input("do you want show all data in the database or not?\n").strip().lower()
        if answer == "y":
            cr.execute('select * from skills')
            all_data = cr.fetchall()
            for data in all_data:
                print(f"your user_id is {data[0]} and your skill is => {data[1]} and your progress is => {data[2]}")
        else:
            cr.execute(f"SELECT * FROM skills where user_id = {user_id}")
            result_list = cr.fetchall()
            if len(result_list) > 0:
                print("there are your data.")
                for result in result_list:
                    print(f"your skill is => {result[1]} and your progress is => {result[2]}")
            else:
                print("there are not skills to showing.")
        save_info()
    elif char == "a":
        skill_name = input("enter the skill: ").capitalize().strip()
        cr.execute(f"select skill_name from skills where skill_name = '{skill_name}' and user_id = {user_id}")
        test = cr.fetchone()
        if test != None:
            print("this skill is already exists.")
        else:
            prog = int(input("enter the progress: ").strip())
            cr.execute("INSERT INTO skills values(?,?,?)", (user_id, skill_name, prog))
            print("the skill is added")
        save_info()
    elif char == "u":
        sk = input("enter the skill's name: ").strip().capitalize()
        pr = int(input("enter the new progress : ").strip())
        cr.execute(f"UPDATE skills set progress = {pr} WHERE user_id = {user_id} and skill_name = '{sk}'")
        print("the skill is updated")
        save_info()
    elif char == "d":
        skl = input("enter the skill :").capitalize().strip()
        cr.execute(f"DELETE FROM skills WHERE user_id = {user_id} and skill_name = '{skl}'")
        print("the skill is deleted.")
        save_info()
    elif char == "q":
        print("the program is quit.")
        save_info()
    else:
        print(f"this commend \"{char}\" is not exists.")

job(choose)