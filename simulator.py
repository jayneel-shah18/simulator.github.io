import random

index = 0

#to store average and player ids
averages = {}

#creating a list of 60 random scores
scores = []
for i in range(0, 60):
  x = random.randint(0, 250)  #random score between 0 and 250
  scores.append(x)

#generating number of matches for 11 players such that sum is 60
while True:
  matches = [random.randint(2, 10) for i in range(0, 11)]
  if sum(matches) == 60:
    break


#generating a random player id
def getpid(k):
  '''
    Randomly generates a Player ID of format PXXXXXX. Where X can be any digit from 0 to 9.
    '''
  p_id = 'P' + str(random.randint(0, 999999)).zfill(6)

  return p_id


#generating scores, player id and averages for players
def getscores(k):
  '''
    Generates a list of 10 scores for a given player. NA indicates that player did not play that match
    '''
  global scores  #to access scores and matches
  global matches  #and update them
  global index  #for choosing values from matches
  global averages  #appending averages and pids

  temp = []
  sums = 0

  for i in range(index, matches[k] + index):
    temp.append(scores[i])
    sums += scores[i]
    avg = sums / matches[k]

  for element in temp:
    if element in scores:
      scores.remove(
        element)  #scores from temp are removed from global scores list

  #appends NA for the matches not played
  if matches[k] != 10:
    for i in range(0, 10 - matches[k]):
      temp.append('NA')

  random.shuffle(temp)  #shuffles the list after adding NA

  temp.append(avg)  #appends average to the list

  pid = getpid(k)  #generates pid for player and
  temp.insert(0, pid)  #inserts it to 0th position in scores

  averages[avg] = pid  #dictionary of scores and player
  #ids for generating result

  return temp


print(
  "PlayerID \tMatch1 \tMatch2 \tMatch3 \tMatch4 \tMatch5 \tMatch6 \tMatch7 \tMatch8 \tMatch9 \tMatch10 \tAverage"
)
for i in range(0, 11):
  print(*getscores(i), sep="    \t")

print("\n\n")

decisionlist = sorted(averages.keys(), reverse=True)
decisionlist = decisionlist[:6]

print("Players selected are - ", end=" ")
for i in decisionlist:
  print(averages[i], end=" ")
