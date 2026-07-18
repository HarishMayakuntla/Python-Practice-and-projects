

## ========= Email Validator ========
# we remove duplicate emails and which gives the unique emails


emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]

unique = set(emails)

print("Unique Emails")

for email in unique:
    print(email)



## o/p :

# Unique Emails

# b@gmail.com

# a@gmail.com

# c@gmail.com