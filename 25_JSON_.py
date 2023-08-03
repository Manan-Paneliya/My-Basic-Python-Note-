import json

## JSON Formate  --  in string
#  "{'URL':'www.wscubetect.com','name':'Wscubetect'}"

#### CONVERT dictionary to JSON ####
blog = {'URL':'www.wscubetect.com','name':'Wscubetect'}
print("blog is ",type(blog))
to_json = json.dumps(blog)   # convert dictionary(blog) to json
print(to_json)
print("to_json is ",type(to_json))

#### CONVERT jSON to dictionary ####
j = '{"class":"Python","fees":"16000","duration":"3 Months"}'
print("j is",type(j))
to_dict = json.loads(j)    # it converts json (string formate) Formate to Dictionary
print(to_dict)
print("to_dict is ",type(to_dict))