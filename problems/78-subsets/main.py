from copy import deepcopy


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output: list[list[int]] = [[]]
        for n in nums:
            next_output = deepcopy(output)
            for out in output:
                next_output.append(out + [n])
            output = next_output
        return output
