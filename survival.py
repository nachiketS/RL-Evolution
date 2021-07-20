# Remake because last one was a total mess
import random,math,time,sys,pygame

pygame.font.init()

life_span = 50
population = 50
step = 20
goal = (240,480)
class agent:
    def __init__(self,step,life_span,aai=[],baba=[]):
        self.x = 240
        self.y = 0
        self.life_span = life_span
        self.step = step
        if aai == []:
            aai = [(random.randint(-step,step),random.randint(-step,step)) for _ in range(self.life_span)]
        if baba == []:
            baba = [(random.randint(-step,step),random.randint(-step,step)) for _ in range(self.life_span)]
        self.aai= aai
        self.baba = baba
        self.genes = self.get_genes()
        self.life = self.bhavishya_bagha()    
    def get_genes(self):
        genes = []
        mutation = 0.02
        for i in range(self.life_span):
            if i%2 == 0:genes.append(self.aai[i])
            else: genes.append(self.baba[i])
        # add mutaion here.
        
        for i in range(math.floor(self.life_span*mutation)):
            genes[random.randint(1,self.life_span-1)] = ((random.randint(-self.step,self.step)),(random.randint(-self.step,self.step)))
        return genes
    def bhavishya_bagha(self):
        life = [(self.x,self.y)]
        for i in self.genes:
            temp = [0,1]
            temp[0] = life[-1][0] + i[0]
            temp[1] = life[-1][1] + i[1]
            life.append(tuple(temp))
        return life

class environment:
    def __init__(self,step,life_span,population,goal):
        self.life_span = life_span
        self.population = population
        self.goal = goal
        self.step = step
        self.genepool = self.genesis()
        self.current_generation = 0
    def genesis(self):
        genepool = []
        for i in range(self.population):
            temp = agent(self.step, self.life_span)
            genepool.append(temp)
        return genepool
    def generation(self,screen):
        for i in range(self.life_span):
            # print(self.genepool[i].life[j])
            time.sleep(.025)
            pygame.event.pump()
                # print(i,path[i])
            screen.fill((160, 255, 125))
            font = pygame.font.SysFont('Ubuntu-TH',30)
            text = font.render('generation : '+str(self.current_generation),True,(0,0,0))
            screen.blit(text,(0,0))
            pygame.draw.circle(screen,(0,255,0),self.goal,10)         
            for j in range(self.population):
                pygame.draw.circle(screen,(4,30,66),self.genepool[j].life[i],5)         
                pygame.display.flip()
        print('end of generation ',self.current_generation)
        print(sum(self.get_fitness())/len(self.get_fitness()))
        self.current_generation+= 1
        self.breeding()
    # the way fitness is being calculated is 
    # I'm averaging the distances at all the points in time of the life of an agent.
    # Thus this fitness score will never be 0. 
    # However the logic is still to minimize this score so as to survive.
    def get_fitness(self):
        fitness = []
        for i in range(self.population):
            avg = 0
            for j in range(self.life_span):
                print(math.sqrt(((self.genepool[i].life[j][0]-self.goal[0])**2) + ((self.genepool[i].life[j][1] - self.goal[1])**2)))
                avg+= math.sqrt(((self.genepool[i].life[j][0]-self.goal[0])**2) + ((self.genepool[i].life[j][1] - self.goal[1])**2))    
            avg/=self.life_span
            fitness.append(avg)
        return fitness
    def breeding(self):
        new_genepool = []
        fitness = self.get_fitness()
        fittest = sorted(range(len(fitness)),key=lambda i:fitness[i],reverse = True)[-20:]
        for i in range(self.population):
            parents = random.sample(fittest,2)
            child = agent(self.step,self.life_span,self.genepool[parents[0]].genes,self.genepool[parents[1]].genes)
            new_genepool.append(child)
        self.genepool = new_genepool
    


pangea = environment(step,life_span,population,goal)
print(pangea.genepool)

screen = pygame.display.set_mode((480,480))
screen.fill((255,255,255))
pygame.draw.circle(screen,(255,255,0),(240,0),5)
pygame.display.flip()


while(1):
    pangea.generation(screen)