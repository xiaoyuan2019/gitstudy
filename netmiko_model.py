from netmiko import ConnectHandler
import threading
import queue


class Get_arp1(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            ip = self._queue.get()
            cisco_sw = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': 'zhangsan',
                'password': '123456',
            }
            sw_connect = ConnectHandler(**cisco_sw)
            # net_connect = ConnectHandler(device_type='cisco_ios',host='IP地址',username='用户名',password='密码')
            result = sw_connect.send_command("show ip arp | ex Incomplete")
            path = "c:/iplist/"+ip+".txt"
            with open(path, "a+") as f1:
                f1.write(result)
            print("the ip {} is done.".format(ip))


if __name__ == "__main__":
    ip_list = ["10.195.249.1",
               "10.195.32.1",
               "10.195.64.1",
               "10.195.160.1",
               "10.195.168.1",
               "10.195.170.1",
               "10.195.180.1",
               "10.195.68.1"]
    threads = []
    queues = queue.Queue()
    for i in ip_list:
        queues.put(i)

    for i in range(len(ip_list)):
        # print("starting the {} ".format(i))
        threads.append(Get_arp1(queues))
    # print(threads)

    for i in threads:
        i.start()

    for i in threads:
        i.join()
