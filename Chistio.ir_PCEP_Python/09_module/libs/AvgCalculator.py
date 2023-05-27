class AvgCalculator:
    x1_c = 4
    x2_c = 3
    x3_c = 2
    
    def calculate(self, x1, x2, x3):
        sum = (x1 * self.x1_c) + (x2 * self.x2_c) + (x3 * self.x3_c)
        avg = sum / (self.x1_c + self.x2_c + self.x3_c)
        return avg