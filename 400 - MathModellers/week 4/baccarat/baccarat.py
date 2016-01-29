import numpy as np

# create a suit
suit = list(range(1,11)) + [0,0,0]

# create a multidimensional array to hold card
# combination sum values
sumTallies = [list(range(0,11)),[0]*11]

# set the number of suits
suit_count = 4

# create the suits
suits = []
for i in range(0,suit_count):
    suits.append(suit)

def compareSamesuit(d):
    # get all the combinations of cards within a suit and get the baccarat value
    for idx1 in range(0,len(d)):
        if idx1 < len(d) - 1:
            for idx2 in range(idx1+1,len(d)):
                value = d[idx1] + d[idx2]
                if value >= 10:
                    # in baccarat, if the sum of two cards is greater than 9, you subract 10 from the sum
                    value -= 10
                # increment the tally for the value
                #if value == 0:
                    #print("%d : %d" % (d[idx1],d[idx2]))
                sumTallies[1][value] += 1

def compareAcrosssuits(ds):
    # for each suit
    for idx1 in range(0,len(ds)):
        if idx1 < len(ds) - 1:
            # compare the next suit
            for idx2 in range(idx1+1,len(ds)):
                # create a supersuit of each element in the first suit to all the cards
                # in the second suit
                for idx3 in range(0,len(ds[idx1])):
                    supersuit = [ds[idx1][idx3]] + ds[idx2]
                    compareSamesuit(supersuit)

def getProbabilityOfANatural():
    # a natural sums to an 8 or a 9
    combinations = sum(sumTallies[1])
    nbrOfCards = 0
    for d in suits:
        nbrOfCards += len(d)
    print("\nProbability of getting a natural with %d cards:" % nbrOfCards)
    prob = (float(sumTallies[1][8])+float(sumTallies[1][9])) / float(combinations)
    print(round(prob,8))

def getProbabilityOfANaturalKnowingDealerGotANatural():
    #to simulate dealer getting a natural, remove one of the naturals from the set
    sumTallies[1][8] -= 1
    combinations = sum(sumTallies[1])
    nbrOfCards = -2
    for d in suits:
        nbrOfCards += len(d)
    print("\nProbability of player getting a natural knowing dealer had a natural with %d cards:" % nbrOfCards)
    prob = (float(sumTallies[1][8])+float(sumTallies[1][9])) / float(combinations)
    print(round(prob,8))

def main():
    #there are two ways to compute if two cards add up to the right total
    #sum cards in the same suit, or sum a card in one suit against all the 
    #other suits
    for d in suits:
        compareSamesuit(d)
    compareAcrosssuits(suits)

    print("Totals of two card baccarat combinations are:")
    print (np.transpose(sumTallies))

    #now that we have totals, we can figure out probabilities
    getProbabilityOfANatural()
    getProbabilityOfANaturalKnowingDealerGotANatural()

    
main()