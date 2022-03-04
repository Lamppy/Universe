"""Графики"""
from matplotlib import pyplot as pp 
MODEL_G=9.81
MODEL_DT=0.1
class Body:
    """Создали класс тела"""
    def __init__(self,x_coord,y_coord,v_x,v_y):
        """
        Создать тело.
        Пареметры:
        ----------
        x_coord: float
            горизонтальная координата
        y_coord: float
            вертикальная координата
        v_x: float
            горизонтальная скорость
        v_y: float
            вертикальная скорость
        """
        self.x_coord=x_coord
        self.y_coord=y_coord
        self.v_x=v_x
        self.v_y=v_y
        self.trajectory_x=[]
        self.trajectory_y=[]
    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x_coord)
        self.trajectory_y.append(self.y_coord)
        self.x_coord+=self.v_x * MODEL_DT
        self.y_coord+=self.v_y * MODEL_DT
        self.v_y-=MODEL_G * MODEL_DT
class Rocket(Body):
    """Создали класс объекта"""
    def __init__(self,x_coord,y_coord,m_body=250,m_fuel=1000,d_m=100,vel_of_gas=400):
        """
        Создать ракету с параметрами.
        """
        super().__init__(x_coord,y_coord,10,10) # Вызовем конструктор предка — тела
        self.m_fuel=m_fuel
        self.m_body=m_body
        self.d_m=d_m
        self.vel_of_gas=vel_of_gas
    def advance(self):
        """
        Выполним шаг математической модели ракеты, запоминая его координаты
        """
        super().advance() # вызовем метод предка — тела, т.к. и он для ракеты актуален.
        if self.m_fuel>=self.d_m*MODEL_DT:
            self.m_fuel-=self.d_m * MODEL_DT # вычтем массу сгоревшего топлива
            d_v=(self.m_fuel+self.m_body)*MODEL_G*MODEL_DT+(self.d_m*self.vel_of_gas)/(self.m_body+self.m_fuel)
            d_vx=d_v*(self.x_coord/(self.x_coord**2 + self.y_coord**2)) 
            d_vy=d_v * (self.y_coord/(self.x_coord**2 + self.y_coord**2)) 
            self.v_x+=d_vx
            self.v_y+=d_vy
        elif(self.m_fuel>0 and self.m_fuel<self.d_m*MODEL_DT):
            self.m_fuel=0
            d_v=(self.d_m * self.vel_of_gas)/(self.m_body + self.m_fuel) 
            d_vx=d_v*(self.x_coord/(self.x_coord**2 + self.y_coord**2)) 
            d_vy=d_v*(self.y_coord/(self.x_coord**2 + self.y_coord**2))
            self.v_x += d_vx
            self.v_y += d_vy
rocket_initial=Rocket(0,0,float(input("Body mass")),float(input("Fuel mass")),
 float(input("Fuel mass per dt")),float(input("Velocity of exhaust")))
rocket_initial.advance() 
while rocket_initial.y_coord>0: 
    print(rocket_initial.m_fuel)
    rocket_initial.advance()
pp.plot(rocket_initial.trajectory_x, rocket_initial.trajectory_y)
pp.show()
print("Наглядный график движения произвольной ракеты")
rocket_arbitrary=Rocket(0, 0)
rocket_arbitrary.advance() 
while rocket_arbitrary.y_coord>0:
    rocket_arbitrary.advance()
pp.plot(rocket_arbitrary.trajectory_x, rocket_arbitrary.trajectory_y) 
pp.show() 
