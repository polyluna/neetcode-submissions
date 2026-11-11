class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0]*(len(cost)+1)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        for i in range(2, len(cost)+1):
            current_cost = cost[i] if i < len(cost) else 0
            min_cost[i] = current_cost + min(min_cost[i-1], min_cost[i-2])
        return min_cost[(len(cost))]