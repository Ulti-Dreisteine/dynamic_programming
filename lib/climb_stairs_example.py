# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:32:52 2018

@author: luolei

动态规划:
*	动态规划(dynamic programming)是运筹学的一个分支，是求解决策过程(decision process)最优化的数学方法。把多阶段过程转化为一系列单阶段问题，
	利用各阶段之间的关系，逐个求解
*	使用动态规划特征：
	1. 求一个问题的最优解
	2. 大问题可以分解为子问题，子问题还有重叠的更小的子问题
	3. 整体问题最优解取决于子问题的最优解（状态转移方程）
	4. 从上往下分析问题，从下往上解决问题
	5. 讨论底层的边界问题
*	动态规划最重要的有三个概念：
	1. 最优子结构
	2. 边界
	3. 状态转移方程

测试算例为：
	有一座高度是10级台阶的楼梯，从下往上走，每跨一步只能向上1级或者2级台阶，求出一共有多少种走法。
"""
import time
import matplotlib.pyplot as plt


class ClimbingStairsProblem(object):
	"""爬楼梯问题"""
	def recursive_solution(self, n):
		"""递归算法"""
		if n <= 2:
			return n
		else:
			return self.recursive_solution(n - 1) + self.recursive_solution(n - 2)  # 这是由最后只能跨1级台阶或者2级台阶的条件决定的
	
	def _initialize_memo_map(self):
		self.memo_map = {}
	
	def memo_dict_solution(self, n):
		"""备忘录解法"""
		self._initialize_memo_map()
		if n <= 2:
			self.memo_map[n] = n
			return n
		else:
			if n in self.memo_map.keys():
				return self.memo_map[n]
			else:
				self.memo_map[n] = self.memo_dict_solution(n - 1) + self.memo_dict_solution(n - 2)
				return self.memo_map[n]
	
	def dp_solution(self, n):
		"""动态规划解法"""
		if n <= 2:
			return n
		temp_list = [0, 1, 2]
		for i in range(3, n + 1):
			temp_list.append(temp_list[-1] + temp_list[-2])
		return temp_list[-1]
	

if __name__ == '__main__':
	# 获得不同算法的时间消耗
	csp = ClimbingStairsProblem()
	methods = [csp.recursive_solution, csp.memo_dict_solution, csp.dp_solution]
	time_costs = {}
	for method in methods:
		time_costs[method.__name__] = []
		for n in range(1, 30):
			time_start = time.time()
			results = method(n)
			time_cost = time.time() - time_start
			time_costs[method.__name__].append(time_cost)
	
	# 三种算法的对比
	plt.figure(figsize = [8, 6])
	for method_name in time_costs.keys():
		plt.plot(time_costs[method_name])
	plt.legend([p[:-9] for p in time_costs.keys()])
	plt.xlabel('number of stairs')
	plt.ylabel('time cost (seconds)')
	plt.grid(True)



