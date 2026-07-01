class Solution:
    def compress(self, chars: List[str]) -> int:
        #write紀錄寫到哪 anchor紀錄當前字元的起點
        write = 0
        anchor = 0
        
        #read一個一個往右走
        for read in range(len(chars)):
            #condition1:已經走到陣列最後一個字了
            #condition2:下一個字跟現在這個字長得不一樣
            if read == len(chars) - 1 or chars[read] != chars[read + 1]:
                
                #動作一：先把這個字元寫進 write 的位置
                chars[write] = chars[anchor]
                write += 1
                
                #動作二：計算這群字元出現了幾次
                count = read - anchor + 1
                
                #動作三：如果出現超過 1 次，要把數字也寫進去
                if count > 1:
                    #若數字很大(ex:12)，要拆成'1'和'2'寫入
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                
                #動作四：這群結束了，把下一個群體的定錨點移到下一格
                anchor = read + 1
                
        #最後write停下的位置，剛好就是新陣列的長度
        return write