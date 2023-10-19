"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    def letterCombinations(self, digits):
        phone = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"]
        }
        if digits == "":
            return []
        
        ans = phone[int(digits[0])]

        for digit in digits[1:]:
            new_ans = []
            for ans_element in ans:
                for i in range(len(phone[int(digit)])):
                    new_ans.append(ans_element + phone[int(digit)][i])
            ans = new_ans
        
        return ans


def main():
    digits = "23"

    solution = Solution()

    result = solution.letterCombinations(digits)
    
    print(result)


if __name__ == "__main__":
    main()