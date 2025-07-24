from typing import List
from functools import lru_cache
from itertools import product

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dfs(players: tuple, round_num: int) -> List[int]:
            i, j = 0, len(players) - 1
            while i < j:
                if (players[i], players[j]) == (firstPlayer, secondPlayer) or (players[j], players[i]) == (firstPlayer, secondPlayer):
                    return [round_num, round_num]
                i += 1
                j -= 1

            next_players_sets = []

            i, j = 0, len(players) - 1
            matches = []
            while i < j:
                a, b = players[i], players[j]
                if {a, b} & {firstPlayer, secondPlayer}:
                    winner = a if a in {firstPlayer, secondPlayer} else b
                    matches.append([winner])
                else:
                    matches.append([a, b])
                i += 1
                j -= 1
            if i == j:
                matches.append([players[i]])

            for outcome in product(*matches):
                next_players = tuple(sorted(outcome))
                res = dfs(next_players, round_num + 1)
                next_players_sets.append(res)

            min_round = min(x[0] for x in next_players_sets)
            max_round = max(x[1] for x in next_players_sets)
            return [min_round, max_round]

        initial_players = tuple(range(1, n + 1))
        return dfs(initial_players, 1)
