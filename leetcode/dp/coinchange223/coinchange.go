package coinchange223

/**
 * 暴力法
 * base amount = 0  count = 0
 * 状态 amount
 * 选择  min([f(amount - coins[i])])
 * 方程
 *	fx(n) = {}  1 + min(f(n-coin) coin -> coins)
 */

func CoinChange(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	if amount < 0 {
		return -1
	}

	var res int = amount + 5
	for _, coin := range coins {
		if amount-coin < 0 {
			continue
		}
		v := CoinChange(coins, amount-coin)
		if v == -1 {
			continue
		}
		res = Min(res, 1+v)
	}
	if res == amount+5 {
		return -1
	}
	return res
}

/**
 * 备忘录法
 *
 */
func CoinChangeMem(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	amountMem := initSlice(amount+1, amount+1)
	return helper(amountMem, coins, amount)
}

func helper(amountMem []int, coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	if amountMem[amount] <= amount {
		return amountMem[amount]
	}
	var res int = amount + 5
	for _, coin := range coins {
		if amount-coin < 0 {
			continue
		}
		v := CoinChange(coins, amount-coin)
		if v == -1 {
			continue
		}
		res = Min(res, 1+v)
	}
	if res == amount+5 {
		amountMem[amount] = -1
	} else {
		amountMem[amount] = res
	}
	return amountMem[amount]
}

func Min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func initSlice(n int, val int) []int {
	var mem = make([]int, n)
	for i := 0; i < len(mem); i++ {
		mem[i] = val
	}
	return mem
}

/**
 * 自底而上 - 循环解法
 *
 */
func CoinChangeLoop(coins []int, amount int) int {
	if amount < 0 {
		return -1
	}
	if amount == 0 {
		return 0
	}
	dp := initSlice(amount+1, amount+1)
	dp[0] = 0

	for i := 1; i <= amount; i++ {
		var res = amount + 1
		for _, coin := range coins {
			if i-coin < 0 {
				continue
			}
			v := dp[i-coin]
			if v == amount+1 || v == -1 {
				continue
			}
			res = Min(res, 1+v)
		}
		if res == amount+1 {
			dp[i] = -1
		} else {
			dp[i] = res
		}
	}
	return dp[amount]
}
