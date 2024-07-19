"""info={}
info["name "]="siva"
info["job"]="stuent"
print(info)
print(info.get("job"))
print(info.pop("job"))
print(info)"""
grades = {90:'A', 80:'B', 70:'C'}
print(list(grades.items()))
for (key, value) in grades.items():
    print(key, value)
print(grades[90])    