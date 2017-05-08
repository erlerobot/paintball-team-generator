# -*- coding: utf-8 -*-
import random

team = ["Risto", "Asier", "Lander", "Irati", "Iñigo", "Alex",
"Víctor", "Carlos San Vicente", "Carlos Uraga", "Patxi", "Aitor"]
team_size = len(team)

random.shuffle(team) # shuffle the team
team1 = team[0:team_size/2]
team2 = team[team_size/2:]

print("Generating random teams...")
print("Team 1:", team1)
print("Team 2:", team2)
