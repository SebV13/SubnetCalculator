import os
def main():
  while(1):
    prompt()


def prompt():
  print("please enter ip address: ")
  firstOctet,secondOctet,thirdOctet,fourthOctet=map(int,input().split('.'))
  cidr=int(input("please enter Cidr: /"))
  print(f"you entered {firstOctet} {secondOctet} {thirdOctet} {fourthOctet} and /{cidr}")

  a = translate(firstOctet)
  b = translate(secondOctet)
  c = translate(thirdOctet)
  d = translate(fourthOctet)
  print(f"In binary form: {a}.{b}.{c}.{d}") 
 

  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)

  print("bit mask: " + bin(mask).replace('0b',""))
  foo = bin(mask).replace('0b',"")
  temp = str(foo)
  partedMask=[temp[i:i+8] for i in range(0, len(temp), 8)]
  
  


  countZeros = bin(mask).replace('0b',"").count("0")

  one=eightBitify(int(firstOctet))
  two=eightBitify(int(secondOctet))
  three=eightBitify(int(thirdOctet))
  four=eightBitify(int(fourthOctet))
  octets = [one,two,three,four]

  ans= int(partedMask[0],2) & int(one,2)
  ans2= int(partedMask[1],2) & int(two,2)
  ans3= int(partedMask[2],2) & int(three,2)
  ans4= int(partedMask[3],2) & int(four,2)
  networkAddr=(f"Network address: {ans}.{ans2}.{ans3}.{ans4}")
  firstHost=(f"First Host: {ans}.{ans2}.{ans3}.{ans4+1}")
  print(networkAddr)
  print(firstHost)
  broadcast = [(int(octets[i],2) & int(partedMask[i],2)) | (255^int(partedMask[i],2)) for i in range(4)]
  #print(broadcast)
  print(f"Broadcast address: {broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]}")
  print(f"Last Host: {broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]-1}")


  if(fourthOctet < broadcast[3]-1 and fourthOctet > ans4 + 1):
    print("Valid Host on network")
  else:
    print("Not a valid host")

  hosts = 0
  if(firstOctet < 128):
    print("Class A network")
    zero = cidr - 8
    hosts = abs(2 ** countZeros -2)
    print(f"number of hosts: {hosts}" ) 
  elif(firstOctet < 192):
    print("Class B network")
    zero = cidr - 16
    hosts = abs(2 ** countZeros -2)
    print(f"number of hosts: {hosts}")
  elif(firstOctet < 224):
    print("Class C network")
    zero = cidr - 24
    hosts = abs(2 ** countZeros -2)
    print(f"number of hosts: {hosts}")
  askToContinue()

  
def askToContinue():
  print("Do you want to continue y or n:")
  response=input()
  if(response=='y'):
    os.system('clear')
    main()
  else:
    quit()

def eightBitify(x):
  return bin(x)[2:].zfill(8)

def translate(n):
  return decToBin(n)

def decToBin(octet):
  return bin(octet).replace("0b","")

  
if __name__ == "__main__":
    main()