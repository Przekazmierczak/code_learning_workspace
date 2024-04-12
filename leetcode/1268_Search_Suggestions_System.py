"""
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
"""

class Solution:
    # def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        
        def searchleft(l, r, products, index, letter):
            while l <= r:
                mid = (l + r) // 2
                if index > len(products[mid]) - 1 or products[mid][index] < letter:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        def searchright(l, r, products, index, letter):
            while l <= r:
                mid = (l + r) // 2
                if index > len(products[mid]) - 1 or products[mid][index] <= letter:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        
        left, right = 0, len(products) - 1
        for index in range(len(searchWord)):
            curr_res = []
            count = 0
            
            curr_left = searchleft(left, right, products, index, searchWord[index])
            
            curr_right = searchright(left, right, products, index, searchWord[index])
            
            while count < 3 and curr_left + count <= curr_right:
                curr_res.append(products[curr_left + count])
                count += 1
            
            left = curr_left
            right = curr_right
            res.append(curr_res)
        
        return res
            

def main():
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"

    solution = Solution()

    result = solution.suggestedProducts(products, searchWord)
    
    print(result)


if __name__ == "__main__":
    main()