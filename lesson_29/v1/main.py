# 导入 SeatBooking 类
from seat_booking import SeatBooking
# 导入 infos 列表
from infos import infos
from random import choice

# 从 infos 列表中取出任意一部电影的座位表
seats_list = choice(infos)['seats']

# 实例化 SeatBooking 类
booking = SeatBooking()
# 打印所有座位的预订信息
booking.check_bookings(seats_list)
# 按用户输入的座位号预订座位
booking.book_seat(seats_list)