import requests
validaror_url = "https://validator.w3.org/nu/"
ip_address = "https://www.zhihu.com/question/24237220/"
params = { "doc": ip_address, "out": "json"}

response = requests.get(validaror_url,params=params)

# Use "type:error" to locate errors
error_key = "\"type\":\"error\""

# Use "subType:warning" to locate warnings
warning_key = "\"subType\":\"warning\""

# .text contains entire content of checking result
print(response.text.count(error_key))
print(response.text.count(warning_key))