###########Team Activity#########
###Michael Tuft###
##1/9/2023##
from datetime import datetime
Mt_current_date_and_time= datetime.now()
MT_Dayofweek = Mt_current_date_and_time.weekday()
Mt_discountratio=0
print(MT_Dayofweek)
if MT_Dayofweek == 1 :
    Mt_discountratio =0.1
elif MT_Dayofweek ==2:
        Mt_discountratio =0.1
Mt_subt= float(input('Please enter the subtotal amount '))
Mt_dicount= Mt_subt*Mt_discountratio
Mt_salestax= (Mt_subt - Mt_dicount)*.06
Mt_total=Mt_subt+Mt_salestax-Mt_dicount
print('----------------')
if MT_Dayofweek == 1:
    print(f'That dicount total is {Mt_dicount:.2f}')
elif MT_Dayofweek == 2:
    print(f'That dicount total is {Mt_dicount:.2f}')
print(f' The sales tax total: {Mt_salestax:.2f}$')
print(f' The total is {Mt_total:.2f}$')
    