"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
"""

class Solution:
    # def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    def isNStraightHand(self, hand, groupSize):
        LEN = len(hand)
        cards = {}

        if LEN % groupSize:
            return False
        
        num = LEN // groupSize
        
        for card in hand:
            if not card in cards:
                cards[card] = 0
            cards[card] += 1

        for _ in range(num):
            first = min(cards)
            for i in range(groupSize):
                if first + i not in cards:
                    return False
                cards[first + i] -= 1
                if cards[first + i] == 0:
                    del cards[first + i]

        return True


def main():
    hand = [8,10,12]
    groupSize = 3

    solution = Solution()

    result = solution.isNStraightHand(hand, groupSize)
    
    print(result)


if __name__ == "__main__":
    main()