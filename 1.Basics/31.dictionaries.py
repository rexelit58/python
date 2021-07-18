#storing the values in key value pair
customer={
    "name":"John smith",
    "is_verified":True
}
print(customer["name"])
#instead of using [] brackets to get the value we can use get method
#get method won't give any error if the key not exists.but [] bracket will give
print(customer.get("name"))#o/p:John smith
print(customer.get("abc"))#o/p:None
print(customer.get("abc","default value"))#o/p:default value
#overring the value
customer["name"]="kavi arasan"
#adding the new key value paid
customer["age"]=26
print(customer)

