votes = ["Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Cassie"]

# Your code below: 
jake_votes = votes.count("Jake")
laurie_votes = votes.count("Laurie")
cassie_votes = votes.count("Cassie") 

print("Votes for Jake: ", jake_votes)
print("Votes for Laurie: ", laurie_votes)
print("Votes for Cassy: ", cassie_votes)

if jake_votes > laurie_votes and jake_votes > cassie_votes:
  winner = "Jake!"
elif laurie_votes > jake_votes and laurie_votes > cassie_votes:
  winner = "Laurie!"
elif cassie_votes > laurie_votes and jake_votes < cassie_votes:
  winner = "Cassie!"
elif cassie_votes == laurie_votes and jake_votes == cassie_votes:
  winner = "Tie"

if winner != "Tie":
  print("And the winner is: ", winner)
else:
  print("Its a Tie!")
