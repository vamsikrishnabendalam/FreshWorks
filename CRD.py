import threading 
from threading import*
import time
dic={} #'dic' is the dictionary in which we store date

# create operation
def create(key,value,timeout=0):
    if key in dic:
        print(" this key exists") 
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    dic[key]=l
            else:
                print("Memory limit overflowed")
        else:
            print("Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

# read operation
            
def read(key):
    if key not in dic:
        print(" given key does not exist in database.")
        print(" Please enter a valid key")
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("Living time ",key,"has been expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri

# delete operation

def delete(key):
    if key not in dic:
        print(" given key does not exist in database.")
        print(" Please enter a valid key")
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del dic[key]
                print("key is successfully deleted")
            else:
                print("Living time ",key,"has been expired")
        else:
            del dic[key]
            print("key is successfully deleted")
