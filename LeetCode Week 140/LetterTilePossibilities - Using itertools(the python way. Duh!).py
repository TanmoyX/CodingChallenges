'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
'''

from itertools import permutations

def numTilePossibilities(tiles: str) -> int:
    res = []
    for i in range(1, len(tiles)+1):
        res += list(permutations(tiles, i))
        res += list(permutations(tiles[::-1], i))
    return len(set(res))

print(numTilePossibilities("AAABBC"))
    
