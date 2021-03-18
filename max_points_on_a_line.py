class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<2 : return len(points)
        
        aligned_with_p=[]
        sol=0
        for p in points:
            if (p[0],p[1]) not in aligned_with_p:
                
                p_rep=len(filter((lambda x: x==p),points))
                
                #center with p and discard same x coordinate for valid quotient
                quot_list_valid=[((x[1]-p[1]),(x[0]-p[0]))  for x in points if x[0]!=p[0] ] 



                quot_count= len(filter((lambda x: x[0]==p[0]), points))

                for (a,b) in set(quot_list_valid):
                    aligned_with=p_rep
                    for (c,d) in quot_list_valid:                     
                            if a*d==b*c: #cross product check
                                aligned_with+=1
                    quot_count = max(aligned_with, quot_count)

                aligned_with_p.append((p[0],p[1]))
                sol=max(sol,quot_count) 
        
        return sol