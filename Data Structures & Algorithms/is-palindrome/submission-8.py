class Solution:
    def isPalindrome(self, s: str) -> bool:

        head = 0
        tail = len(s)-1

        if len(s) == 0:
            return True
        

        while head < tail:
            while not s[head].isalnum():
                head +=1 

                if head>len(s)-1:
                    return True

            character1 = s[head].lower()

            while not s[tail].isalnum():
                if tail<=0:
                    return True
                tail-=1 
            character2 = s[tail].lower()
            
            if character1 != character2:
                return False

            tail -= 1
            head +=1 
        
        return True

            
