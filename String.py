################################################################
## Consider the below application which Demonstrate concept of String
################################################################

print("------------Akshada Sayaji Ghadge--------------");
print("------Demonstration of STRING--------");

name = "JaySadguru";
newName = "Marvellous";

print(name);
print(type(name));

print(newName);
print(type(name));

# as string is array of character we can access using the subscript operator

print(name[0]);
print(newName[7]);
# print(name[10]); // index out of range

# negative index access element from right to left
print(name[-1]);
print(newName[-6]);

# we can also print character in range
print(name[0:3]);
print(newName[2:6]);
print(name[2:]);
print(newName[:5]); # 5 is exclusive 

# string in python are immutable
# newName[0] = 'm'; //Error : string obj does not support item assignment

# we can use len function to calculate length of String
print(len(name));

# strip method removes whitespaces from beginning and ending
className = "  Marvellous Infosystem  Pune  ";
print(className.strip());

# By using split we tokenize the String
Languages = "C,C++,Java,Python,PHP,C#,Angular";
print(Languages.split(","));
