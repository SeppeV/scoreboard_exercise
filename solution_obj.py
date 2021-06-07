class Game:
    """Deze class houdt de stand bij, en voorziet een functie
    om de nieuwe stand te berekenen.
    """

    def __init__(self):
        """Zet de stand op de beginstand bij aanvang van de wedstrijd"""
        # TODO: Gebruik onderstaande member variables,
        # maar corrigeer de initiele waardes:
        self.sets_home = 0
        self.sets_away = 0
        self.points_home = 0
        self.points_away = 0
        self.set_nr = 1

    def get_max_points(self):
        """Geef het maximaal aantal punten voor deze set terug."""
        # TODO: Geef de correcte waarde terug afhankelijk van
        # de set_nr.
        if self.set_nr <= 4:
            return 25
        else:
            return 15

