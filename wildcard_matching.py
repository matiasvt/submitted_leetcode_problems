def remove_adj_ast(p):
    res=p
    while('**' in res):
        res=res.replace('**','*')
    return res

def last_letters(p):
    l=len(p)-1
    res=''
    while(l>0):
        if p[l].isalpha() :
            res+=(p[l])
            l-=1
        else:
            break
    return (res[::-1])

precalculated_matches={}

class Solution(object):
    def isMatch(self,s, p,i_s=0,i_p=0):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if i_s==i_p==0:
            precalculated_matches={}  
            print precalculated_matches
        else:
            global precalculated_matches
        
        p_cnt=0
        
        p = remove_adj_ast(p)
        
        if p =='*' : 
            precalculated_matches[(i_s,i_p)]=True
            return True
        
        if s==p : 
            precalculated_matches[(i_s,i_p)]=True
            return True      
        
        tail_p=last_letters(p)
        if len(tail_p)<len(s) and len(tail_p)>0 : 
            if tail_p != s[-len(tail_p):] :
                precalculated_matches[(i_s,i_p)]=False
                return False

        if (i_s,i_p) in precalculated_matches: return precalculated_matches[(i_s,i_p)]

        for i,l in enumerate(s):
            if p_cnt == len(p) : 
                precalculated_matches[(i_s,i_p)]=False
                return False

            if p[p_cnt]==l or p[p_cnt]=='?':
                p_cnt+=1
            elif p[p_cnt]=='*':
                
                if p_cnt==len(p)-1 : 
                    precalculated_matches[(i_s,i_p)]=True
                    return True
                
                adv_both =  self.isMatch(s[i+1:],p[p_cnt+1:],i_s=i_s+i+1,i_p=i_p+p_cnt+1) if (i<len(s)-1 and p_cnt<len(p)-1) else False
                
                if adv_both : 
                    precalculated_matches[(i_s,i_p)]=True
                    return True
                
                adv_s =  self.isMatch(s[i+1:],p[p_cnt:],i_s=i_s+i+1,i_p=i_p+p_cnt) if (i<len(s)-1 ) else False
                
                if adv_s : 
                    precalculated_matches[(i_s,i_p)]=True
                    return True
                
                adv_p = self.isMatch(s[i:],p[p_cnt+1:],i_s=i_s+i,i_p=i_p+p_cnt+1) if (p_cnt<len(p)-1)  else False
                
                if adv_p :
                    precalculated_matches[(i_s,i_p)]=True
                    return True
                else:
                    precalculated_matches[(i_s,i_p)]=False
                    return False                    

                
            else:
                precalculated_matches[(i_s,i_p)]=False
                return False
        
        if p_cnt==len(p) : 
            precalculated_matches[(i_s,i_p)]=True
            return True            

        if (p_cnt == len(p)-1) and p[p_cnt]=='*' : 
            precalculated_matches[(i_s,i_p)]=True
            return True
        
        precalculated_matches[(i_s,i_p)]=False
        return False