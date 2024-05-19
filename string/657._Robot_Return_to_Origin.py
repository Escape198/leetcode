class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = moves.count('U') - moves.count('D')
        horizontal = moves.count('R') - moves.count('L')

        return vertical == 0 and horizontal == 0
