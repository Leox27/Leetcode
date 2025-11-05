### Roman to Integer Leetcode Problem Solution

s = str(input("Enter the Roman numeral: "))
# s = "LVIIII"

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        integer_value = 0
        
        for i in range(len(s)): 
            current_value = roman_map[s[i]]
            print(f"{i+1}th roman value is: {current_value}")

            if i + 1 < len(s):
                next_value = roman_map[s[i+1]]
                
                if current_value < next_value:
                    integer_value -= current_value
                else:
                    integer_value += current_value
            else:
                integer_value += current_value

        return print(f"The total sum is {integer_value}")

print(Solution().romanToInt(s))

#  Accepted
#  Runtime: 4 ms