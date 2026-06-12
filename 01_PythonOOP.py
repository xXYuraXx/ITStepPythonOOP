class Money:
    def __init__(self, int_part=0, float_part=0, sign='$'):
        self.__int_part = 0
        self.__float_part = 0
        self.__sign = '$'
        
        self.int_part = int_part
        self.float_part = float_part
        self.sign = sign
        
    @property
    def int_part(self):
        return self.__int_part
    
    @property
    def float_part(self):
        return self.__float_part
    
    @property
    def sign(self):
        return self.__sign
    
    @int_part.setter
    def int_part(self, value):
        if value < 0:
            value = 0
        
        self.__int_part = value
    
    @float_part.setter
    def float_part(self, value):
        if value < 0:
            value = 0
        
        if value >= 100:
            value = 99
        
        self.__float_part = value
    
    @sign.setter
    def sign(self, value):
        self.__sign = value
    
    def print_sum(self):
        print(f"{self.int_part}.{self.float_part:02d} {self.sign}")

    
    
        
class Product(Money):
    def __init__(self, int_part=0, float_part=0, sign='$'):
        super().__init__(int_part, float_part, sign)
        
    def reduce_price(self, int_part, float_part=0):
        total_reduce_in_float = int_part * 100 + float_part
        total_cur_in_float = self.int_part * 100 + self.float_part
        
        total = total_cur_in_float - total_reduce_in_float
        total = max(total, 0)
        
        total_int = total // 100
        total_float = total % 100
        
        self.int_part = total_int
        self.float_part = total_float
        
        
        


class Circle:
    pi = 3.1415
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    @property
    def len(self):
        return 2 * Circle.pi * self.r
    
    def __eq__(self, other):
        return self.r == other.r
    
    def __gt__(self, other):
        return self.len > other.len
    
    def __lt__(self, other):
        return self.len < other.len
    
    def __le__(self, other):
        return self.len <= other.len
    
    def __ge__(self, other):
        return self.len >= other.len
    
    def __add__(self, value):
        return Circle(self.x, self.y, self.r + value)
        
    def __sub__(self, value):
        return Circle(self.x, self.y, self.r - value)
    
    def __iadd__(self, value):
        self.r += value
        return self
        
    def __isub__(self, value):
        self.r -= value
        return self
        
    def __str__(self):
        return f"x: {self.x}, y: {self.y}, r: {self.r}, len: {self.len:.3f}"


class Airplane:
    def __init__(self, type="None", passengers=0, max_passengers=0):
        self.type = type
        self.passengers = passengers
        self.max_passengers = max_passengers
        
    def __eq__(self, other):
        return other.type == self.type
    
    def __add__(self, value):
        return Airplane(self.type,
                        max(min(self.passengers + value, self.max_passengers), 0),
                        self.max_passengers)
    
    def __sub__(self, value):
        return Airplane(self.type,
                        max(min(self.passengers - value, self.max_passengers), 0),
                        self.max_passengers)

    def __iadd__(self, value):
        self.passengers = max(min(self.passengers + value, self.max_passengers), 0)
        return self
    
    def __isub__(self, value):
        self.passengers = max(min(self.passengers - value, self.max_passengers), 0)
        return self
    
    def __gt__(self, other):
        return self.max_passengers > other.max_passengers
    
    def __lt__(self, other):
        return self.max_passengers < other.max_passengers
    
    def __le__(self, other):
        return self.max_passengers <= other.max_passengers
        
    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers
    
    def __str__(self):
        return  f"type: {self.type}, " \
                f"passengers: {self.passengers}, " \
                f"max_passengers: {self.max_passengers}"
                
                
class Flat:
    def __init__(self, area=0, price=0):
        self.area = area
        self.price = price
        
    def __eq__(self, other : Flat):
        return self.area == other.area
    
    def __ne__(self, other : Flat):
        return self.area != other.area
    
    def __gt__(self, other : Flat):
        return self.price > other.price
    
    def __lt__(self, other : Flat):
        return self.price < other.price
    
    def __le__(self, other : Flat):
        return self.price <= other.price
    
    def __ge__(self, other : Flat):
        return self.price >= other.price
    
    def __str__(self):
        return  f"area: {self.area}, " \
                f"price: {self.price}, "

def main():
    # 1 ==========
    p1 = Product(10, 99)
    p1.print_sum()
    p1.reduce_price(0, 200)
    p1.print_sum()
    p1.reduce_price(2)
    p1.print_sum()
    
    # 2 ==========
    c1 = Circle(2, 5, 5)
    c2 = Circle(2, 5, 10)
    
    print("== Circle 1 ==")
    print(c1)
    print("== Circle 2 ==")
    print(c2)
    
    print(c1 == c2)
    print(c1 < c2)
    
    c2 += 10
    
    print("== Circle 1,2 ==")
    print(c1 + 10, c2, sep='\n')
    
    # 3 ==========
    a1 = Airplane("Fast", 4, 10)
    a2 = Airplane("Slow", 20, 50)
    print(a1, a2, sep='\n')
    print(a1 == a2)
    print(a1 > a2)
    print(a1 + 10)
    a2 += 20
    print(a2)
    
    # 4 ==========
    f1 = Flat(150, 50000)
    f2 = Flat(200, 75000)
    f3 = Flat(150, 100000)
    print(f1, f2, f3, sep='\n')
    print(f1 == f2)
    print(f1 == f3)
    print(f1 <= f3)

if __name__ == "__main__":
    main()