import util
import collections


def generateAndSaveValidStates():
    targetStateNumber = util.stateToNumber(util.targetState)

    queue = collections.deque([targetStateNumber])

    visitedStates = set([targetStateNumber])

    with open('valid_states.txt', 'w') as file:
        file.write(f'{targetStateNumber}\n')

        while queue:
            currentNumber = queue.popleft()
            currentState = util.numberToState(currentNumber)

            for transition in [util.leftTransition, util.rightTransition, util.upTransition, util.downTransition]:
                nextState = transition(currentState)
                if nextState is not None:
                    nextStateNumber = util.stateToNumber(nextState)
                    if nextStateNumber not in visitedStates:
                        visitedStates.add(nextStateNumber)
                        queue.append(nextStateNumber)
                        file.write(f'{nextStateNumber}\n')

    print(f"Total valid states generated and saved: {len(visitedStates)}")


generateAndSaveValidStates()
