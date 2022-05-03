class student:
	def __init__(self, name, interests):
		self.name = name
		self.email = "student@vansd.org"
		self.interests = interests.casefold()

student1 = student("Bill", "Chess, equestrian, mock trial")
student2 = student("Katy", "equestrian, Mock trial, videogame club")
student3 = student("Roger", "chess, videogame club")

student_list = [student1, student2, student3]
chess_list = []
equestrian_list = []
mock_trial_list = []
videogame_club_list = []



for i in range(len(student_list)):
  if "chess" in student_list[i].interests:
    chess_list.append(student_list[i])
  if "equestrian" in student_list[i].interests:
    equestrian_list.append(student_list[i])
  if "mock trial" in student_list[i].interests:
    mock_trial_list.append(student_list[i])
  if "videogame" in student_list[i].interests:
    videogame_club_list.append(student_list[i])

print("Chess Club:")
for i in range(len(chess_list)):
  print(chess_list[i].name + ", " + chess_list[i].email)
  
print("\nEquestrian Team:")
for i in range(len(equestrian_list)):
  print(equestrian_list[i].name + ", " + equestrian_list[i].email)

print("\nMock Trial:")	
for i in range(len(mock_trial_list)):
  print(mock_trial_list[i].name + ", " + mock_trial_list[i].email)

print("\nVideogame Club:")
for i in range(len(videogame_club_list)):
  print(videogame_club_list[i].name + ", " + videogame_club_list[i].email)





