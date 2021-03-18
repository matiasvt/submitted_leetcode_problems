def int_check(s):
    
    if len(s)==0: return False
    
    if s[0] in ['+', '-']:
        return s[1:].isdigit()
    else:
        return s.isdigit()

def decimal_check(s):
    
    if len(s)==0: return False
    
    if s[0] in ['+', '-'] :
        check_s=s[1:]
    else:
        check_s=s
    
    if '.' in check_s:
        check_s=check_s.split('.')
        if len(check_s)==2:
            
            case1=check_s[0].isdigit() and check_s[1]==''
            if case1: return True
            case2=check_s[0].isdigit() and check_s[1].isdigit()
            if case2: return True
            case3=check_s[1].isdigit() and check_s[0]==''
            return case3
            
        else:
            return False
    else:
        return False


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0: return False
        
        s2=lower(s)
        
        if 'e' in s2:
            s2=s2.split('e')
            if len(s2)==2:
                left_s=(decimal_check(s2[0]) or int_check(s2[0]))  
                right_s = int_check(s2[1])
                return left_s and right_s     
            else:
                return False
            
        else:
            return (decimal_check(s2) or int_check(s2))