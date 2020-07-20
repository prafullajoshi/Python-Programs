import ecommerce.sales          # METHOD 1
from ecommerce import sales     # METHOD 2
from ecommerce.sales import calc_shipping, calc_tax  # METHOD 3


# METHOD 1 calling
calc_shipping()
calc_tax()

# METHOD 2 calling

sales.calc_shipping()
sales.calc_tax()

# METHOD 3 calling

ecommerce.sales.calc_shipping()
ecommerce.sales.calc_tax()
