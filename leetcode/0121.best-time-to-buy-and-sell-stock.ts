function maxProfit(prices: number[]): number {
    let l = 0;
    let r = 1;
    let N = prices.length - 1;
    let profit = 0;
    while(r <= N) {
        let diff = prices[r] - prices[l];
        profit = Math.max(profit, diff);
        while(prices[l] > prices[r]) {
            l = l + 1
        }
        r = r + 1 
    }
    return profit
};