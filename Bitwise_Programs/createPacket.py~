#Write a program to accept following information from user-CRC, length, data and flag where
#	CRC= 5 bits
#	length = 8bits

def createPacket(crc,length,data,flag):
	packet = 0
	crc = crc & ((1<<5)-1)
	packet = crc
	
	packet = packet << 8
	
	length = length & ((1<<8)-1)
	packet =packet | length
	
	packet = packet << 18
	
	data = data & ((1<<18)-1)
	packet = packet | data
	
	packet = packet << 1
	
	flag = flag & 1
	packet = packet | flag
	print("Packet created successfully.")
	return packet
	
def dePacketize(packet):
	flag = packet & 1
	packet = packet >> 1
	
	data = packet & ((1<<18)-1)
	packet = packet >> 18
	
	length = packet & ((1<<8)-1)
	packet = packet >> 8
	
	crc = packet & ((1<<5)-1)
	
	return crc,length,data,flag	
		
def main():
	crc=input("Enter CRC value :")
	length=input("Enter length :")
	data=input("Enter data :")
	flag=input("Enter flag :")
	packet=createPacket(crc,length,data,flag)
	print(packet)
	print("After depacketizing")
	crc,length,data,flag=dePacketize(packet)
	print(crc)
	print(length)
	print(data)
	print(flag)
if __name__=="__main__":
	main()
