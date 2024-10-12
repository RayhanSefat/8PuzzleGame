# any state is a 3 X 3 matrix

import copy

N = 3
targetState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def stateToNumber(state):
    result = 0
    
    for i in range(N):
        for j in range(N):
            x = int(state[i][j])
            result = (result * 10) + x

    return result

def numberToState(number):
    result = []

    for i in range(N):
        currentRow = []
        for j in range(N):
            currentRow.append(number % 10)
            number //= 10
        currentRow = currentRow[::-1]
        result.append(currentRow)

    result = result[::-1]
    return result

def leftTransition(state):
    changedState = copy.deepcopy(state)

    for i in range(N):
        for j in range(1, N):
            if changedState[i][j] == 0:
                changedState[i][j-1], changedState[i][j] = changedState[i][j], changedState[i][j-1]
                return changedState

    return None

def rightTransition(state):
    changedState = copy.deepcopy(state)

    for i in range(N):
        for j in range(N-1):
            if changedState[i][j] == 0:
                changedState[i][j+1], changedState[i][j] = changedState[i][j], changedState[i][j+1]
                return changedState

    return None

def upTransition(state):
    changedState = copy.deepcopy(state)

    for i in range(1, N):
        for j in range(N):
            if changedState[i][j] == 0:
                changedState[i-1][j], changedState[i][j] = changedState[i][j], changedState[i-1][j]
                return changedState

    return None

def downTransition(state):
    changedState = copy.deepcopy(state)

    for i in range(N-1):
        for j in range(N):
            if changedState[i][j] == 0:
                changedState[i+1][j], changedState[i][j] = changedState[i][j], changedState[i+1][j]
                return changedState

    return None