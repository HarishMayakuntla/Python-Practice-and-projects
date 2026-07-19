## ==================  unique email collector ============

college_id = set()

while True:
    id = input("Enter id (exit): ")

    if id.lower() == "exit":
        break

    if id in college_id:
        print("id already exists.")
    else:
        college_id.add(id)
        print("Added Successfully!")

print("\nUnique colleage_ids:")
for id in college_id:
    print(id)




# output

Enter id (exit): 5289564
Added Successfully!
Enter id (exit): 5298746
Added Successfully!
Enter id (exit): 52894613
Added Successfully!
Enter id (exit): 5289741
Added Successfully!
Enter id (exit): 52878741
Added Successfully!
Enter id (exit): 25487896
Added Successfully!
Enter id (exit): 2596387
Added Successfully!
Enter id (exit): 527863
Added Successfully!
Enter id (exit): 52987741
Added Successfully!
Enter id (exit): 2576
Added Successfully!
Enter id (exit): 2345678
Added Successfully!
Enter id (exit): 23795
Added Successfully!
Enter id (exit): 25416398
Added Successfully!
Enter id (exit): exit

Unique colleage_ids:
2596387
2345678
23795
52878741
25416398
5298746
52987741
5289564
25487896
52894613
2576
527863
5289741