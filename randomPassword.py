import random
import string

pool = string.ascii_letters + string.digits

password_list = random.choices(pool, k=12)

random.shuffle(password_list)

password = "".join(password_list)
print("Your password is:", password)
