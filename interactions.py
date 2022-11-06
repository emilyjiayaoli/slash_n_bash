from player import *
from wind_enemy import *

def isAttacking(entity):
    return entity.combatTuple[0] != 0

def isVulnerable(entity):
    return entity.combatTuple[2] == 'vulnerable'

def isHit(entity):
    entity.state = 'hit'
    entity.animationCounter = 0

def checkInteractions(player, enemy):
    playerBlockEff = player.combatTuple[1]
    if isAttacking(player) and isVulnerable(enemy):
        dmg = player.combatTuple[0]
        enemy.hp -= dmg
        isHit(enemy)
    elif isAttacking(player) and enemy.combatTuple[2] == 'counterhit':
        player.hp -= 5
    if isAttacking(enemy) and isVulnerable(player):
        dmg = enemy.combatTuple[0]
        player.hp -= dmg
        isHit(player)
    elif playerBlockEff != 1 and isAttacking(enemy):
        player.hp -= dmg*(1 - playerBlockEff)