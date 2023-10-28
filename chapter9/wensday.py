#  import the entire math module
import math
print(math.floor(2.5))
print(math.ceil(2.5))
print(math.pi)
#  importing only variables and functions rather than an entire
#  module, better efficiency
from math import floor,pi
print(floor(2.5))
#  print(celi(2.5)) it will gives error
print(pi)

#  using the 'as' keyword t create and alias for imports
from math import floor as f
print(f(2.5))

## Using our Module
import wensday_module
print(wensday_module.lenght,wensday_module.width)
print(wensday_module.print_info('tohidul',24))

