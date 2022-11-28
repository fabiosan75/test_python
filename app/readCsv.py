import csv

def read_csv(path):
  with open(path) as fp:
    reader = csv.reader(fp, delimiter=',')
    header = next(reader)
    data = []
    for line in reader:
      iterable = zip(header,line)
      row = {key: value for key,value in iterable}
      data.append(row)

    return data
    
    

'''
Rank	
CCA3	
Country/Territory	
Capital	
Continent	2022 
Population	2020 
Population	2015 
Population	2010 
Population	2000 
Population	1990 
Population	1980 
Population	1970 
Population	
Area
Density	
Growth_Rate

'''

if __name__ == '__main__':
  data = read_csv('world_population.csv')
  print(data)