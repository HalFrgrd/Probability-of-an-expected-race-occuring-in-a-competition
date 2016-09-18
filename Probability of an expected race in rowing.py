
from math import ceil
from random import choice

perRace = 8
contestants = 32
assignedTruePositions = [x for x in range(contestants)]

#numberOfFairTimes = 0
#numberOfUnfairTimes = 0

top1 = 0
top2 = 0
top3 = 0
top4 = 0
top5 = 0
top6 = 0
top7 = 0
top8 = 0

numberOfTimesNPlacesWereExpected = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

for k in range(1,10000):

	heats = [x for x in range(contestants)]
	reps = []
	semis = []
	finalA = []



	for y in range(4):
		currentHeat = []
		for i in range(8):
			currentContestant = choice(heats)
			heats.pop(heats.index(currentContestant))
			currentHeat.append(currentContestant)
		currentHeat.sort()
		semis.append(currentHeat[0])
		for z in currentHeat[1:]:
			reps.append(z)


	#print(reps)
	#print(semis)

	for z in range(4):
		currentRep = []
		for i in range(7):
			currentContestant = choice(reps)
			reps.pop(reps.index(currentContestant))
			currentRep.append(currentContestant)
		currentRep.sort()
		for z in currentRep[0:2]:
			semis.append(z)

	#print(semis)

	for v in range(2):
		currentSemi = []
		for i in range(6):
			currentContestant = choice(semis)
			semis.pop(semis.index(currentContestant))
			currentSemi.append(currentContestant)
		currentSemi.sort()
		for z in currentSemi[0:4]:
			finalA.append(z)

	finalA.sort()
	#print(finalA)

	for i in range(1,9):
		if finalA[0:i] == [0,1,2,3,4,5,6,7][0:i]:
			numberOfTimesNPlacesWereExpected[i] += 1

for b in range(1,9):
	print("Probability of the first %s places being as expected: %s" %(b,numberOfTimesNPlacesWereExpected[b]/k))

