class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.tie()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.score_four()
        else:
            score = self.current_score()

        return score

    def tie(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def score_four(self):
        minus_result = self.player1_score - self.player2_score

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def current_score(self):
        score = ""
        score += self.get_score_text(self.player1_score)
        score = score + "-"
        score += self.get_score_text(self.player2_score)

        return score
    
    def get_score_text(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"