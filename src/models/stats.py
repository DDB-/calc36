from exceptions import InvalidBattleResult

class CombatStats:
    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def print_summary(self):
        total_runs = len(self.results)
        attacker_wins = [x for x in self.results if x.winner == "Attacker"]
        attacker_win_count = len(attacker_wins)
        defender_wins = [x for x in self.results if x.winner == "Defender"]
        defender_win_count = len(defender_wins)

        attacker_win_pct = attacker_win_count / total_runs * 100
        defender_win_pct = defender_win_count / total_runs * 100

        if attacker_win_count > 0:
            attacker_ipp_lost_avg = sum([x.ipp_lost for x in attacker_wins]) / attacker_win_count
            attacker_ipp_killed_avg = sum([x.ipp_killed for x in attacker_wins]) / attacker_win_count
        else:
            attacker_ipp_lost_avg = 0
            attacker_ipp_killed_avg = 0

        if defender_win_count > 0:
            defender_ipp_lost_avg = sum([x.ipp_lost for x in defender_wins]) / defender_win_count
            defender_ipp_killed_avg = sum([x.ipp_killed for x in defender_wins]) / defender_win_count
        else:
            defender_ipp_lost_avg = 0
            defender_ipp_killed_avg = 0

        print("A total of {} were simulated for this battle".format(total_runs))
        print("Attacker won {:.2f}% of the battles, averaging {:.2f} IPP killed and {:.2f} IPP lost".format(
            attacker_win_pct, attacker_ipp_killed_avg, attacker_ipp_lost_avg))

        print("Defender won {:.2f}% of the battles, averaging {:.2f} IPP killed and {:.2f} IPP lost".format(
            defender_win_pct, defender_ipp_killed_avg, defender_ipp_lost_avg))


class CombatResult:
    def __init__(self, winner, ipp_lost=0, ipp_killed=0):
        if winner is None:
            raise InvalidBattleResult("Combat must have a winner (defender wins ties)")

        self.winner = winner
        self.ipp_lost = ipp_lost
        self.ipp_killed = ipp_killed
