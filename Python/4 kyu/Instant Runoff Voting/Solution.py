def runoff(voters):
    votesCast = []
    totalVotes = 0
    votesCast = countVotes(voters)

    for val in voters[0]:
        if findVote(votesCast, val) == 404:
            votesCast.append([val,0])

    print(votesCast)

    print("")

    while(1):
        totalVotes = tallyTotal(votesCast)
        mostVotes = findLargest(votesCast)

        if(countAtValue(votesCast, mostVotes) == 1):
            if float(mostVotes) / float(totalVotes) > 0.5:
                votesCast = getVoteWithValue(votesCast, mostVotes)
                return votesCast[0]
            else:
                leastVotes = findLowest(votesCast)
                print("leastVotes = " + str(leastVotes))
                if leastVotes == mostVotes:
                    return None
                else:
                    removeLowest(voters, getVoteWithValue(votesCast, leastVotes))
                    votesCast = countVotes(voters)
        else:
            leastVotes = findLowest(votesCast)
            if leastVotes == mostVotes:
                return None
            else:
                while(getVoteWithValue(votesCast, leastVotes) != 404):
                    removeLowest(voters, getVoteWithValue(votesCast, leastVotes))
                    votesCast = countVotes(voters)
        printVoters(voters)
        print("")

def printVoters(voters):
    for row in voters:
        print(row)

def countVotes(voters):
    votesCast = []

    for row in voters:
        print("Vote = " + row[0])
        if findVote(votesCast, row[0]) == 404:
            votesCast.append([row[0],1])
        else:
            votesCast[findVote(votesCast, row[0])][1] += 1

    return votesCast

def tallyTotal(votesCast):
    total = 0

    for group in votesCast:
        total += group[1]

    return total

def findVote(votesCast, vote):
    for group_i in range(0, len(votesCast)):
        if votesCast[group_i][0] == vote:
            return group_i
    return 404

def findLargest(votesCast):
    largest = votesCast[0][1]
    for group in votesCast:
        if group[1] > largest:
            largest = group[1]
    return largest

def findLowest(votesCast):
    lowest = votesCast[0][1]
    for group in votesCast:
        if group[1] < lowest:
            lowest = group[1]
    return lowest

def countAtValue(votesCast, value):
    count = 0
    for group in votesCast:
        if group[1] == value:
            count += 1
    return count

def getVoteWithValue(votesCast, value):
    votesWithValue = []

    for group in votesCast:
        if value == group[1]:
            votesWithValue.append(group[0])
    
    if(len(votesWithValue) == 0):
        return 404
    else:
        return votesWithValue

def removeLowest(voters, value):
    for val in value:
        for row in voters:
            for row_i in range(0, len(row)):
                print(row_i)
                if row[row_i] == val:
                    row.pop(row_i)
                    break
