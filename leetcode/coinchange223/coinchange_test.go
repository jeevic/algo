package coinchange223

import "testing"

type Question struct {
	coins  []int
	amount int
	answer int
}

var questions = []Question{
	{
		coins:  []int{1, 2, 5},
		amount: 11,
		answer: 3,
	},
	{[]int{3}, 2, -1},
	{[]int{1}, 0, 0},
	{[]int{1}, 1, 1},
}

func TestCoinChange(t *testing.T) {
	for _, q := range questions {
		output := CoinChange(q.coins, q.amount)
		if output != q.answer {
			t.Errorf("[errror]conis:%v, amount:%d output:%d not match answer:%d", q.coins, q.amount, output, q.answer)
		} else {
			t.Logf("conis:%v, amount:%d output:%d match answer:%d", q.coins, q.amount, output, q.answer)
		}
	}
}
