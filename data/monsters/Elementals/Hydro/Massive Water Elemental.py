massive_water_elemental = genMonster("Massive Water Elemental", 11, 10499) #same corpse id as water elem need to add aid to corpse bodies
massive_water_elemental.health(1250, healthmax=1250)
massive_water_elemental.type("undead")
massive_water_elemental.defense(armor=48, fire=0, earth=0, energy=1.25, ice=0, holy=0.5, death=0.5, physical=0.4, drown=1)
massive_water_elemental.experience(1100)
massive_water_elemental.speed(500)
massive_water_elemental.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
massive_water_elemental.walkAround(energy=1, fire=0, poison=0)
massive_water_elemental.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
massive_water_elemental.melee(165)
massive_water_elemental.loot( ("fish", 59.25, 2), ("platinum coin", 29.5, 2), (2148, 100, 100), ("energy ring", 1.0), ("rainbow trout", 1.5), ("great health potion", 11.75), ("small diamond", 3.25, 2), ("great mana potion", 8.75), ("green perch", 1.0), ("small emerald", 3.25, 2), ("life ring", 1.0) )