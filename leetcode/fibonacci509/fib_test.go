/*
 *  go test -bench . -benchmem  -cpu=2,4
	go test -bench .  -benchmem
	goos: darwin
	goarch: amd64
	pkg: algo/leetcode/fibonacci509
	BenchmarkFib-8                     25768             47357 ns/op               0 B/op          0 allocs/op
	BenchmarkFibMem-8                6432949               214 ns/op             176 B/op          1 allocs/op
	BenchmarkFibLoop-8              13539915                84.8 ns/op           176 B/op          1 allocs/op
	BenchmarkFibCompress-8          100000000               10.9 ns/op             0 B/op          0 allocs/op
*/

package fibonacci509

import "testing"

const Num int = 20

func BenchmarkFib(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		Fib(Num)
	}
}

func BenchmarkFibMem(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		FibMem(Num)
	}
}

func BenchmarkFibLoop(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		FibLoop(Num)
	}
}

func BenchmarkFibCompress(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		FibCompress(Num)
	}
}
