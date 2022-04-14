import string
import random

def random_user_id():
    print(string.ascii_letters)
    print(string.digits)
    r = "".join(random.choices(string.ascii_letters + string.digits, k= 6))
    print(r)






