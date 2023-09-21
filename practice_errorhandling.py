the_file = None
the_tries = 5
print(f"you have the {the_tries} tries")
while the_tries > 0:
    try:
        user_input = input("enter the file absolute path: ").strip()
        the_file = open(user_input, "r")
        print("\n", the_file.read())
        break
    except FileNotFoundError:
        print("file not found")
        the_tries -=1
    except:
        print("error happened")
    finally:
        if the_file is not None:
            the_file.close()
            print("\nthe file was closed.")
else:
    print("\nyour tries is done")