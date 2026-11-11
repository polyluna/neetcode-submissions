class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "[({":
                stack.append(s[i])
            elif s[i] == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif len(stack) > 0 and s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif len(stack) > 0  and s[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0



        # if len(s) % 2 != 0:
        #     return False
        # else:
        #     s1 = s[:len(s)//2]
        #     s2 = s[len(s)//2:]
        #     s3 = s2[::-1]
            
        #     for i in range(len(s3)):
        #         if s3[i] == ")":
        #             return s1[i] == "("
        #         elif s3[i] == "]":
        #             return s1[i] == "["
        #         elif s3[i] == "}":
        #             return s1[i] == "{"
        #         else:
        #             return False


