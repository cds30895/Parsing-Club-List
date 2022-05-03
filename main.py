"""
Excel Data Parser
------
This program is to find students who indicated an interest in Chess.
"""
import pandas as pd

if __name__ == "__main__":
  
  #Open the data file
  data = pd.read_csv("fake_club_data.csv")

  #Check data in and length of file
  print(data)

  #Copy data and fill "NaN" cells with "none" to prevent boolean ambiguity errors
  data2 = data.fillna("none")

  #Select Interests Column as lower case strings
  interests = data2["What Clubs are you interested in joining this year?"].str.lower()

  #Select only the cells in the Interests Column that contain "chess"
  chess_interest = data2[interests.str.contains("chess")]

  #For those cells that contain "chess", print the Name and Email associated with that row
  print(chess_interest[["Name", "Student Email Address"]])

  #Write the info to a new .csv file
  #Index=False because we don't need the row numbers the data was at on the original data sheet
  chess_interest[["Name", "Student ID Number", "Student Email Address", "What Clubs are you interested in joining this year?"]].to_csv("chess_club.csv", index=False)