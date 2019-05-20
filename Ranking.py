from datetime import date

name = ""
rank = []

def SetUsername():
    global name
    name = input("USERNAME: ")

def GetUsername():
    return name

def GetRanking():
    return rank

def SetRank(score,level,name):
    with open("Ranking.txt", "a") as txt:
        day = date.today()
        txt.write(str(day) + ";")
        txt.write(name + ";")
        txt.write(str(level) + ";")
        txt.write(str(score) + ";")
        txt.write("\n")    
        txt.close()

def LoadRanking():
    global rank
    rank = []
    file = open("Ranking.txt", 'r')
    for linha in file:
        user = linha.rstrip().split(';')
        rank.append(user)
    orderRanking(rank)
        
def orderRanking(rank):
    for i in range(len(rank)-1):
        for j in range(i+1, len(rank)):
            if int(rank[i][3]) < int(rank[j][3]):
                rank[i], rank[j] = rank[j], rank[i]
