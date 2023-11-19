"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 
Constraints:

1 <= s.length <= 20
s consists of digits only.
"""

class Solution:
    # def restoreIpAddresses(self, s: str) -> List[str]:
    def restoreIpAddresses(self, s):
        ans = []
        s_len = len(s)
        def restore(pointer, counter, sub_list):
            if pointer == s_len and counter == 4:
                ans.append(sub_list[:-1])
                return
            
            if pointer == s_len or counter == 4:
                return

            restore(pointer + 1, counter + 1, sub_list + s[pointer] + ".")

            pointer += 1
            if int(s[pointer - 1: pointer + 1]) >= 10:
                restore(pointer + 1, counter + 1, sub_list + s[pointer - 1: pointer + 1] + ".")

            pointer += 1    
            if 100 <= int(s[pointer - 2: pointer + 1]) <= 255:
                restore(pointer + 1, counter + 1, sub_list + s[pointer - 2: pointer + 1] + ".")

            return
        
        restore(0, 0, "")
        
        return ans

def main():
    s = "25525500"

    solution = Solution()

    result = solution.restoreIpAddresses(s)
    
    print(result)


if __name__ == "__main__":
    main()