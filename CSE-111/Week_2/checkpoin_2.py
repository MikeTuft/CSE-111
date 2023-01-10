#################
#Check point 2
#michael Tuft
#1/9/2023

MT_item= float(input('how many items?'))
MT_perbx=float(input('How many items per box ?'))
MT_bxnded=round(MT_item/MT_perbx)
print(f' For {round(MT_item)} Item(S), with {round(MT_perbx)} per box, you will need atleast, {MT_bxnded} Boxes.')