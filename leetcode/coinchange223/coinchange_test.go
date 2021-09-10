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

func TestCoinChangeMem(t *testing.T) {
	for _, q := range questions {
		output := CoinChangeMem(q.coins, q.amount)
		if output != q.answer {
			t.Errorf("[errror]conis:%v, amount:%d output:%d not match answer:%d", q.coins, q.amount, output, q.answer)
		} else {
			t.Logf("conis:%v, amount:%d output:%d match answer:%d", q.coins, q.amount, output, q.answer)
		}
	}
}

func TestCoinChangeLoop(t *testing.T) {
	for _, q := range questions {
		output := CoinChangeLoop(q.coins, q.amount)
		if output != q.answer {
			t.Errorf("[errror]conis:%v, amount:%d output:%d not match answer:%d", q.coins, q.amount, output, q.answer)
		} else {
			t.Logf("conis:%v, amount:%d output:%d match answer:%d", q.coins, q.amount, output, q.answer)
		}
	}
}

func BenchmarkCoinChange(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, q := range questions {
			output := CoinChange(q.coins, q.amount)
			if output != q.answer {
				b.Errorf("[errror]conis:%v, amount:%d output:%d not match answer:%d", q.coins, q.amount, output, q.answer)
			}
		}
	}
}

func BenchmarkCoinChangeMem(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, q := range questions {
			output := CoinChangeMem(q.coins, q.amount)
			if output != q.answer {
				b.Errorf("[errror]conis:%v, amount:%d output:%d not match answer:%d", q.coins, q.amount, output, q.answer)
			}
		}
	}
}

func BenchmarkCoinChangeLoop(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		for _, q := range questions {
			output := CoinChangeLoop(q.coins, q.amount)
			if output != q.answer {
				b.Errorf("[errror]conis:%v, amount:%d output:%d not match answer:%d", q.coins, q.amount, output, q.answer)
			}
		}
	}
}
