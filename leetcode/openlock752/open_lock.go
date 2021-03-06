package openlock752

func OpenLock(deadends []string, target string) int {
	//队列
	queens := make(Queen, 0, 1)
	step := 0

	queens = append(queens, "0000")
	visit := make(map[string]uint8)

	for !queens.Empty() {
		size := queens.Len()
		for i := 0; i < size; i++ {
			//遍历当前值
			secr := queens.Dequeue()

			//secr 等于 目标
			if target == secr {
				return step
			}

			if Contain(secr, deadends) {
				continue
			}

			for j := 0; j < len(secr); j++ {
				down := turnDown(secr, j)
				if _, ok := visit[down]; !ok {
					visit[down] = 1
					queens = append(queens, down)
				}

				up := turnUp(secr, j)
				if _, ok := visit[up]; !ok {
					visit[up] = 1
					queens = append(queens, up)
				}
			}
		}
		step++
	}

	return -1
}

/**
 * 双向BFS遍历
 *
 */
func DoubleDirectionOpenLock(deadends []string, target string) int {

	//队列
	q1 := make(Queen, 0, 1)
	q2 := make(Queen, 0, 1)
	step := 0
	visit := make(map[string]uint8)
	q1 = append(q1, "0000")
	//visit["0000"] = 1

	q2 = append(q2, target)
	//visit[target] = 1

	for !q1.Empty() && !q2.Empty() {
		temp := make(Queen, 0, 1)

		size := q1.Len()
		for i := 0; i < size; i++ {
			//遍历当前值
			secr := q1.Dequeue()

			if Contain(secr, deadends) {
				continue
			}

			if Contain(secr, q2) {
				return step
			}
			visit[secr] = 1

			for j := 0; j < len(secr); j++ {
				down := turnDown(secr, j)
				if _, ok := visit[down]; !ok {
					temp = append(temp, down)
				}

				up := turnUp(secr, j)
				if _, ok := visit[up]; !ok {
					temp = append(temp, up)
				}
			}
		}
		step++
		q1 = q2
		q2 = temp
	}
	return -1
}

// 0 -1  9 - 0
func turnUp(s string, index int) string {
	st := []byte(s)
	if s[index] == '9' {
		st[index] = byte('0')
	} else {
		st[index] = st[index] + 1
	}
	return string(st)
}

// 0 -> 9
func turnDown(s string, index int) string {
	st := []byte(s)
	if s[index] == '0' {
		st[index] = byte('9')
	} else {
		st[index] = st[index] - 1
	}
	return string(st)
}

type Queen []string

func (q *Queen) Enqueue(s string) {
	*q = append(*q, s)
}

func (q *Queen) Dequeue() string {
	if q.Len() > 0 {
		node := (*q)[0]
		*q = (*q)[1:]
		return node
	}
	return ""
}

func (q *Queen) Len() int {
	return len(*q)
}

func (q *Queen) Empty() bool {
	return q.Len() == 0
}

func Contain(s string, ss []string) bool {
	for _, v := range ss {
		if v == s {
			return true
		}
	}
	return false
}
