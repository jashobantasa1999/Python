# g) create a list using names of 10 cities and pincodes. Combine 
# them all to convert it into string using join with delimiter “:”. Modify the names of 
# cities by adding state-cities in the string. Finally split it to have the information in 
# list in the format state-city-pincode.

city =[]
pin =[]

for i in range (3):
    city.append(input("enter 3 cities "))
    pin.append(input("enter 3 pin "))
cp=[]
for i in list(range(len(city))):
    s=city[i]+":"+pin[i]
    cp.append(s)
print(cp)
state=[]
for i in range(3):
    state.append(input("Enter state name:-"))
scp=[]
for i in list(range(3)):
    x=state[i]+"-"+city[i]+"-"+pin[i]
    scp.append(x)
print(scp)