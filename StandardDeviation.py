list1=[]
list2=[]
total_Mean_Value=0
while len(list1)==0:
    item=input("Enter a value, or enter value<0 to stop:").split(",")
    for elements in item:    
        if elements=='':
            print("Enter a valid value")
        else:
            elements=float(elements)
            if elements>-1:
                list1.append(elements)
            else:
                print("Invalid Value")
                break       

if len(list1)!=0:
    count=len(list1)
    total=sum(list1)
    average=total/count
    
    for value in list1:
        new_value=value-average
        list2.append(new_value)
    count=len(list2)
    
    for div in list2:
        m=(div)**2
        total_Mean_Value+=m
    
    count-=1
    SD=total_Mean_Value/count
    print(f"The standard deviation for the data is: {(SD)**0.5:1.3}")
    print("The average for the data is: ",average)


    
    
