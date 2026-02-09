maths = int (input("Enter maths marks: "))
science = int (input("Enter science marks: "))
hindi = int (input("Enter hindi marks: "))
english = int (input("Enter english marks: "))

totalMarks = maths + science + hindi + english

percentage = (totalMarks / 400) * 100

print(percentage)