conjure = spell.Spell("Conjure Bolt", "exevo con mort", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=140, level=17, maglevel=0, soul=2, learned=0, vocations=(3, 7))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2543, 5))