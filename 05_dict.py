marks={
    "Hindi":40,
    "Math" :78,
    "science":89

}
print(marks)
print(marks.get("Hindi"))
print(marks.get("Eng"))
# add imtes in dictonary
marks["Eng"]=98
print(marks)
del marks["Hindi"]
print(marks)
marks["Hind="]=86
print(marks)