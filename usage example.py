import json

from message import Message

# Create
msg = Message()
msg = Message('{"a":100}',b=2,c="Hello")
print("Message = ", msg)  # json
print(f"messge() method returned type dict {type(msg())}")
# add, update and return dict
print(f"msg(b=200, d=400)= {msg(b=200, d=400)}")

# add and update also with json
jstr = '{"Z":"ok"}'
lst = list(range(10,15))
jstr2 = json.dumps({"chckd":False,"list":lst})

print(f"messge json {str(msg(jstr, jstr2))}")
#############

# delete - remove
msg.rm("b", 'unknown', 'unknown2', "c", "chckd")  # non-existent variable is ignored
msg.rm()
print('del b, c and chckd', msg)

# access to variables
print(f"msg.list[2] = {msg.list[2]}")  # directe
# non-existent variable
print(f"non-existent variable = ",msg.unknown_variable)  # WARNING non-existent variable = None
