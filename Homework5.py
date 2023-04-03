#import math
def int_h(num):
    if (num - int(num)) > 0:
        num = int(num + 1)
    elif (num - int(num)) < 0:
        num = int(num - 1)
    else:
        num = int(num)
    return num
# Создание родительского класса
class machine(object):
    def __init__(self, perfomance, price, a_detail_price):
        self.perfomance = perfomance #производительность (изделий в час)
        self.price = price #стоимость станка
        self.a_detail_price = a_detail_price #средняя стоимость детали

    def detail_quant(self):
        return  int_h(self.price / (self.a_detail_price * self.perfomance)) #окупаемость при ср. стоимости

    def payback_time(self, detail_fix):
        self.detail_fix = detail_fix
        return int_h(self.price / (self.detail_fix * self.perfomance)) #окупаемость при фикс.стоимости

    def __add__(self, other):
        return self + other

class milling(machine):
    def __init__(self, perfomance, price, a_detail_price, mil_size):
        super().__init__(perfomance, price, a_detail_price)
        self.mil_size = mil_size

    def output(self):
        print("Окупаемость при средней стоимости: {}".format(self.detail_quant()))
        print("Окупаемость при фиксированной стоимости детали: {}".format(self.payback_time(self.detail_fix)))

class CNCmachine(machine):
    def __init__(self, perfomance, price, a_detail_price, axis):
        super().__init__(perfomance, price, a_detail_price)
        self.axis = axis

    def output(self):
        print("Окупаемость при средней стоимости: {}".format(self.detail_quant()))
        print("Окупаемость при фиксированной стоимости детали: {}".format(self.payback_time(self.detail_fix)))

mac_1 = milling(1,20,1,1)
mac_1.detail_fix = 3
mac_1.output()

mac_2 = CNCmachine(1,10,3,6)
mac_2.detail_fix = 1
mac_2.output()