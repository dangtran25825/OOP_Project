class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, *args):
        # 1. Hàm xây dựng mặc định: d1(8, 5) và d2(1, 0)
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        
        # 2. Hàm xây dựng truyền vào 2 đối tượng Point
        elif len(args) == 2 and isinstance(args[0], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]
        
        # 3. Hàm xây dựng truyền vào 4 số nguyên (x1, y1, x2, y2)
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
            
        # 4. Hàm xây dựng sao chép sâu (Deep Copy)
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            mau = args[0]
            self.__d1 = Point(mau.get_d1().x, mau.get_d1().y)
            self.__d2 = Point(mau.get_d2().x, mau.get_d2().y)

    def get_d1(self): return self.__d1
    def get_d2(self): return self.__d2