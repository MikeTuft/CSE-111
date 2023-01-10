import math
##########Tire Volume#########
### Michael Tuft###
##1/6/2023##
mt_width=float(input('What is the width of the tire? (millimeters)'))
mt_aspratio=float(input('What is the Aspect ratio of the tire?'))
mt_diameter=float(input('What is the diameter of the Wheel? (inches)'))
mt_radius= 25.4*mt_diameter/2
mt_hugt=mt_aspratio/100*mt_width
mt_odiameter=25.4*mt_diameter + mt_hugt
mt_oradius=mt_odiameter/2

mt_wvolume=math.pi* mt_radius**2*mt_hugt
mt_ovolume=math.pi* mt_oradius**2*mt_hugt

mt_tvolume= mt_ovolume - mt_wvolume
volume= mt_tvolume/10**10
print('the aproximate volume is %.2f liters' %(volume))



# mt_volume= (math.pi*(mt_width**2)*mt_aspratio(mt_width*mt_aspratio+2,540*mt_diameter))/10000000000
# print(f'The aproximate volume is {mt_volume}')