from typing import Any

class QueryBuilder:
    def __init__(self, pino = None):
        if pino == None:
            pino = All()
        self.pino_olio = pino

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.pino_olio, HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.pino_olio, HasFewerThan(value, attr)))
    
    def plays_in(self, team):
        return QueryBuilder(And(self.pino_olio, PlaysIn(team)))
    
    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self.pino_olio


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return False
            
        return True
    

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    
class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
            
        return False