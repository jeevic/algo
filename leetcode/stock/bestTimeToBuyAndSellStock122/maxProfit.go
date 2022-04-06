package main

const INT_MAX = int(^uint(0) >> 1)
const INT_MIN = ^INT_MAX


/**
 * 122. 买卖股票的最佳时机2
 * @see https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
 */

func Max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

/**
 * base:
 *
 *  dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + p)
 *  dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - p)
 *
 */
func MaxProfit(prices []int) int {
	n := len(prices)
	dp := make([][2]int, n)
	for i := 0; i < n; i++ {
		if i - 1 == -1 {
			dp[0][0] = 0
			dp[0][1] = -prices[i]
			continue
		}
		dp[i][0] = Max(dp[i - 1][0], dp[i - 1][1] + prices[i])
		dp[i][1] = Max(dp[i - 1][1], dp[i - 1][0] - prices[i])
	}
	return dp[n - 1][0]
}

func  MaxProfit_o(prices []int) int {
	n := len(prices)
	dI0 := 0;  dI1 := INT_MIN
	for i := 0; i < n; i++ {
		dI0 = Max(dI0, dI1 + prices[i])
		dI1 = Max(dI1, -prices[i])
	}
	return dI0
}


/*
 * max  profit1
 */
func maxProfit1(prices []int) int {
	count := len(prices)
	if count < 1 {
		return 0
	}
	profit := 0
	for i := 0; i < count; i++ {
		profit = Max(profit, Profit(i, prices))
	}
	return profit
}

func Profit(i int, prices []int) int {
	result := 0
	for j := i + 1; j < len(prices); j++ {
		result = Max(result, prices[j] - prices[i])
	}
	return result
}


/**
 *  n为天数 k为交易次数  s状态:buy seller buy-reset seller-reset
 *  for i = 0; i < n; i++
 :     for 1 <= k <= K
         for s in [buy, seller]
			d[i][k][buy] = max(d[i-1][k][s], d[i-1][k-1][seller] + cp)
			d[i][k][seller] = max(d[i-1][k][s], d[i-1][k-1][buy] - cp)

         d[-1][...][0] = 0  d[-1][...][1] = -infinity
		 d[...][0][0] = 0 d[...][0][1] = -infinity
 *
 */
