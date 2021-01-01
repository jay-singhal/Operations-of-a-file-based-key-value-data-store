import time
import threading

d={}

def read(key):
	if key not in d:
	    print("ERROR- Given key does not exist in database")
	else:
	    a=d[key]
	    if a[1]!=0:
	        if time.time()<a[1]:
	            value=str(key)+":"+str(a[0])
	            return value
	        else:
	            print(key,"has expired")
	    else:
	        value=str(key)+":"+str(a[0])
	        return value
    		

def delete(key):
    if key not in d:
        print("ERROR- Given key does not exist in database")
    else:
        a=d[key]
        if a[1]!=0:
            if time.time()<a[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print(key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")
	
def modify(key,value):
    a=d[key]
    if a[1]!=0:
        if time.time()<a[1]:
            if key not in d:
                print("ERROR- Given key does not exist in database")
            else:
                l=[]
                l.append(value)
                l.append(a[1])
                d[key]=l
        else:
            print(key,"has expired") #error message5
    else:
        if key not in d:
            print("ERROR- Given key does not exist in database")
        else:
            l=[]
            l.append(value)
            l.append(a[1])
            d[key]=l
			
			
def create(key,value,timeout=0):
    if key in d:
        print("ERROR- key already exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name 32chars
                    d[key]=l
            else:
                print("ERROR- Memory limit exceeded!")
        else:
            print("ERROR- Invalind key name! key contain only alphabets and no special characters or numbers")
			
			
create("s",25)
print(read("s"))
modify("s",26)  # modify s value from 25 to 26
print(read("s"))
create("2312313",25) # ERROR

t1=threading.Thread(target=(create),args=("j",30,10))
t1.start()
t2=threading.Thread(target=(create),args=("s",50))
t2.start()

