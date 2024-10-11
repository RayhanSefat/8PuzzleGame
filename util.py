# any state is a 3 X 3 matrix

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