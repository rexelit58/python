#we can import all available functions from a model
# or we can  import the required function by  specifying it
# Both approaches function calling syntax get differs
# import converters
# converters.lbs_to_kg(70)

import converters
from converters import kg_to_lbs
kg_to_lbs(1000)
print(kg_to_lbs(1000))