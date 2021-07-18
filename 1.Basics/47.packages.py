# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
#importing a function from a specific package and module
from ecommerce.shipping import calc_shipping
calc_shipping();

#importing multiple functions from a specific package and module
from ecommerce.shipping import calc_shipping,calc_tax
calc_shipping();

#importing specific  module from a package
from ecommerce import shipping
shipping.calc_shipping();