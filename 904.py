class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        cur_a = None
        cur_b = None
        a_count = 0
        b_count = 0
        ans = 0
        while right < len(fruits):
            if cur_a == fruits[right]:
                a_count += 1
            elif cur_b == fruits[right]:
                b_count += 1
            else:
                if cur_a == None:
                    a_count = 1
                    cur_a = fruits[right]
                elif cur_b == None:
                    b_count = 1
                    cur_b = fruits[right]
                else:
                    while left < right:
                        if cur_a == fruits[left]:
                            a_count -= 1
                            if a_count == 0:
                                cur_a = fruits[right]
                                a_count = 1
                                left += 1
                                break
                        else:
                            b_count -= 1
                            if b_count == 0:
                                cur_b = fruits[right]
                                b_count = 1
                                left += 1
                                break
                        left += 1
            ans = max(ans, right - left + 1)
            print(left, right, cur_a, cur_b)
            right += 1
        return ans