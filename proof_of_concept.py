import pandas as pd

data = pd.read_csv("fake_club_data.csv")
data2 = data

print(data2[(data2["Interests"].str.lower()).str.contains("chess")])

interests = data["Interests"].str.lower()

chess_interest = interests[interests.str.contains("chess")]

#print(chess_interest)