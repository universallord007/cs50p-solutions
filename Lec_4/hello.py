import sys

# if len(sys.argv) < 2:
#     print("Please provide a name as an argument.")
# elif len(sys.argv) > 2:
#     print("Please provide only one name as an argument.")
# else :
#     print("Hello my name is",sys.argv[1])


# if len(sys.argv) < 2:
#     sys.exit("Please provide a name as an argument.")
# elif len(sys.argv) > 2:
#     sys.exit("Please provide only one name as an argument.")

# print("Hello my name is",sys.argv[1])



if len(sys.argv) < 2:
    sys.exit("Please provide a name as an argument.")


for arg in sys.argv[1:] :
    print("Hello my name is",arg)




