class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #初始化輸出的答案陣列，全部填 1
        res = [1] * n
        
        #步驟 1：計算前綴乘積（左邊所有數字的乘積）
        #prefix_product 用來記錄目前位置左邊所有人的累積乘積
        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]#更新前綴乘積，留給下一個數字用
            
        # 步驟 2：從右往左一邊計算後綴乘積（右邊），一邊直接乘進 res 陣列裡
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_product #將目前的左積直接乘以剛剛累積的右積
            suffix_product *= nums[i] #更新後綴乘積，留給左邊的下一個數字用
            
        return res