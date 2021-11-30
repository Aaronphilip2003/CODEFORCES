test_cases=int(input())
while test_cases!=0:
  players=[]
  player_skill=input().split()
  for i in player_skill:
    players.append(int(i))
  round1a_winner=max(players[0],players[1])
  round1b_winner=max(players[2],players[3])
  round1a_loser=min(players[0],players[1])
  round1b_loser=min(players[2],players[3])
  if round1a_loser>round1b_winner or round1b_loser > round1a_winner:
    print("NO")
  else:
    print("YES")  
  test_cases-=1

# 800 rated program
