#%%
import time

class RacingCar:
    carName = ''
    
    def __init__(self,name):
        self.carName = name
    
    def runCar(self):
        for _ in range(0, 3):
            carStr = self.carName + '~~달립니다.\n'
            print(carStr,end= '')
            time.sleep(0.1)
        
car1 = RacingCar('@자동차1')
car2 = RacingCar('%자동차2')
car3 = RacingCar('*자동차3*')

car1.runCar()
car2.runCar()
car3.runCar()

print('-------'*10)

# %%
import threading
import time

class RacingCar:
    carName = ''
    def __init__(self,name):
        self.carName = name
    
    def runCar(self):
        for _ in range(0,3):
            carStr = self.carName + '~~달립니다.\n'
            print(carStr,end= '')
            time.sleep(0.1)

car1 = RacingCar('@자동차1')
car2 = RacingCar('%자동차2')
car3 = RacingCar('*자동차3*')

th1 = threading.Thread(target=car1.runCar)
th2 = threading.Thread(target=car2.runCar)
th3 = threading.Thread(target=car3.runCar)

th1.start()  # 스레드를 시작한다.
th2.start()
th3.start()

th1.join()   # 모든 스레드가 끝날 때까지 기다린다.
th2.join()
th3.join()

#%%
# mulit - processing
import multiprocessing
import time

class RacingCar:
    carName = ''
    def __init__(self,name):
        self.carName = name
    
    def runCar(self):
        for _ in range(0, 3):
            carStr = self.carName + '~~달립니다.\n'
            print(carStr,end= '')
            time.sleep(0.1)

if __name__== "__main__":
    car1 = RacingCar('@자동차1')
    car2 = RacingCar('*자동차2')
    car3 = RacingCar('&자동차3')

    mp1 = multiprocessing.Process(target = car1.runCar)
    mp2 = multiprocessing.Process(target = car2.runCar)
    mp3 = multiprocessing.Process(target = car3.runCar)

    mp1.start()
    mp2.start()
    mp3.start()

    mp1.join()
    mp2.join()
    mp3.join()

    print('----'*10)

# %%
import time
import threading
class Calc:
    data =[x for x in range(10000)]
    def __init__(self,start,finish):
        self.start = start
        self.finish = finish
        self.sum = 0

    def runCalcSum(self):
        self.sum = 0
        print(f'sum range = {self.start}~{self.finish} start !!!\n')
        for i in range(self.start,self.finish):
            self.sum += self.data[i]
        print(f'sum range = {self.start}~{self.finish} = {self.sum} finish !!!\n')
        time.sleep(0.1)

calc_1 = Calc(0,1000)
calc_2 = Calc(1000,2000)
calc_3 = Calc(2000,3000)
calc_4 = Calc(3000,4000)
calc_5 = Calc(4000,5000)

start_time = time.time()
calc_1.runCalcSum()
calc_2.runCalcSum()
calc_3.runCalcSum()
calc_4.runCalcSum()
calc_5.runCalcSum()

end_time = time.time()


print('-------'*10)

# %%
