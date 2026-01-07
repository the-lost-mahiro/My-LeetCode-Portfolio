class Solution:
    def decodeString(self, s: str) -> str:
        cur_str = ''
        cur_num = ''
        stack = []

        for char in s:
            if char.isdigit():
                cur_num += char
            elif char == '[':
                stack.append([cur_str, cur_num])
                cur_str = ''
                cur_num = ''
            elif char == ']':
                prev_str, prev_num = stack.pop()
                cur_str = prev_str + int(prev_num) * cur_str
            else:
                cur_str += char
        
        return cur_str
