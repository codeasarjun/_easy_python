from test_package.module1 import greet # this calling specfic function
from test_package.module2 import multiply


from test_package import module1 # this way we are importing everthing of modulue1

message = module1.greet("Bob") # way 1 to access
print(message)

message = greet("Bob") # way 2 to access the requied funtion only
print(message)

