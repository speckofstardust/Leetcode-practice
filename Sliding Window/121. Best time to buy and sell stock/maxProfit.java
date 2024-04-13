class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0, i=0, j=1;
        while(j<prices.length){
            if(prices[i] < prices[j]){
                if(maxprofit < prices[j] - prices[i])
                    maxprofit = prices[j] - prices[i];
            }
            else {
                i = j;
            }
            j++;
        }
        return maxprofit;
    }
}
