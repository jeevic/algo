卡鲁斯卡尔 最小生成树算法

算法原理:
按照权重排序

以此从最小往并查集添加, 并判断是否连通


Prim:
首先，Prim 算法也使用贪心思想来让生成树的权重尽可能小，也就是「切分定理」，这个后文会详细解释。

其次，Prim 算法使用 BFS 算法思想 和 visited 布尔数组避免成环，来保证选出来的边最终形成的一定是一棵树。
Prim 算法不需要事先对所有边排序，而是利用优先级队列动态实现排序的效果，所以我觉得 Prim 算法类似于 Kruskal 的动态过程。
