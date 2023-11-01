import person_pb2  


person = person_pb2.Person()


with open("/home/nejc/VAJE/VAJE-3/DATA/POMOC/person_updated.pb", "rb") as f:
    person.ParseFromString(f.read())


person.age= 31
person.married = False

with open("/home/nejc/VAJE/VAJE-3/DATA/POMOC/person_updatedUpdate.pb", "wb") as f:
    f.write(person.SerializeToString())

# print
print(person)