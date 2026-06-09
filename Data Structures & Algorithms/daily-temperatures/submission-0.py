class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out  = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                out[index] = i - index
                
            stack.append(i)
        
        return out
      
                        

        