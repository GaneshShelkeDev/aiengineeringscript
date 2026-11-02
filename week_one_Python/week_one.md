1. Types and numbers

Python is dynamically typed (types are checked at runtime) but strongly typed (no silent coercion). "5" + 1 is "51" in JS and 6 in PHP; in Python it raises TypeError. You convert explicitly: int("5") + 1.


type(5)        # <class 'int'>   -- ints are unlimited size, no overflow
type(5.0)      # <class 'float'>
7 / 2          # 3.5  (/ always returns float)
7 // 2         # 3    (floor division)
7 % 2          # 1
0.1 + 0.2      # 0.30000000000000004 -- same as JS

from decimal import Decimal
Decimal("0.1") + Decimal("0.2")   # Decimal('0.3') -- use for money

Senior habit: never use float for money. Use Decimal (built from strings, not floats) or store integer paise/cents. You will use this in the S3 CLI.


2. Strings
Strings are immutable sequences. Single and double quotes are identical; triple quotes span lines.

s = "Hello, Ganesh"
s.lower()            # 'hello, ganesh'
s.split(", ")        # ['Hello', 'Ganesh']
", ".join(["a", "b"]) # 'a, b'   -- join is called on the separator
s.strip()            # trim whitespace
s.startswith("He")   # True
"Gan" in s           # True  (like str_contains / includes)
s[0], s[-1]          # 'H', 'h'  -- negative index counts from the end
s[0:5]               # 'Hello'   -- slicing: [start:stop:step], stop excluded
s[::-1]              # reversed string

Senior note: building a big string with += in a loop is slow because each += creates a new string. Collect parts in a list and "".join(parts) once.




3. Lists, tuples, sets, dicts



Type    Literal     Mutable     Ordered                 Use it for  

list    [1, 2, 3]   yes         yes                     A collection that changes   

tuple   (1,2)       no          yes                     Fixed records, dict keys, returning several values

set     {1,2}       yes         No                      Uniqueness, fast in checks

dict    {"a", 2}    yes       insertion order kept      Key-value lookup




# list
nums = [3, 1, 2]
nums.append(4)          # push 
nums.pop()              # removes and returns last
nums.sort()             # in place, returns None!
sorted_copy = sorted(nums, reverse=True)   # new list
nums[1:3]               # slice -> new list

# tuple + unpacking (like JS destructuring)
point = (10, 20)
x, y = point
first, *rest = [1, 2, 3, 4]    # first=1, rest=[2, 3, 4]
a, b = b, a                     # swap without temp variable

# set
seen = {"a", "b"}
"a" in seen             # O(1) average, list `in` is O(n)
{1, 2, 3} & {2, 3, 4}   # intersection {2, 3}

# dict
user = {"name": "Ganesh", "city": "Pune"}
user["name"]                  # KeyError if missing
user.get("age")               # None if missing
user.get("age", 0)            # default
for key, value in user.items():
    print(key, value)
{**user, "city": "Mumbai"}    # merge/override, like JS spread
user | {"city": "Mumbai"}     # same, Python 3.9+