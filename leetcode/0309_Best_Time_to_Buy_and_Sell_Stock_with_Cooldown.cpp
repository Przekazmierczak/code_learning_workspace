/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 
Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
*/

#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int stack[2] = {-INT_MAX, -INT_MAX};
        int noStack[2] = {0, 0};
        int currStack = 0;
        int currNoStack = 0;

        for (int i = 0; i < prices.size();i++) {
            currStack = (std::max(noStack[0] -prices[i], stack[1]));
            currNoStack = (std::max(stack[1] + prices[i], noStack[1]));

            stack[0] = stack[1];
            noStack[0] = noStack[1];
            stack[1] = currStack;
            noStack[1] = currNoStack;
        }
        
        return std::max(stack[1], noStack[1]);
    }
};