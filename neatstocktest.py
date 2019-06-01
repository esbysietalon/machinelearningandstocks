import math
import random

import alfa_vantage
import neatmain


# 45
# 
data_0 = alfa_vantage.data_0
data_1 = alfa_vantage.data_1
data_2 = alfa_vantage.data_2
data_3 = alfa_vantage.data_3
data_4 = alfa_vantage.data_4

DATA_LENGTH = len(data_0)
IN_SAMPLE = 90
OUT_SAMPLE = 10

TEST_SIZE = 105

OPTIMIZE_GENS = 5
MODELNUM = 10

print("Test Started (Daily Stock Data)")
neat = neatmain.Main(int(math.floor((DATA_LENGTH - IN_SAMPLE - TEST_SIZE) * 1.0/(OUT_SAMPLE))), MODELNUM)
neat.generateModels()
print("Generated Models Successfully")
for i in range(neat.iterations()):
    # print("ITERATION " + str(i + 1) + " OUT OF " + str(neat.iterations()))
    for j in range(OPTIMIZE_GENS):
        print("GENERATION " + str(j + 1) + " OUT OF " + str(OPTIMIZE_GENS) + " ON ITERATION " + str(i + 1) + " OUT OF " + str(neat.iterations()))
        for m in neat.models(): 
            m.resetEquity()
        neat.runModels(0, data_0[i * OUT_SAMPLE:i * OUT_SAMPLE + IN_SAMPLE])
        neat.runModels(1, data_1[i * OUT_SAMPLE:i * OUT_SAMPLE + IN_SAMPLE])
        neat.runModels(2, data_2[i * OUT_SAMPLE:i * OUT_SAMPLE + IN_SAMPLE])
        neat.runModels(3, data_3[i * OUT_SAMPLE:i * OUT_SAMPLE + IN_SAMPLE])
        neat.runModels(4, data_4[i * OUT_SAMPLE:i * OUT_SAMPLE + IN_SAMPLE])
        neat.cleanGeneRecord()
        neat.evolve()
    for m in neat.models():
        m.resetEquity()
    # print("OUT OF SAMPLE RUN")
    #neat.runModels(0, data_0[((i + 1) * IN_SAMPLE):((i + 1) * IN_SAMPLE + OUT_SAMPLE)])
    #neat.runModels(1, data_1[((i + 1) * IN_SAMPLE):((i + 1) * IN_SAMPLE + OUT_SAMPLE)])
    #neat.runModels(2, data_2[((i + 1) * IN_SAMPLE):((i + 1) * IN_SAMPLE + OUT_SAMPLE)])
    #neat.runModels(3, data_3[((i + 1) * IN_SAMPLE):((i + 1) * IN_SAMPLE + OUT_SAMPLE)])
    #neat.runModels(4, data_4[((i + 1) * IN_SAMPLE):((i + 1) * IN_SAMPLE + OUT_SAMPLE)])
    
    neat.runModels(0, data_0[(IN_SAMPLE + (i * OUT_SAMPLE)):(IN_SAMPLE + ((i + 1) * OUT_SAMPLE))])
    neat.runModels(1, data_1[(IN_SAMPLE + (i * OUT_SAMPLE)):(IN_SAMPLE + ((i + 1) * OUT_SAMPLE))])
    neat.runModels(2, data_2[(IN_SAMPLE + (i * OUT_SAMPLE)):(IN_SAMPLE + ((i + 1) * OUT_SAMPLE))])
    neat.runModels(3, data_3[(IN_SAMPLE + (i * OUT_SAMPLE)):(IN_SAMPLE + ((i + 1) * OUT_SAMPLE))])
    neat.runModels(4, data_4[(IN_SAMPLE + (i * OUT_SAMPLE)):(IN_SAMPLE + ((i + 1) * OUT_SAMPLE))])
    
    maxFitness = 0
    averageFitness = 0
    maxEquity = 0
    averageEquity = 0
    maxStocks = 0
    averageStocks = 0
    realMaxEquity = 0
    for m in neat.models():
        averageFitness += m.potential()
        averageEquity += m.equity()
        averageStocks += m.stocks()
        if maxFitness < m.potential():
            maxFitness = m.potential()
            maxEquity = m.equity()
            maxStocks = m.stocks()
        if realMaxEquity < m.equity():
            realMaxEquity = m.equity()
    averageFitness = averageFitness * 1.0 / len(neat.models())
    averageEquity = averageEquity * 1.0 / len(neat.models())
    averageStocks = averageStocks * 1.0 / len(neat.models())
    print("Max Fitness for Iteration " + str(i + 1) + ": " + str(maxFitness) + " with Cash: " + str(maxEquity) + " and Stocks: " + str(maxStocks))
    print("Average Fitness for Iteration " + str(i + 1) + ": " + str(averageFitness) + " and Average Cash: " + str(averageEquity) + " and Average Stocks: " + str(averageStocks))
    randm = random.randint(0, len(neat.models()) - 1)
    print("Genome for Model " + str(randm) + ": ")
    for g in neat.models()[randm].genome().genes():
        print(str(g.inputNum()) + " -" + str(g.weight()) +"-> " + str(g.outputNum()) + " enabled: " + str(g.isEnabled()))

for m in neat.models():
    m.resetEquity()

neat.runModels(0, data_0[(DATA_LENGTH-TEST_SIZE):DATA_LENGTH])
neat.runModels(1, data_1[(DATA_LENGTH-TEST_SIZE):DATA_LENGTH])
neat.runModels(2, data_2[(DATA_LENGTH-TEST_SIZE):DATA_LENGTH])
neat.runModels(3, data_3[(DATA_LENGTH-TEST_SIZE):DATA_LENGTH])
neat.runModels(4, data_4[(DATA_LENGTH-TEST_SIZE):DATA_LENGTH])

maxFitness = 0
averageFitness = 0
maxEquity = 0
averageEquity = 0
maxStocks = 0
averageStocks = 0
realMaxEquity = 0
bigboy = neat.models()[0]
for m in neat.models():
    averageFitness += m.potential()
    averageEquity += m.equity()
    averageStocks += m.stocks()
    if maxFitness < m.potential():
        maxFitness = m.potential()
        maxEquity = m.equity()
        maxStocks = m.stocks()
        bigboy = m
    if realMaxEquity < m.equity():
        realMaxEquity = m.equity()
averageFitness = averageFitness * 1.0 / len(neat.models())
averageEquity = averageEquity * 1.0 / len(neat.models())
averageStocks = averageStocks * 1.0 / len(neat.models())
print("Max Fitness: " + str(maxFitness) + " with Cash: " + str(maxEquity) + " and Stocks: " + str(maxStocks))
print("Average Fitness: " + str(averageFitness) + " and Average Cash: " + str(averageEquity) + " and Average Stocks: " + str(averageStocks))
print("Max Equity: " + str(realMaxEquity))
print("Bigboy Fitness: " + str(bigboy.potential()) + " with Cash: " + str(bigboy.equity()) + " and Stocks: " + str(bigboy.stocks()))
print("TEST COMPLETED SUCCESSFULLY") 


data = [data_0[(DATA_LENGTH-TEST_SIZE):(DATA_LENGTH-28)], data_1[(DATA_LENGTH-TEST_SIZE):(DATA_LENGTH-28)], data_2[(DATA_LENGTH-TEST_SIZE):(DATA_LENGTH-28)], data_3[(DATA_LENGTH-TEST_SIZE):(DATA_LENGTH-28)], data_4[(DATA_LENGTH-TEST_SIZE):(DATA_LENGTH-28)]]
bigboy.testRun(data)
