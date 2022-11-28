import readCsv as csv
import dataFilter
#import charts


country = input("Pais a consultar ? ")
dataBase = csv.read_csv('world_population.csv')

countryData = dataFilter.filterItem(dataBase, 'Country/Territory', country)

#print(countryData)


dataPopulation = dataFilter.filterPopulation('Population', countryData)

print(dataPopulation)
print(dataPopulation.type())
#charts.generate_bar_chart(labels, values)