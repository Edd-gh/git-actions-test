import looker_sdk

sdk = looker_sdk.init40()  # or init31() for the older v3.1 API
my_user = sdk.me()

print(my_user["first_name"])
