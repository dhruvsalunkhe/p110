from datetime import date
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

figure = ff.create_distplot([data],["time"],show_hist=False)
figure.show()

print("mean of original/population data =", statistics.mean(data) )
print("sd of original/population data  =", statistics.stdev(data) )

def randomsetpicker(samplesize):
    sample = []
    for i in range(0,samplesize):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        sample.append(value)
    mean = statistics.mean(sample)
    return mean

def samplingcalculator():
    mean_list = []
    for i in range(0,1000):
        randomsetmean = randomsetpicker(100)
        mean_list.append(randomsetmean)
    figure = ff.create_distplot([mean_list],["temp"],show_hist=False)
    figure.show()
    print("mean of sampling distribution =", statistics.mean(mean_list) )

    print("sd of sampling distribution =", statistics.stdev(mean_list) )


samplingcalculator()