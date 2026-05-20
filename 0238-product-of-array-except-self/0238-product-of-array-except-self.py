class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #初始化輸出的答案陣列 全部填 1
        res = [1] * n
        
        #計算前綴乘積（左邊數字乘積）
        #prefix_product用來記錄目前位置左邊所有的累積乘積
        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]#更新前綴乘積 留給下一個數字用
            
        #從右往左一邊計算後綴乘積（右邊） 一邊直接乘進res陣列裡
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_product #將目前的左積直接乘以剛剛累積的右積
            suffix_product *= nums[i] #更新後綴乘積 留給左邊的下一個數字用
            
        return res


        #for迴圈邏輯: 先把目前左邊累積的成果（prefix_product）送給 res[i]，送完之後，再把現在的 nums[i] 乘進去，留給下一個人用。
        
        #當 i = 0 (數字是 2)：res[0] = prefix_product $\rightarrow$ 此時 prefix_product 是 1（因為 2 的左邊沒有任何人，所以是 1）。此時 res = [1, 1, 1, 1]。更新留給下一個人的：prefix_product = 1 * 2 = 2。
        #當 i = 1 (數字是 3)：res[1] = prefix_product $\rightarrow$ 把剛才算好左邊的 2 送給它。此時 res = [1, 2, 1, 1]。更新留給下一個人的：prefix_product = 2 * 3 = 6。