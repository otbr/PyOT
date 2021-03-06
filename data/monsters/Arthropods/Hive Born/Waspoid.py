waspoid = genMonster("Waspoid", 8, 5980)
waspoid.health(1100)
waspoid.type("slime")
waspoid.defense(armor=30, fire=1.1, earth=0, energy=0.75, ice=1, holy=1.05, death=0.95, physical=1.05, drown=1)
waspoid.experience(830)
waspoid.speed(270) #incorrect
waspoid.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
waspoid.walkAround(energy=1, fire=1, poison=0)
waspoid.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
waspoid.melee(250)