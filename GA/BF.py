class Problem:
    def __init__(self, input):
        self.input = input
        self.numTasks = len(input)
    def cost(self, ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime

min=100000
store=[]
def find(a,sum,left,right,level):
    global min
    if(left==right):
        sum+=input[level][a[left]]
        if(sum<min):
            global store
            store=a.copy()
            min=sum
        return     
    b=a[:]
    for i in range(left,right+1):
        b[left],b[i]=b[i],b[left]
        find(b,sum+input[level][b[left]],left+1,right,level+1)

if __name__ == '__main__':
    
    import json
    with open('input.json', 'r') as inputFile:
        data = json.load(inputFile)
        for key in data:
            input = data[key]
            min=100000
            a=[]
            store=[]
            solver = Problem(input)
            input = solver.input
            numTasks = solver.numTasks

            for i in range(0,numTasks):
                a.append(i)
            find(a,0,0,numTasks-1,0)
            print(f"{key}\nAssignment: {store}\nCost: {min}\n")
           

