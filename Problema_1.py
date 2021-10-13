# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:09:33 2021

@author: ssala
"""
from gekko import GEKKO

m = GEKKO(remote=True)

### Definir variables
x1 = m.Var(value=1000, lb=0, ub=2000)
x2 = m.Var(value=8000,lb=0,ub=16000)
x3 = m.Var(value=60,lb=0,ub=120)
x4 = m.Var(value=3000,lb=0,ub=5000)
x5 = m.Var(value=1000,lb=0,ub=2000)
x6 = m.Var(value=89,lb=85,ub=93)
x7 = m.Var(value=92,lb=90,ub=95)
x8 = m.Var(value=8,lb=3,ub=12)
x9 = m.Var(value=2.5,lb=0.01,ub=4)
x10 = m.Var(value=150,lb=142,ub=162)

### Definir par.
c1 = m.Param(0.063)
c2 = m.Param(5.04)
c3 = m.Param(0.035)
c4 = m.Param(10.0)
c5 = m.Param(3.36)

m.Equations([x4 == x1*(1.12+0.1317*x8-0.0067*x8**2), \
             x5 == 1.22*x4 - x1, \
             x6 == 98000*x3/(x4*x9 + 1000*x3), \
             x7 == 85.88 + 1.098*x8 - 0.04*x8**2 + 0.325*(x6-88.8), \
             x9 == 35.8 - 0.222*x10, \
             x10 == -133.0 + 3.0*x7, \
             x8 == (x5 + x2)/x1])

m.Maximize(c1*x4*x7 - c2*x1 - c3*x2 - c4*x3 - c5*x5)
m.options.IMODE = 3
m.options.SOLVER = 3 # 3 IPOPT
m.solve()

print('Solver: ', m.options.SOLVER)
print('Alimentación oleofina: ',x1.value)
print('Reciclo de isobutano: ',x2.value)
print('Ratio de adición de ácido: ',x3.value)
print('Rendimiento del alquilato: ',x4.value)
print('Isobutano fresco: ',x5.value)
print('Pureza del ácido: ',x6.value)
print('Número de octano: ',x7.value)
print('Relación externa de isobutano a oleofina: ',x8.value)
print('Factor de dilución del ácido: ',x9.value)
print('F4 performance number: ',x10.value)
















