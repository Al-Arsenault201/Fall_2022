def add_to_list(l):
    print(id(l))
    for i in range(len(l)):
       l[i] += 10
    return

if __name__ == "__main__":
   my_list = [1,2,3,4,5]
   print(id(my_list))
   add_to_list(my_list)
   print(my_list)