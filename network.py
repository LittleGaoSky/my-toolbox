import Utils
from collections import Counter
class NetworkUtils:
    def __init__(self, continuous_address):
        self.continuous_address = continuous_address

    # 1、一段连续地址192.168.1.1-192.168.1.124 | 192.168.1.1-124
    # 2、已知IP/Subnet_Mask
    # return 网络地址/子网掩码

    def test1(self):
        # 去除空格
        continuous_address = self.continuous_address.replace(' ', '')
        # 去除重复的分隔符
        continuous_address = Utils.filter_char(continuous_address, '-')

        #    相同部分匹配, 计算网络号
        #      part_prv & part_next

        # 2. 一段连续地址
        list_addr = continuous_address.split('-')
        # 判断x.x.x.1-x.x.x.124 or x.x.x.1-124
        addr_prv = list_addr[0]
        addr_next = list_addr[1]
        type_full= self.__type_full_check(addr_prv, addr_next)
        if type_full:
            result = self.__continuous_full(addr_prv, addr_next)
        else:
            result = self.__continuous_half(addr_prv, addr_next)
        return result

    def __continuous_full(self, addr_prv, addr_next):
        # 比较相同的部分
        self.__get_same_part(addr_prv, addr_next)
        return ''

    def __continuous_half(self, addr_prv, addr_next):

        return ''

    # param1: addr_prv
    # param2: addr_next
    # return True: Like to x.x.x.1-x.x.x.124
    # return False: Like to x.x.x.1-124
    def __type_full_check(self, addr_prv, addr_next):
        counter_prv = Counter(addr_prv)
        prv_dot_num = counter_prv['.']
        counter_next = Counter(addr_next)
        next_dot_num = counter_next['.']
        if prv_dot_num == 3 and next_dot_num == 3:
            return True
        elif prv_dot_num == 3 and next_dot_num == 0:
            return False
        else:
            exit('The IP Network is Invalid')
            # Utils.log(str_content)

    def __get_same_part(self, addr_prv, addr_next):
        NSID_prv = []
        NSID_next = []
        list_prv = addr_prv.split('.')
        list_next = addr_next.split('.')
        length = len(list_prv)
        for i in range(length):
            if list_prv[i] == list_next[i]:
                NSID_prv.append(list_prv[i])
            else:
                # 1.1 and 11.124
                h1 = '{:08b}'.format(int(list_prv[i]))
                h2 = '{:08b}'.format(int(list_next[i]))
                NSID_next.append('')
                break
        print(NSID_prv)
def check(high, num):
    res = high + '0'*(8-num)
    return int(res,2)
network = NetworkUtils('192.168.1.1 --192.168.11.124')
res = network.test1()
# print(res)
