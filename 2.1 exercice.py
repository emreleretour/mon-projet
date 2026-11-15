def compterVoix(prefs):
    voix = [0] * len(prefs[0])

    for pref in prefs:
        voix[pref[0]] += 1

    return voix

prefs = [
    [0, 1, 2],
    [1, 0, 2],
    [0, 2, 1],
    [2, 1, 0]
]

print(compterVoix(prefs))
