package nqueens

import "strings"

func SolveNQueens(n int) [][]string {
	res := make([][]string, 0, 1)
	boards := InitBoards(n)
	backTrack(boards, &res, n, 0)
	return res
}

func backTrack(boards []string, res *[][]string, n int, row int) {
	//if length match n return
	if row == n {
		cp := CopyBoards(boards)
		*res = append(*res, cp)
		return
	}

	//loop  choice rows equal Q
	for col := 0; col < n; col++ {
		if !IsValid(boards, row, col) {
			continue
		}
		ro := []byte(boards[row])
		ro[col] = 'Q'
		boards[row] = string(ro)
		backTrack(boards, res, n, row+1)
		ro = []byte(boards[row])
		ro[col] = '.'
		boards[row] = string(ro)
	}
}

func IsValid(boards []string, row int, col int) bool {
	n := len(boards)
	//当前列是否
	for i := row; i >= 0; i-- {
		if boards[i][col] == 'Q' {
			return false
		}
	}
	//左上列
	for i, j := row-1, col-1; i >= 0 && j >= 0; {
		if boards[i][j] == 'Q' {
			return false
		}
		i--
		j--
	}
	//右上列

	for i, j := row-1, col+1; i >= 0 && j < n; {
		if boards[i][j] == 'Q' {
			return false
		}

		i--
		j++
	}
	return true
}

func CopyBoards(a []string) []string {
	cp := make([]string, len(a))
	for index, item := range a {
		cp[index] = item
	}
	return cp
}

func InitBoards(n int) []string {
	borads := make([]string, n)
	for i := 0; i < n; i++ {
		borads[i] = strings.Repeat(".", n)
	}
	return borads
}
