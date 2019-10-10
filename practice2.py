# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:56:47 2019

@author: bhuwan.madhikarmi
"""
#
#input n number of test scores and print the runner up
#
def main():
    n = int(input())
#    if n in range(2,11):
    if n >=2 and n <=10:
#    if 2<= n <=10:
#        print("input is okay"+str(n))
        arr = map(int, input().split())
        arr_sorted = sorted(arr, reverse=True)
        maz_arr = arr_sorted[0] #max_arr = max(arr)
        for i in arr_sorted:
            if i in range(-100,101):
                #print(str(i) +" input score is inside the range")
                if i != maz_arr:
                    return i
            else:
#                print(str(i) +" input score is out of range, exiting...")
                return -1
    else:
#        print(str(n) +" is out of range, exiting...")     
        return -1
#    arr = map(int,input().split())
#    for n in arr:
#        print(n)
    
if __name__ == "__main__":
    main()
 
    
#def calculate_2nd_lowest(score_card):
#    for s in score_card:
#        if s[1] != score_card[0][1]: 
#            print("2nd high score="+str(s))
#            return s[1]
        
def get_all_2nd(score_card):
    for i in range(len(score_card)):
        if score_card[i][1] != score_card[0][1]:
            return i
def print_all_2nd(score_card,  index_):
    res = []
    for i in range(index_, len(score_card)):
        if score_card[i][1] == score_card[index_][1]:
#            print(score_card[i][0])
            res.append(score_card[i][0])
    for r in sorted(res):
        print(r)
    return -1
def main():
#    score_card = [['a',3],['z',2.5],['c',4],['d',2.5],['e',1],['f',1]]
    score_card = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ind_score = [name, score]
        score_card.append(ind_score)

    sort_score_card = sorted(score_card, key = lambda x:x[1])   
    index_ = get_all_2nd(sort_score_card)
    print_all_2nd(sort_score_card, index_)
    
            
        
if __name__ == "__main__":
    main()
    
  