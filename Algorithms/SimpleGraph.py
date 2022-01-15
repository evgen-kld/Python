from collections import deque

graph = {}
graph['start'] = ['2', '3']
graph['2'] = ['5', '9', '10']
graph['3'] = ['4', '6', '7']
graph['4'] = []
graph['5'] = ['11']
graph['6'] = ['7']
graph['7'] = ['3']
graph['8'] = ['13']
graph['9'] = ['10']
graph['10'] = ['12']
graph['11'] = []
graph['12'] = ['stop']


def finish(elem):
    return elem == 'stop'


def breadthFirsSearch(first_elem):
    searh_deque = deque()
    searh_deque += graph[first_elem]
    searched = []
    while searh_deque:
        elem = searh_deque.popleft()
        if not elem in searched:
            if finish(elem):
                return 'Путь найден!'
            else:
                searh_deque += graph[elem]
                searched.append(elem)
    return 'Путь не найден'


print(breadthFirsSearch('start'))
