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
	var mem = make([]int, 0, len(coins))
	for _, coin := range coins {
		if amount-coin < 0 {
			continue
		}
		v := CoinChange(coins, amount-coin)
		if v == -1 {
			continue
		}
		mem = append(mem, CoinChange(coins, amount-coin))
	}
	if len(mem) == 0 {
		return -1
	}
	return 1 + min(mem)
}

func min(mem []int) int {
	min := mem[0]
	for _, val := range mem {
		if val < min {
			min = val
		}
	}
	return min
}
