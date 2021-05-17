def update_score(oldscore, team):
    """Deze functie berekent de nieuwe stand, vertrekkend van
    de oude stand "oldscore" als "team" net gescoord heeft.
    De nieuwe stand wordt als resultaat teruggegeven.
    oldscore: een tuple van 4 nummers, set thuis, set away, punten thuis,
    punten away
    team: de ploeg die net scoorde, "H" voor thuis, "A" voor away
    """
    sets_h = oldscore[0]
    sets_a = oldscore[1]
    points_h = oldscore[2]
    points_a = oldscore[3]

    # schrijf hier de nodige code om de testen te doen slagen

    last_set = True
    if sets_h == 2 and sets_a == 2:

    if team == "H":
        points_h += 1

    if team == "A":
        points_a += 1

    if last_set == False:
        if points_h >= 25:
            if points_a < points_h - 1:
                points_h = 0
                points_a = 0
                sets_h += 1

    if last_set == False:
        if points_a >= 25:
            if points_h < points_a -1:
                points_h = 0
                points_a = 0
                sets_a += 1

    return sets_h, sets_a, points_h, points_a