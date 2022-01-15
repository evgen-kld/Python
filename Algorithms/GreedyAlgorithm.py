states = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
final_statios = set()
while states:
    best_station = None
    states_covered = ()
    for station, states_for_station in stations.items():
        covered = states & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states -= states_covered
    final_statios.add(best_station)
print(final_statios)
