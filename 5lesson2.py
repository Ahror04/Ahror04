# import math
# # x=15
# # r=(math.sqrt(x))       #ildizini olish
# # print(round(r))        #yaxlitlash
# # print(math.ceil(r))    #katta tomonga yaxlitlaydi
# # print(math.floor(r))   #kichik tomonga yaxlitlaydi
# # print(divmod(12,5))    #bolinmasi va qoldigini ham olib beradi
# # print(pow(5,5))        #darajaga oshiradi



# # #KASR SONLAR

# # e=10_000_000
# # d=0,1 == .1
from decimal import Decimal
# # x=Decimal('0.1')
# # y=Decimal('0.1')
# # z=Decimal('0.1')
# # print(x+y+z==Decimal('0.3'))

# # price=10.25
# # minutes,secund=5,34
# # secund=(minutes*60+secund)/60
# # min=math.ceil(secund) 
# # summa=min*price
# # print(summa)


# # print(round(3.1479487894, 2))

q=Decimal('0.001')
x=Decimal('3.144541245')
s=x.quantize(q)
print(s)

# from PIL import Image





   