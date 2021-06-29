from nordvpn_switcher import initialize_VPN,rotate_VPN
import time

instructions = initialize_VPN(area_input=['Germany,France,Netherlands,Sweden,Switzerland,Denmark,Italy,Norway,Spain,Belgium,Poland,Ireland,Czech Republic,Austria,Finland,Portugal,Ukraine,Serbia,Hungary,Greece,Latvia,Luxembourg,Romania,Bulgaria,Estonia,Slovakia,Iceland,Albania,Cyprus,Croatia,Slovenia,Bosnia and Herzegovina,Georgia,Moldova,North Macedonia,Canada,Brazil,Argentina,Mexico,Chile,Costa Rica,Australia,South Africa,India,United Arab Emirates,Israel,Turkey,Australia,Singapore,Taiwan,Japan,Hong Kong,New Zealand,Indonesia,Malaysia,Vietnam,South Korea,Thailand'])

rotate_VPN(instructions)