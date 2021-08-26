def minFlipsMonoIncr(s :str)->int:
        one = flip = 0
        for i in s:
            if i == "1":
                one +=1
            else:
                flip +=1
            flip = min(one,flip)
        return flip    
            
# we go through string and found out how much 1 before index much be flipped to 0 and how much 0 after index need to be flipped to 1. adds them up and get min for result           