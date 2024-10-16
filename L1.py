# L1
# Mac Weber-Hess & Gwyneth Gangwer

# A : Too Long for SMS
def too_long(text):
    if len(text) > 140:
        print("This SMS is too long.")

# Emoji in my string?
import unicodedata
print(unicodedata.lookup("snake"))
print(unicodedata.name(";"))
print(unicodedata.name("&"))