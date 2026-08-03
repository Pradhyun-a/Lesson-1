student_data = {
    "id1": {"name": "Alice", "class": "10", "subject": "Math"},
    "id2": {"name": "Bob", "class": "10", "subject": "Science"},
    "id3": {"name": "Alice", "class": "10", "subject": "Math"},
    "id4": {"name": "Charlie", "class": "11", "subject": "History"}
}

print("Step 2:")
print(student_data)

print("Step 3:")
print(student_data.get("id1", "Not Found"))
print(student_data.get("id5", "Not Found"))

print("Step 4:")
student_data["id5"] = {"name": "David", "class": "12", "subject": "English"}
print(student_data)

print("Step 5:")
student_data["id2"]["subject"] = "Physics"
print(student_data)

print("Step 6:")
cleaned_data = {}
seen_records = []

for student_id, details in student_data.items():
    if details not in seen_records:
        seen_records.append(details)
        cleaned_data[student_id] = details
print(cleaned_data)

print("Step 7:")
student_data.pop("id4")
print(len(student_data))

print("Step 8:")
for student_id, details in student_data.items():
    print(student_id, details)
