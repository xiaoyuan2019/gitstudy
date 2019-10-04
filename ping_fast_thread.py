from subprocess import Popen,PIPE
import threading
import queue,sys

class DoRun(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue=queue

	def run(self):
		while not self._queue.empty():
			ip=self._queue.get()
			a=Popen('ping -n 1 '+ip,stdin=PIPE,stdout=PIPE)
			data=str(a.stdout.read())
			# print(data)
			if "TTL" in data:
				print("{} is up".format(ip))


def main():
	threads=[]
	threads_count=64
	queues=queue.Queue()
	# ip=input("pls input ip range:")
	for i in range(1,255):
		queues.put("10.195.249."+str(i))

	for i in range(threads_count):
		print("Do the {} threading".format(i))
		threads.append(DoRun(queues))

	for i in threads:
		i.start()
	for i in threads:
		i.join()

if __name__=="__main__":
	main()

# def pingtest(ip):
	# a=Popen('ping -n 1 '+ip,stdin=PIPE,stdout=PIPE)
	# data=str(a.stdout.read())
	# # print(data)
	# if "TTL" in data:
	# 	print("{} is up".format(ip))
# for i in range(1,255):
# 	ip= '10.195.128.'+str(i)
# 	t=threading.Thread(pingtest,(ip,))
# 	t.start
