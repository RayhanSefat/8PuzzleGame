import util

class PuuzleSolver:
    def __init__(self, inputState):
        self.inputState = inputState
        self.foundTarget = False
        self.nodeList = []

    def checkInputExistsInFile(self):
        pass

    def checkVaalidty(self):
        for i in range(util.N):
            if len(self.inputState[i]) != util.N:
                return False
            
        return self.checkInputExistsInFile()

    def dls(self, mxDepth, currentDepth, node):
        nodeState = util.numberToState(node)

        if nodeState == util.targetState:
            self.foundTarget = True
            self.nodeList.append(node)
            return
        
        if currentDepth == mxDepth:
            return
        
        transitionStates = []
        transitionStates.append(util.leftTransition(nodeState))
        transitionStates.append(util.rightTransition(nodeState))
        transitionStates.append(util.upTransition(nodeState))
        transitionStates.append(util.downTransition(nodeState))

        for transitionState in transitionStates:
            if transitionState == None:
                continue

            transitionStateCorespondingNumber = util.stateToNumber(transitionState)
            self.dls(mxDepth, currentDepth + 1, transitionStateCorespondingNumber)

            if self.foundTarget == True:
                self.nodeList.append(node)
                return

    def iddls(self):
        inputStateCorrespondingNumber = util.stateToNumber(self.inputState)

        mxDepth = 1
        while True:
            self.dls(mxDepth, 0, inputStateCorrespondingNumber)

            if self.foundTarget == True:
                break   

            mxDepth += 1

    def solvePuzzle(self):
        if self.checkVaalidty() == False:
            print('Given input in not valid')
            return
        
        print('Solution exists!\n')
        
        self.iddls()

        self.nodeList = self.nodeList[::-1]
        stateNumber = 0
        for node in self.nodeList:
            print(f'State {stateNumber}:')
            stateNumber += 1
            nodeState = util.numberToState(node)
            for row in nodeState:
                print(row)
            print('')
        
def getInputState():
        print('Enter the input state:')
        inputState = [None] * util.N
        for i in range(util.N):
            inputState[i] = list(map(int, input().split()))
        print('')

        return inputState

inputState = getInputState()
puuzleSolver = PuuzleSolver(inputState)
puuzleSolver.solvePuzzle()