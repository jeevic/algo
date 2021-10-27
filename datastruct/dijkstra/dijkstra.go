package dijkstra

import "sort"

//迪杰斯特拉最短路径算法

//邻接表存储
var graph [][]int

//返回对应节点的相邻节点
func adj(s int) []int {
	return graph[s]
}

//边之间的权重
func weight(from int, to int) int {
	_ = from
	_ = to
	return 1
}

/**
 *
 */
func dijkstra(start int, graph [][]int) map[int]int {
	//原图
	distTo := make(map[int]int, 0)
	//
	queen := make(PrioritySlice, 0, 1)
	queen.Push(NewState(start, 0))
	distTo[0] = 0

	for !queen.Empty() {
		v := queen.pull()
		if dist, ok := distTo[v.Id]; ok && dist < v.DistFromStart {
			continue
		}
		neighbors := adj(v.Id)
		for _, neighbor := range neighbors {
			weight := weight(v.Id, neighbor)
			if dist, ok := distTo[neighbor]; ok {
				if dist < v.DistFromStart+weight {
					continue
				}
			}
			queen.Push(NewState(neighbor, v.DistFromStart+weight))
			distTo[neighbor] = v.DistFromStart + weight
		}
	}
	return distTo
}

type State struct {
	Id            int
	DistFromStart int
}

func NewState(Id int, DistFromStart int) *State {
	return &State{Id: Id, DistFromStart: DistFromStart}
}

type PrioritySlice []*State

func (s PrioritySlice) Len() int {
	return len(s)
}

func (s PrioritySlice) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s PrioritySlice) Less(i, j int) bool {
	return s[i].DistFromStart < s[j].DistFromStart
}

func (s *PrioritySlice) Push(state *State) {
	*s = append(*s, state)
	sort.Sort(*s)
}

func (s *PrioritySlice) pull() *State {
	if s.Len() > 0 {
		v := (*s)[0]
		*s = (*s)[1:]
		return v
	}
	return nil
}

func (s *PrioritySlice) Empty() bool {
	return s.Len() == 0
}
