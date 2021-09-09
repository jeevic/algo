package fibonacci509

/**
 * 通常用  F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 * 明确base -> 明确状态 -> 明确选择 ->定义Dp函数/数组
*/
/**
 * 递归调用
 * base: base n = 0; n = 1
 * 状态: f(x) = f(x-1) + f(x - 2)
 * 时间复杂度: O(2^n)
 */
func Fib(n int) int {
	if n < 1 {
		return 0
	}
	if n == 0 || n == 1 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}

/**
 * 备忘录法 进行剪枝条
 * 时间复杂度:O(n)
 */
func FibMem(n int) int {
	if n < 1 {
		return 0
	}
	var memeArr = make([]int, n+1)
	return helper(memeArr, n)
}

func helper(memArr []int, n int) int {
	if n == 0 || n == 1 {
		return n
	}
	if memArr[n] != 0 {
		return memArr[n]
	}
	memArr[n] = helper(memArr, n-1) + helper(memArr, n-2)
	return memArr[n]
}

/**
 * 循环法
 *
 */
func FibLoop(n int) int {
	if n < 1 {
		return 0
	}
	var memeArr = make([]int, n+1)
	memeArr[0] = 1
	memeArr[1] = 1

	for i := 2; i <= n; i++ {
		memeArr[i] = memeArr[i-1] + memeArr[i-2]
	}
	return memeArr[n]
}

/**
 * 压缩变量
 */
func FibCompress(n int) int {
	if n < 1 {
		return 0
	}
	if n == 0 || n == 1 {
		return n
	}
	var prev int = 0
	var cur int = 1
	var sum int

	for i := 2; i < n; i++ {
		sum = cur + prev
		prev = cur
		cur = sum
	}
	return sum
}
