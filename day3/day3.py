def star1(test: str) -> int:
    claims = test.splitlines()
    squares = {}
    for i in claims:
        claimData = i.split()
        claimLocation = claimData[2][:-1].split(",")
        claimSize = claimData[3].split("x")
        for j in range(int(claimLocation[0]), int(claimLocation[0]) + int(claimSize[0])):
            for k in range(int(claimLocation[1]), int(claimLocation[1]) + int(claimSize[1])):
                if (j, k) in squares:
                    squares[(j, k)] += 1
                else:
                    squares[(j, k)] = 1
    counter = 0
    for j in squares.values():
        if j >= 2:
            counter += 1
    return counter


def star2(test: str) -> int:
    claims = test.splitlines()
    takenSquares = {}
    takenSquaresByClaimID = {}
    for i in claims:
        claimData = i.split()
        claimLocation = claimData[2][:-1].split(",")
        claimSize = claimData[3].split("x")
        takenSquaresByClaimID[claimData[0][1:]] = []
        for j in range(int(claimLocation[0]), int(claimLocation[0]) + int(claimSize[0])):
            for k in range(int(claimLocation[1]), int(claimLocation[1]) + int(claimSize[1])):
                takenSquaresByClaimID[claimData[0][1:]].append((j, k))
                if (j, k) in takenSquares:
                    takenSquares[(j, k)] += 1
                else:
                    takenSquares[(j, k)] = 1
    overlappingSquares = set()
    for j in takenSquares:
        if takenSquares[j] >= 2:
            overlappingSquares.add(j)
    for w in takenSquaresByClaimID:
        nooverlap = False
        for x in takenSquaresByClaimID[w]:
            if x in overlappingSquares:
                nooverlap = True
                break
        if not nooverlap:
            return w
