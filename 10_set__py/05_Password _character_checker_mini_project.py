## ========== password character checker =========

password = input("Enter Password: ")

special = set("@#$%^&*!")

found = special & set(password)

if found:
    print("Password contains special characters.")
    print("Characters Found:", found)
else:
    print("No special characters found.")


# o/p :

# Enter Password: harish@2005
# Password contains special characters.
# Characters Found: {'@'}
