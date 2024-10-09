import os
print("Version 1.0.0")
print("Welcome to Rock Paper Scissors! This game is entirely text based, so no assets will be used.")
print("Put down notes if you would like to know the current patch notes")
print("Put down news if you would like to read upcoming news on updates and more!")
print("Please select a mode by putting down the corresponding number")
print("By birdsfan24")
print("Literally one or two lines of code: partially made by ai")
print("1:Normal Mode")
print("2:Best Out of Three")
user_choice =input("Response:")
if user_choice =="1":
  os.system ("clear")
  import Normal
if user_choice =="2":
  os.system ("clear")
  import Bestoutof3
if user_choice =="notes" or "Notes":
  os.system ("clear")
  import notes
if user_choice =="news" or "News":
  os.system ("clear")
  import news