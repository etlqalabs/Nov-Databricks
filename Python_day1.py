# print("This is my day 1")

age = 10
'''
print(age)

if age>=18:
    print("elligble for voting")
else:
    print("not elligble for voting")

print("program completed..")

print(age)
print(type(age))

name = "ETL QA Labs"
print(name)
print(type(name))

weight = 48.9
print(weight)
print(type(weight))


nameofyoutubechannel = "ETL QA Labs"
name_of_youtube_channel = "ETL QA Labs"

NameOfYoutubeChannel = "ETL QA Labs"

nameOfYoutubeChannel = "ETL QA Labs"
print(name)
print(type(name))

marital_status = True
print(marital_status)

weight_of_person = 50.8
weight_int = int(weight_of_person)
print(weight_int)



num1 = 10
num2 = 20
sum =  num1 +num2
print("sum : ",sum)

print(f"num1 is : {num1} and dataype is {type(num2)} and num4 is {num2} and dataype is {type(num2)} and sum is {sum}")


num3 = '10'
num4 = "20"
sum =  int(num3) +int(num4)
print("sum : ",sum)
print(f"num3 is : {num3} and dataype is {type(num3)} and num4 is {num4} and dataype is {type(num4)} and sum is {sum}")


# user input

num1 = input("enter num 1")
num2 = input("enter num 2")
print(int(num1)+int(num2))

num1 = int(input("enter num 1"))
num2 = int(input("enter num 2"))
print(num1+num2)



source_count = 1000
target_count = 980

#source_count = target_count

print(source_count)
print(target_count)

status = source_count == target_count
print(status)


duration = 70

if duration <= 30:
    print("SLA Met")
elif duration <= 45:
    print("SLA Warning")
elif duration <= 60:
    print("SLA nearing break")
else:
    print("SLA Breached")

has_file = True
row_count = 0

if has_file and row_count > 0:
    print("Ready for validation")
else:
    print("Check file or data availability")

if has_file or row_count > 0:
    print("Ready for validation")
else:
    print("Check file or data availability")

if has_file and not row_count > 0:
    print("Ready for validation")
else:
    print("Check file or data availability")



# range() -> range(start,end,step)
# range(5) => range(0,5,1)
#print(range(5))

#for num in range(5):
 #   print(num)

#for num in range(1,5,1):
 #   print(num)

for num in range(1,10,2):
    print(num)

for num in range(2,10,2):
    print(num)
    


# while loop for prting even number from 2 to 8
start = 2
end = 8
while start <=end:
    print(start)
    start = start +2



# print all the multiple of 5 starting from 5 to 100 ( 5,10,15,20......)

for num in range(5,30,1):
    if num%5 == 0:
        print(num)

for num in range(1,6,1):
    if num== 3:
        continue
    print(num)

'''

for num in range(1,6,1):
    if num== 3:
        break
    print(num)

for num in range(1,6,1):
    pass

