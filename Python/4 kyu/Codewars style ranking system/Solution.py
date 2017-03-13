class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, num):
        assert(num <= 8 and num >= -8 and num != 0)
        
        if self.rank == 8:
            None
        else:
            ranks = []
            numPosition = 0
            rankPosition = 0
            
            for ranks_i in range(-8,9):
                if not ranks_i == 0:
                    ranks.append(ranks_i)
    
            for ranks_i in range(0, len(ranks)):
                if ranks[ranks_i] == num:
                    numPosition = ranks_i
                if ranks[ranks_i] == self.rank:
                    rankPosition = ranks_i
                    
           if(numPosition > rankPosition):
                difference = numPosition-rankPosition
                self.progress += 10 * difference**2
            elif(numPosition < rankPosition):
                if(numPosition == rankPosition-1):
                    self.progress += 1
            else:
                self.progress += 3
    
            leftOver = 0
            while(self.progress > 100):
                leftOver = self.progress - 100
                self.progress -= 100
                self.progress = leftOver
                if(self.rank == -1):
                    self.rank += 2
                else:
                    self.rank += 1
                if(self.rank == 8):
                    self.progress = 0
                    break
