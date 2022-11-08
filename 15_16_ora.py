""""
print("Hello")
print('Hello')
a = "Hello"
print(a)
"""
"""
a = ""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""
print(a)
a = "Hello, World!"
print(a[a])
print(a[12])
#a
# b =10
# b
a = "hello world!asdfsdgake"
print(a[len(a)-1])
print("VEGE")
print("az utolso", len(a)-1)


a = "abcdefghijklmnop"

szamlalo = 1
for x in a:
    if szamlalo % 2 == 0:
        print(a[szamlalo-1], end="")
    szamlalo = szamlalo+1 

a = "Hello, World!"

print(len(a))

txt = "The best things in life are freae!"

print("free" in txt) # True

txt = "The best things in life are free!"

if "expensive" not in txt:

  print("No, 'expensive' is NOT present.")

b = "Hello, World!"

print(b[2:5])  # llo
 
b = "Hello, World!"

print(b[:5]) # Hello

b = "Hello, World!"

print(b[1:5]) # Hello

c = "H" +b[1:5]
print(c)

b = "Hello, World!"

print(b[2:]) # llo, World!

a = "Hello, World!"

print(a.upper())


a = "Hello, World!"

nagybetu = a.upper()
print(nagybetu)
 
a = " Hello, World! "
b = a.strip()

print(a.strip()) # returns "Hello, World!"

print(len(b)) 

a = "Hello, Korld!"

print(a.replace("K", "W"))

a = "Hello, World!,2222,3333"

print(a.split(",")) # returns ['Hello', ' World!']
lista = a.split(",")
print(lista[3])
"""
a = "44;341;223;333;"
a.split(",")
lista = a.split(";")
print(lista[3])