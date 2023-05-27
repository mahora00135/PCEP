class calculat:
    i = 0
    sum = 0
    count = 0
    def mean(self):
        while self.i != '':
            self.i = input('Please enter a number (left blank to calculate mean):')
            if self.i == '':
                continue
            self.i = int(self.i)
            self.sum = self.sum +self.i
            self.count = self.count + 1 

        print(self.sum / self.count)



calculat1 = calculat()
calculat1.mean()
