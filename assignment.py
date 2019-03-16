quest = [x for x in range(1, 1004)]

from numpy import random
random.shuffle(quest)

"""
python  75%
java    5%
c#      5%
c++     2.5%
go      2.5%
c       2%
kotlin  2%
rust    2%
scala   2%
swift   2%
"""
l = len(quest)

pythonq = quest[: int(l * 0.75)]
javaq = quest[int(l * 0.75) : int(l * 0.8)]
csharpq = quest[int(l * 0.8) : int(l * 0.85)]
cppq = quest[int(l * 0.85) : int(l * 0.875)]
goq = quest[int(l * 0.875) : int(l * 0.9)]
cq = quest[int(l * 0.9) : int(l * 0.92)]
kotlinq = quest[int(l * 0.92) : int(l * 0.94)]
rustq = quest[int(l * 0.94) : int(l * 0.96)]
scalaq = quest[int(l * 0.96) : int(l * 0.98)]
swiftq = quest[int(l * 0.98) :]

lanq = [pythonq, javaq, csharpq, cppq, goq, kotlinq, rustq, scalaq, swiftq]
lan = ['python', 'java', 'c#', 'c++', 'go', 'kotlin', 'rust', 'scala', 'swift']

assign = list()
for l in range(0, len(lanq)):
    for q in lanq[l]:
        assign.append((lan[l], q))
# print(sorted(assign, key=lambda x : x[1]))
assign.sort(key= lambda x: x[1])
with open('task', 'w') as t:
    for q in assign:
        t.write(str(q) + '\n')
