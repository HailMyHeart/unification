substitution = []
formulas = []
"""
    substitute the variable to item
"""
def insertToFormula(formula, i, item):
    if len(formula)==1:
        return item.split("|")[0]
    else:
        return formula[:i]+item.split("|")[0]+formula[i+1:]
"""
    judge if the formulas set have a MGU or not;
    if can't be unified, return 0;
    if read the end of all formulas, return 1;
    if have difference on some char, return -1;
"""
def canSubstitute():
    global n
    global formulas
    global substitution
    curItem = ""#Item substituting to variables(only one index)
    curVariable = []#variables to substituted(only one index)
    count = 0#index
    isOver = False#judge if read end of all formulas or not
    isEqual = True#judge the chars is the same or not
    while (isEqual):
        isOver = True
        #judge if read the "End" mark and if the "End" of all formulas is read, then return 1
        for i in range(n):
            if formulas[i][count] != "E":
                isOver = False
        if isOver:
            return 1        
        #if not read all "End", judge if the count of item is equal(that is ,if char read of one is regular, the other is "End",
        #then return 0)
        for i in range(n-1):
            if (formulas[i][count]!=formulas[i+1][count]):
                if formulas[i][count]=="E" or formulas[i+1][count]=="E" or formulas[i][count]=="," or formulas[i+1][count]=="," or formulas[i][count]=="(" or formulas[i+1][count]==")" or formulas[i+1][count]==")":
                    return 0
        #if char read of all formulas is regular, and there is difference, then do something and return -1
        #                                ...    ,and all chars is same, then count++, and keep cycling
        for i in range(n-1):
            if (formulas[i][count]!=formulas[i+1][count]):#found difference
                for j in range(n):
                    curStack = []#stack to matching the parenthesis pair
                    curFormula = formulas[j]#the formula to handled
                    curChar = curFormula[count]#the char of current formula to handled
                    #if curChar is variable, then append it to curVariable
                    if curChar == "v" or curChar == "w" or curChar == "x" or curChar == "y" or curChar == "z":
                        if not curChar in curVariable:
                            curVariable.append(curChar)
                    #if curChar belongs to one item
                    else:
                        #if curChar is constant
                        if curChar == "a" or curChar == "b" or curChar == "c" or curChar == "d" or curChar == "e":
                                curItem2=curChar
                        #if curChar is belongs to function or predicate, then get the maximum item
                        else:
                            curCount = count+2
                            curStack.append("(")
                            while(len(curStack)>0):
                                if curFormula[curCount] == "(":
                                    curStack.append("(")
                                elif curFormula[curCount] == ")":
                                    curStack.pop()
                                curCount+=1
                            curItem2=curFormula[count:curCount]
                        #if there is already have one item and current item is different,then return 0
                        if len(curItem)>0 and curItem2!=curItem:
                            return 0
                        elif len(curItem)==0:
                            curItem = curItem2
                #if some variable belongs to the item, return 0   
                if len(curItem)>1:
                    for aVariable in curVariable:
                        if aVariable in curItem:
                            return 0
                #add current substitution to substitution
                curSubstitution = []
                for aVariable in curVariable:
                    curSubstitution.append(curItem+"|"+aVariable)
                substitution.append(curSubstitution)
                #set isEqual False to make the cycle end
                isEqual = False
                break
        #all chars is same, then count++, and keep cycling
        count+=1
    return -1         
"""
    make set substituted
"""
def subsititute():
    global substitution
    global formulas
    for item in substitution[-1]:
        for i in range(len(formulas)):
            curFormula = formulas[i]
            while item.split("|")[1] in curFormula:
                curIndex = curFormula.index(item.split("|")[1]) 
                curFormula = insertToFormula(curFormula, curIndex, item)
            formulas[i] = curFormula
"""
    get MGU of input set
"""
def getMGU():
    #substitution of substitution
    global substitution
    while len(substitution)>1:
        for item in substitution[1]:
            for j in range(len(substitution[0])):
                curSubLeft = substitution[0][j].split("|")[0]
                curSubRight = substitution[0][j].split("|")[1]
                while item.split("|")[1] in curSubLeft:
                    curIndex = curSubLeft.index(item.split("|")[1])
                    curSubLeft = insertToFormula(curSubLeft, curIndex, item)
                if curSubLeft == curSubRight:
                    substitution[0][j]=""
                else:
                    substitution[0][j]=curSubLeft+"|"+curSubRight
            while("" in substitution[0]):
                substitution[0].remove("")                                         
        substitution[0] += substitution[1]
        del substitution[1]                  
"""
    Here is main 
"""
n = int(raw_input("Input the count of formulas:"))
for i in range(n):
    formulas.append(raw_input(":")+"E")
start = canSubstitute()
#keep judge until there is no difference or judged that there is no MGU
while(start == -1):
    subsititute()
    start = canSubstitute()
if start == 0:
    print("No Unification")#There is no MGU
else:
    getMGU()
    print("MGU is:")
    if len(substitution)==0:
        print("Empty")#No need
    else:
        print(substitution[0])    
    
     
                    
                    
                    
                
                            
            