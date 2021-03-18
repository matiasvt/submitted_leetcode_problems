def reduce_steps(mod_len,steps,erased_needed,steps_letters,len_cond): # require steps and mod_len in same order

    step_count=erased_needed

    while(erased_needed>0 and not(all(elem == 0 for elem in steps)) and not(all(elem == 2 for elem in mod_len)) ) :   
        
        for i,m in enumerate(mod_len):
            
            if m==0 and steps[i]>0 and erased_needed>0:
                mod_len[i]=(mod_len[i]-1)%3
                steps[i]-=1
                erased_needed-=1

        for i,m in enumerate(mod_len):

            if m==1 and steps[i]>0 and erased_needed>0:
                mod_len[i]=(mod_len[i]-1)%3
                erased_needed-=1
        

    if all(elem == 2 for elem in mod_len) and erased_needed>0 :
        
         while(erased_needed>2 and sum(steps)>0):
                
                for i,m in enumerate(mod_len):
                    
                    if steps[i]>0 and erased_needed>=3:
                        steps[i]-=1
                        erased_needed-=3
        

    return max(sum(steps),steps_letters)+step_count



def find_3_or_more(password):
    
            
    l_act=l_prev=''

    rep_cnt=1
    rep_letter=False

    steps=[]
    mod_len=[]

    for i,l in enumerate(password):
        l_prev=l_act
        l_act=l

        if l_act == l_prev : 
            rep_letter=True
            rep_cnt+=1
        else:

            if rep_cnt>=3:
                steps.append(rep_cnt/3)
                mod_len.append(rep_cnt%3)

            rep_letter=False
            rep_cnt=1
      
    if rep_cnt>=3: #last iteration correction
        steps.append(rep_cnt/3)
        mod_len.append(rep_cnt%3)

    return steps,mod_len

class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        
        p_len=len(password)
        len_cond=6<=p_len<=20
        low_limit=6-p_len
        upp_limit=p_len-20
        
        one_lower ,one_upper , one_digit=any(l.islower() for l in password) , any(l.isupper() for l in password) , any(l.isdigit() for l in password)
                
        letters_cond=one_lower and one_upper and one_digit
        
        
        #search triplets
        steps, mod_len=find_3_or_more(password)
        
        rep_strings_cond=len(steps)==0
        
        if len_cond and letters_cond and rep_strings_cond : 
            return 0
        else: #handle steps
            
            if len_cond:
                steps_len=0
            else:
                steps_len=max(low_limit,upp_limit)
            
            steps_letters=0
            
            if not(one_lower):
                steps_letters+=1
            if not(one_upper):
                steps_letters+=1
            if not(one_digit):
                steps_letters+=1
            
            
            if not(rep_strings_cond):
                               
                if low_limit>0: #3-4-5 case
                    min_steps=max(steps_len,steps_letters)
                
                else:
                                                                                   
                    if steps_len>0: #erase
                        min_steps=reduce_steps(mod_len,steps,steps_len,steps_letters,len_cond)
                    else:
                        min_steps=max(sum(steps),steps_letters)
                        
                    
                    
                    
                
            
            else:
                
                if low_limit>0: #cases for adding appropriately
                    min_steps=max(steps_len,steps_letters)
                else:
                    min_steps=steps_len+steps_letters
                
            return min_steps
            
                
