#  35 - Create a game / function that takes 1K contestants of "heads of tails" and plays them in a tournament.  Heads wins.
import random

# import initial large word list as contestants
file1_list = []
with open('SOWPODS.txt', 'r') as f:
	line = f.readline()
	while line:
		line = line.strip()
		file1_list.append(line)
		line = f.readline()
# create contestants from the first 1,000 entries in the large word list
next_round = []
for i in range(0,20000):
	next_round.append(random.choice(file1_list))
# print(next_round)
play = True
round = 1

def play_round(): # iterates through current list of contestants, having them "flip a coin", and eliminating.
	global play
	for i in next_round:
		flip = random.randint(0,1) # 0 = 'Heads', 1 = "Tails"
		if flip == 0:
			next_round.append(i)
		next_round.remove(i)
	if next_round == []:
		play = False
	else:
		print(next_round)
		print("{} contestants flipped Heads.").format(len(next_round))
	return (play)

while play == True:
    str(raw_input("Hit <Enter> to play round " + str(round) + "."))
    round +=1
    play_round()

if play == False:
    round -=1
    print("Sorry, but no contestants flipped Heads in round {}. ").format(round)


