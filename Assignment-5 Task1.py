data={"Alice":85,"Tom":92,"Harry":78,"Jenny":81}
name=input("Enter student's name: ")
if name in data.keys():
    print("{} marks: {}".format(name,data[name]))
else:
    print("Student not found")
