from address import Address
from mailing import Mailing

to_address_01 = Address('410008', 'Saratov', 'Железнодорожная', '105', '21')
from_address_01 = Address('101000', 'Moscow', 'Шкулева', '123', '3')
cost = 1370
track = 'E25347DB'

track_01 = Mailing(to_address_01, from_address_01, 1370, 'E25347DB')

print(track_01)
