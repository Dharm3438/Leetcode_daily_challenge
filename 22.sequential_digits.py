'''
1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

https://leetcode.com/problems/sequential-digits/
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        output = []
        
        digit_stack = [ *range(9, 0, -1) ]
        
        while digit_stack:
            
            cur_value = digit_stack.pop()
            
            if high >= cur_value >= low:
				# current value is valid sequential digits in range
                output.append( cur_value )
            
            elif cur_value > high:
                # current value is out of boundary
                # stop growing on this case
                continue
            
			# get LSB digit
            last_digit = cur_value % 10
            
            if last_digit == 9:
                # last digit is 9 already
                # stop growing on this case
                continue
            
            # compute growing value based on current value and last digit
            growing_value = 10*cur_value + (last_digit+1)
            
            digit_stack.append( growing_value )
            
        return sorted( output )