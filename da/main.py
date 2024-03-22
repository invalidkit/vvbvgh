from jar import Fish
from fish import Pair


cichlids = Pair(1.8, "cichlids")
swordtails = Pair(1.1, "swordtails")
shrimp = Pair(0.2, "shrimp")

cichlidsQ = Fish(cichlids, 2)
swordtailsQ = Fish(swordtails, 3)
shrimpQ = Fish(shrimp, 8)

Q = list()

for i in cichlidsQ, swordtailsQ, shrimpQ:
    Q.append(i)

for i in Q:
    print(i)
