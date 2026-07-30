code = {'India' : '0091',
         'Australia' : '0025',
           'Nepal' : '00977'
        }
country = input("Enter a country: ")
if country in code:
    print("Country Code: ", code[country])
else:
    print("Country not found ")
