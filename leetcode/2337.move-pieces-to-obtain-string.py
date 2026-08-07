class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s, t = 0, 0
        n, m = len(start), len(target)

        while s < n or t < m:
            # skip underscores in both
            while s < n and start[s] == '_':
                s += 1
            while t < m and target[t] == '_':
                t += 1

            # one string ran out before the other
            if s == n or t == m:
                return s == n and t == m

            # pieces must match
            if start[s] != target[t]:
                return False

            # position constraints
            if start[s] == 'L' and s < t:
                return False
            if start[s] == 'R' and s > t:
                return False

            s += 1
            t += 1

        return True