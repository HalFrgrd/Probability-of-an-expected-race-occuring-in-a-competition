
from math import ceil
from random import choice
from random import randrange
from random import gauss

contestants = 32

numberOfTimesNPlacesWereExpected = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

def orderOfRace(racers): # racers is a list with smaller lists which are the Key and Value.
	actualtimes = []
	for c in racers:
		time = c[1]
		actualtimes.append([c[0],gauss(time,2)])
	actualtimes.sort(key=lambda x: x[1])
	return actualtimes

def randomElementFromDict(dictionary):
	return choice(list(dictionary.keys()))

def roundProcess(numberofEqualRounds,contestantsPerRound,comingFrom,sucessfullGoingTo,howmanysucessful,unsucessfulGoingTo,):
	for y in range(numberofEqualRounds):
		currentRace = []
		for i in range(contestantsPerRound):
			currentContestant = randomElementFromDict(comingFrom)
			currentRace.append([currentContestant,comingFrom[currentContestant]])
			comingFrom.pop(currentContestant)
		placingsForTheRace = orderOfRace(currentRace)
		
		for m in placingsForTheRace[0:howmanysucessful]:
			sucessfullGoingTo[m[0]] = m[0]
		for z in placingsForTheRace[howmanysucessful:]: # the rest go to whereever else
			unsucessfulGoingTo[z[0]] = z[1]

for k in range(1,1000):

	heats = {}
	for x in range(1,33):
		heats[x] = 420+5*x

	reps = {}
	semis = {}
	eliminated = {}
	finalA = {}
	placings = {}
	'''
	for y in range(4):
		currentHeat = []
		for i in range(8):
			currentContestant = randomElementFromDict(heats)
			currentHeat.append([currentContestant,heats[currentContestant]])
			heats.pop(currentContestant)
		placingsForTheHeat = orderOfRace(currentHeat)
		semis[placingsForTheHeat[0][0]] = placingsForTheHeat[0][0] # the first goes to semis
		for z in placingsForTheHeat[1:]: # the rest go to reps
			reps[z[0]] = z[1]'''

	roundProcess(4,8,heats,semis,1,reps)

	"""
	for z in range(4):
		currentRep = []
		for i in range(7):
			currentContestant = randomElementFromDict(reps)
			currentRep.append([currentContestant,reps[currentContestant]])
			reps.pop(currentContestant)
		placingsForReps = orderOfRace(currentRep)

		for z in placingsForReps[0:2]: # top 2 go to semis
			semis[z[0]] = z[0]
								# rest gets eliminated"""
	roundProcess(4,7,reps,semis,2,eliminated)

	"""
	for v in range(2):
		currentSemi = []
		for i in range(6):
			currentContestant = randomElementFromDict(semis)
			currentSemi.append([currentContestant,semis[currentContestant]])
			semis.pop(currentContestant)
		placingsForSemis = orderOfRace(currentSemi)
		for z in placingsForSemis[0:4]: # top 4 go to finalA
			finalA.append(z[0])"""
	roundProcess(2,6,semis,finalA,4,eliminated)

	roundProcess(1,8,finalA,placings,8,eliminated)

	placingsAsAList = []

	for l in range(8):
		placingsAsAList.append(placings.popitem()[0])

	for i in range(1,9):
		if placingsAsAList[0:i] == [1,2,3,4,5,6,7,8][0:i]:
			numberOfTimesNPlacesWereExpected[i] += 1

for b in range(1,9):
	print("Probability of the first %s places being as expected: %s" %(b,numberOfTimesNPlacesWereExpected[b]/k))

