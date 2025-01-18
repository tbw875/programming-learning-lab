# F-Strings

# Allow you to set variables within pre-built strings

#example

foo = "bar"

print(f"Today I passed the {foo} exam")

# Works for all kinds of dtypes in the variable

bar = 22

print(f"Today I am {bar} years old")

# and can evaluate expressions within the fstring

math = 84
science = 99
english = 81

print(f"Jared's report card shows he averaged {(math+science+english)/3} percent this quarter across 3 subjects")

# Prints today's date with help
# of datetime library
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


