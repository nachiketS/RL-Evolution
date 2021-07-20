import time,random,sys,pygame,math
pygame.init()
# some parameters for the enviroment
life_span = 100
size = width,height = 480,480
goal = (240,480)
center = (240,0)
step  = 20
population = 50

#defining the surface for the world and its initiation
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.draw.circle(screen,(255,255,0),center,5)
pygame.display.flip()

# causing an infinite loop for now
running = True
path = [] #The decisions each agent makes during their lifetime at each step. Being recorded for the next generation. Will act as genes.
path.append(center) # Will change prolly to a random function starting from the first row or first 20 pixels

# Deciding the random path for an agent
for i in range(1,100):
    temp = list(path[i-1])
    temp[0] += random.randint(-1*step,1*step)
    if temp[0] <0: temp[0] = 0
    if temp[0] > 480:temp[0] = 480
    temp[1] += random.randint(-1*step,1*step)
    if temp[1] <0: temp[1] = 0
    if temp[1] > 480:temp[1] = 480
    path.append(tuple(temp))
# for i in range(1,50):
#     path.append((random.randint(-1*step,1*step),random.randint(-1*step,1*step)))

#====================================================================================================================
# # The idea of using a class works well for limited agents. Whereas in my case I want to build a generation of agents
# # so the object oriented approach might not work here.
# class Agent:
#     def __init__(self,color):
#         self.color = color
#         self.path = [(random.randint(0,480),random.randint(0,step))]
#         for i in range(1,life_span):
#             temp = list(self.path[i-1])
#             temp[0] += random.randint(-1*step,1*step)
#             if temp[0] <0: temp[0] = 0
#             if temp[0] > 480:temp[0] = 480
#             temp[1] += random.randint(-1*step,1*step)
#             if temp[1] <0: temp[1] = 0
#             if temp[1] > 480:temp[1] = 480
#             self.path.append(tuple(temp)) 
#     def genesis(self):
#         pygame.draw.circle(screen,self.color,self.path[i],5)

# #defining the agents
# adam = Agent(color = (0,0,255)) 
# eve = Agent(color = (255,255,0))
#==========================================================================================================================

# a single gene-pool for all the agents from a generation in the form of a dictionary ? or a 2d array ?
# genepool = []
# for i in range(population):
#     genepool.append([(random.randint(0,480),random.randint(0,step))])

genepool = [[(240,0)] for i in range (population)]

for i in range(population):
    for j in range(1,life_span):
        # print(genepool,i,j)
        temp = list(genepool[i][j-1])
        # print(temp)
        temp[0] += random.randint(-1*step,1*step)
        if temp[0] <0: temp[0] = 0
        if temp[0] > 480:temp[0] = 480
        temp[1] += random.randint(-1*step,1*step)
        if temp[1] <0: temp[1] = 0
        if temp[1] > 480:temp[1] = 480
        genepool[i].append(tuple(temp)) 
        # print(genepool[i],i,j)

#criteria for fitness: Taking the average of distance from the goal throughout an agents lifetime and selecting the ones with least distance
def find_fitness(population,goal,life_span,genepool):
    fitness = []
    for i in range(population):
        scores = []
        avg = 0
        for genes in genepool[i]:
            avg+= math.sqrt(((genes[0]-goal[0])**2) + ((genes[1] - goal[1])**2))    
        avg/=life_span
        fitness.append(avg)
    return fitness


#breeding the 20 individuals
def breed(population,life_span,fittest,genepool):
    mutation = 0.06
    new_genepool = []
    for agent in range(population):
        parents = random.sample(fittest,2)
        # print(parents)
        child = []
        for i in range(life_span):
            if i%2 == 0: child.append(genepool[parents[0]][i])
            else : child.append(genepool[parents[1]][i])
            # add random mutation somehow
        for i in range(mutation*life_span):
            turning_point = random.randint(0,life_span)
            child[turning_point] = (child[turning_point-1][0]+(-1 * step) 
            temp = 
            temp[0] += random.randint(-1*step,1*step)
            if temp[0] <0: temp[0] = 0
            if temp[0] > 480:temp[0] = 480
            temp[1] += random.randint(-1*step,1*step)
            if temp[1] <0: temp[1] = 0
            if temp[1] > 480:temp[1] = 480

        new_genepool.append(child)

    return new_genepool

colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(40,235,23)]
population = 5 
life_span = 50
i = 0
while(1):
    print('generation: ',i)
    i+=1
    fitness = find_fitness(population,goal,life_span,genepool)
    print('average distance: ',sum(fitness)/len(fitness))

    #selecting top 20 fittest agents
    fittest = sorted(range(len(fitness)),key=lambda i:fitness[i],reverse = True)[-20:]

    genepool = breed(population,life_span,fittest,genepool)
    # print(genepool[25])
    #running the environment
    print(len(genepool))
    for i in range(life_span):
        # center[0] += path[i][0]
        # center[1] += path[i][1]
        # screen.fill((255,255,255))
        time.sleep(.1)
        # print(i,path[i])
        screen.fill((255,255,255))
        # adam.genesis()
        # eve.genesis()
        for j in range(population):
            color = tuple(colors[j%5])
            # print(color)
            pygame.draw.circle(screen,color,genepool[j][i],5)         
        pygame.display.flip()
    print('end generation')