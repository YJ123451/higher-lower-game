import random
from art import logo,vs
from game_data import data
from replit import clear


score = 0
acc = random.choice(data)
#checking guess
def check(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess == "a"
  elif b_followers > a_followers:
    return guess == "b"
game_continue = True
while(game_continue):
  print(logo)
#formatting text
  
  acc2 = random.choice(data)
  acc_followers = acc["follower_count"]
  acc2_followers = acc2["follower_count"]
  if acc == acc2:
    acc2 = random.choice(data)
  def format_data(account):
    acc_name = account['name']
    acc_desc = account['description']
    acc_country = account['country']
    return f"{acc_name}, a {acc_desc}, from {acc_country}"
  print(f"Compare A: {format_data(acc)}.")
  print(vs)
  print(f"Against B: {format_data(acc2)}.")
  
  
  guess = input("Who has more followers? Type 'A' or 'B': ")
  is_correct = check(guess,acc_followers,acc2_followers)
  clear()
  if is_correct:
    score += 1
    print(f"You got it right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong idiot. Final Score {score}")
    game_continue = False
  if acc2_followers > acc_followers:
    acc = acc2