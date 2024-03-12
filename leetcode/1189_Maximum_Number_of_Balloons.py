"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""

class Solution:
    # def maxNumberOfBalloons(self, text: str) -> int:     
    def maxNumberOfBalloons(self, text):     
        count = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }
    
        for letter in text:
            if letter in count:
                count[letter] += 1
        
        onetime = ["b", "a", "n"]
        
        res = float("inf")
        for letter in count:
            if letter in onetime:
                res = min(count[letter], res)
            else:
                res = min((count[letter] // 2), res)
                
        return res
            

def main():
    text = "loonbalxballpoon"

    solution = Solution()

    result = solution.maxNumberOfBalloons(text)
    
    print(result)


if __name__ == "__main__":
    main()