def grade_mcq(sol, ans):
    if len(sol) != len(ans):
        return -1
    score = sum([1 if sol[i] == ans[i]
                else 0 for i in range(len(sol))])
    return score
    
exec(input()) # DON'T remove this line