
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict["brand"])
print()

con = {
    1 : "One",
    2 : "Two",
    "Three" : 3,
    "no" : 0,
    "jan" : "January",
    "feb" : "February"
 }

print(con.get("jan"))
print(con.get("ja"))
print(con.get("ja" , "not found"))
print(con.get(1))
