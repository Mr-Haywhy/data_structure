def bubble_sort(list_a):
    exchanges = True
    i = len(list_a)-1
    while i > 0 and exchanges:
        exchanges = False
        for j in range(i):
            if list_a[j]>list_a[j+1]:
                exchanges = True
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                #You print the contents of the array after every swap
                # print("After pass " + str(i) + ", inner loop "+ str(j) + ": " + str(list_a)) 
        i -= 1

#The following code is only to test the Bubble Sort, so nothing has to be changed here    
list_a = [70, 60, 50, 40, 30, 20, 10]
bubble_sort(list_a)
print(list_a)

# …or create a new repository on the command line
# echo "# data_structure" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Mr-Haywhy/data_structure.git
# git push -u origin main

# …or push an existing repository from the command line
# git remote add origin https://github.com/Mr-Haywhy/data_structure.git
# git branch -M main
# git push -u origin main