spider_queen = genMonster("Spider Queen", 219, 5995)
spider_queen.health(225)
spider_queen.type("slime")
spider_queen.defense(-1)
spider_queen.experience(120)
spider_queen.speed(280)
spider_queen.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=False, targetDistance=1, runOnHealth=0)
spider_queen.walkAround(energy=0, fire=0, poison=0)
spider_queen.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)