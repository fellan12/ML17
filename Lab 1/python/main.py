import monkdata as m
import dtree as dt
import drawtree_qt5 as draw
import matplotlib.pyplot as plt

print("Monk1 has entropy: ", dt.entropy(m.monk1))
print("Monk2 has entropy: ", dt.entropy(m.monk2))
print("Monk3 has entropy: ", dt.entropy(m.monk3))

print("Monk1, attribute a1 has information gain: ", dt.averageGain(m.monk1, m.attributes[0]))
print("Monk1, attribute a2 has information gain: ", dt.averageGain(m.monk1, m.attributes[1]))
print("Monk1, attribute a3 has information gain: ", dt.averageGain(m.monk1, m.attributes[2]))
print("Monk1, attribute a4 has information gain: ", dt.averageGain(m.monk1, m.attributes[3]))
print("Monk1, attribute a5 has information gain: ", dt.averageGain(m.monk1, m.attributes[4]))
print("Monk1, attribute a6 has information gain: ", dt.averageGain(m.monk1, m.attributes[5]))

print("Monk1's best attribute is: ", dt.bestAttribute(m.monk1, m.attributes))

print("\n")

print("Monk2, attribute a1 has information gain: ", dt.averageGain(m.monk2, m.attributes[0]))
print("Monk2, attribute a2 has information gain: ", dt.averageGain(m.monk2, m.attributes[1]))
print("Monk2, attribute a3 has information gain: ", dt.averageGain(m.monk2, m.attributes[2]))
print("Monk2, attribute a4 has information gain: ", dt.averageGain(m.monk2, m.attributes[3]))
print("Monk2, attribute a5 has information gain: ", dt.averageGain(m.monk2, m.attributes[4]))
print("Monk2, attribute a6 has information gain: ", dt.averageGain(m.monk2, m.attributes[5]))
print("Monk2's best attribute is: ", dt.bestAttribute(m.monk2, m.attributes))

print("\n")

print("Monk3, attribute a1 has information gain: ", dt.averageGain(m.monk3, m.attributes[0]))
print("Monk3, attribute a2 has information gain: ", dt.averageGain(m.monk3, m.attributes[1]))
print("Monk3, attribute a3 has information gain: ", dt.averageGain(m.monk3, m.attributes[2]))
print("Monk3, attribute a4 has information gain: ", dt.averageGain(m.monk3, m.attributes[3]))
print("Monk3, attribute a5 has information gain: ", dt.averageGain(m.monk3, m.attributes[4]))
print("Monk3, attribute a6 has information gain: ", dt.averageGain(m.monk3, m.attributes[5]))
print("Monk3's best attribute is: ", dt.bestAttribute(m.monk3, m.attributes))
print("\n")

#Calculate information gain for 2nd level in tree
#Monk1 - a5 - 1
a5 = m.attributes[4]
print("Monk1 - a5 - 1, a1 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[0]), m.attributes[0]))
print("Monk1 - a5 - 1, a2 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[0]), m.attributes[1]))
print("Monk1 - a5 - 1, a3 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[0]), m.attributes[2]))
print("Monk1 - a5 - 1, a4 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[0]), m.attributes[3]))
print("Monk1 - a5 - 1, a6 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[0]), m.attributes[5]))
print("\n")

#Monk1 - a5 - 2
print("Monk1 - a5 - 2, a1 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[1]), m.attributes[0]))
print("Monk1 - a5 - 2, a2 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[1]), m.attributes[1]))
print("Monk1 - a5 - 2, a3 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[1]), m.attributes[2]))
print("Monk1 - a5 - 2, a4 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[1]), m.attributes[3]))
print("Monk1 - a5 - 2, a6 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[1]), m.attributes[5]))
print("\n")

#Monk1 - a5 - 3
print("Monk1 - a5 - 3, a1 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[2]), m.attributes[0]))
print("Monk1 - a5 - 3, a2 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[2]), m.attributes[1]))
print("Monk1 - a5 - 3, a3 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[2]), m.attributes[2]))
print("Monk1 - a5 - 3, a4 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[2]), m.attributes[3]))
print("Monk1 - a5 - 3, a6 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[2]), m.attributes[5]))
print("\n")

#Monk1 - a5 - 4
print("Monk1 - a5 - 4, a1 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[3]), m.attributes[0]))
print("Monk1 - a5 - 4, a2 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[3]), m.attributes[1]))
print("Monk1 - a5 - 4, a3 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[3]), m.attributes[2]))
print("Monk1 - a5 - 4, a4 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[3]), m.attributes[3]))
print("Monk1 - a5 - 4, a6 has info gain: ", dt.averageGain(dt.select(m.monk1, a5, a5.values[3]), m.attributes[5]))
print("\n")



t1 = dt.buildTree(m.monk1, m.attributes)
print(dt.check(t1, m.monk1))
print(dt.check(t1, m.monk1test))

t2 = dt.buildTree(m.monk2, m.attributes)
print(dt.check(t2, m.monk2))
print(dt.check(t2, m.monk2test))

t3 = dt.buildTree(m.monk3, m.attributes)
print(dt.check(t3, m.monk3))
print(dt.check(t3, m.monk3test))



fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
oldres = []
newres = []
errorfrac = []
gain = []
i = 1
for monk in m.monk1, m.monk3:
    
    oldres = []
    newres = []
    errorfrac = []
    gain = []
    mk = "MONK-"+str(i)

    for frac in fractions:
        print("Current fraction is: ", frac)
        for i in range(1000):
            monk1train, monk1val = dt.partition(monk, frac)

            t1train = dt.buildTree(monk1train, m.attributes)

            currBestScore = dt.check(t1train, monk1val)
            oldres.append(currBestScore)
            currBestTree = t1train

            hasFound = True
            while(hasFound):
                hasFound = False
                for tree in dt.allPruned(currBestTree):
                    score = dt.check(tree, monk1val)
                    if score > currBestScore:
                        hasFound = True
                        currBestTree = tree
                        currBestScore = score
            newres.append(currBestScore)
        #print("Old score was: ", sum(oldres)/len(oldres))
        errorfrac.append(sum(newres)/len(newres))
        """print("New score is: ", sum(newres)/len(newres))
        print("Gain is: ", sum(newres)/len(newres)-sum(oldres)/len(oldres))
        gain.append(sum(newres)/len(newres)-sum(oldres)/len(oldres))"""
    plt.plot(fractions, errorfrac, label=mk)
    plt.plot(fractions, errorfrac,'ro')

    i = 3

plt.legend()
#plt.plot(fractions, errorfrac)
#plt.plot(fractions, gain)
plt.ylabel("Classification error")
plt.xlabel("Fraction")
plt.show()

#print(dt.buildTree(m.monk1, m.attributes))
#print(currBestTree)
