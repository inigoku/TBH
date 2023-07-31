import random

# Clase base para dados
class D:
  def __init__(self, nOfDice, nOfSides):
    self.nOfDice = nOfDice
    self.nOfSides = nOfSides

  def roll(self):
    return sum(random.randint(1, self.nOfSides) for i in range(self.nOfDice))
  
  
class Result:
  CRITICAL = 1
  PASS = 2
  FAIL = 3
  BOTCH = 4

class Modifier:
  ADVANTAGE = 1
  NONE = 2
  DISADVANTAGE = 3

class Check:
  @staticmethod
  def attributeTest(attr, modifier = Modifier.NONE, bonus = 0):
    result = D(1,20).roll()
    #Apply modifier if there is
    if modifier == Modifier.ADVANTAGE:
      result2 = D(1,20).roll()
      if result2 < result:
        result = result2
    elif modifier == Modifier.DISADVANTAGE:
      result2 = D(1,20).roll()
      if result2 > result:
        result = result2
    #Apply bonus if there is
    result += bonus
    #Check result against attribute
    if result == 1:
      return Result.CRITICAL
    elif result == 20:
      return Result.BOTCH
    elif result < attr:
      return Result.PASS
    else:
      return Result.FAIL
