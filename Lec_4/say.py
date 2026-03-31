# import cowsay
# import sys

# if len(sys.argv) == 2 :
#     cowsay.trex("Hello "+ sys.argv[1])



# Now we will import our own module 


import sys 
from sayings import hello 

if len(sys.argv) == 2 :
    hello(sys.argv[1])