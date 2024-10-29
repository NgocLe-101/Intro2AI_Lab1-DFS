import os
def getAllTestFiles():
    return [f for f in os.listdir('Test_cases') if os.path.isfile(os.path.join('Test_cases', f))]


def getInfoFromTestFile(filename) -> dict:
    with open(os.path.join('Test_cases', filename)) as f:
        data = f.read().split('\n')
        rockWeights = data[0].split(' ')
        mazeMatrix = [list(row) for row in data[1:]]
        return {
            'name': filename,
            'caseIndex': int(filename.split('-')[1].split('.')[0]),
            'mazeMatrix': mazeMatrix,
            'rockWeights': rockWeights,
        }

def exportSolutionToFile(caseIndex: int, algoName: str, steps: int, path: str, cost: int, nodesGenerated: int, time: float, memory: float) -> bool:
    with open(os.path.join('Outputs', f'output-{caseIndex:02}.txt'), 'w') as f:
        data = f'{algoName}\n'
        data += f'Steps: {steps}, Total weight: {cost}, Nodes generated: {nodesGenerated}, Time: {time:.5f}s, Memory: {memory:.5f} MB\n'
        data += f'{path}'
        f.write(data)