import heapq
class Node:
	def __init__(self,value,arr_pos,value_pos):
		self.value = value
		self.arr_pos = arr_pos
		self.value_pos = value_pos


class ComparableNode:
	def __init__(self,node):
			self.node = node

	def __le__(self,other):
    		return self.node.value <= self.other.value

class Solution:
	def merge(self,arr):
		res = []
		tmp = []
		#setattr(arr, "__lt__", lambda self, other: self.val <= other.val)
		for i in range(len(arr)):
			node = Node(arr[i][0],arr[i],0)
			tmp.append(ComparableNode(node))

		heapq.heapify(tmp)
		
		#heapq.heapify()

		#heapq.heapify()
		while len(heapq) != 0:
			top = heapq.heappop()
			res.append(top.value)
			length = len(arr[top.arr_pos])
			if top.value_pos+1 < length:
				heapq.heappush(arr[top.arr_pos][top.value_pos+1])

		return res


arr = [[2,5,7],[1,4],[6,9]]
out = merge(arr)
print(out)