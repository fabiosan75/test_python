  
def filterItem(iterable, key, value):
  return list(filter(lambda item: item[key] == value, iterable))

def filterPopulation (findKey, iterable):
  data = dict()
  for item in iterable:
    #print(item.items())

    data = [ (key[:4]), float(value) for key, value in item.items() if findKey in key ]
    #for key, value in item.items():
    #  if findKey in key:
        #print(f'{key[:4]} >> {value}')
    #    data[key[:4]] = int(value)
  
  #[ [key, value for key, value in item.items()] for item in iterable ]
  return data


#   {c: c.upper() for c in text if c in 'aeiou' }


def checkKey(findKey, item):
  print(item)
  # if(findKey in item.)


if __name__ == '__main__':
  items = [
{
	"Rank": "46",
	"CCA3": "YEM",
	"Country/Territory": "Yemen",
	"Capital": "Sanaa",
	"Continent": "Asia",
	"2022 Population": "33696614",
	"2020 Population": "32284046",
	"2015 Population": "28516545",
	"2010 Population": "24743946",
	"2000 Population": "18628700",
	"1990 Population": "13375121",
	"1980 Population": "9204938",
	"1970 Population": "6843607",
	"Area (km²)": "527968",
	"Density (per km²)": "63.8232",
	"Growth Rate": "1.0217",
	"World Population Percentage": "0.42"
}, {
	"Rank": "63",
	"CCA3": "ZMB",
	"Country/Territory": "Zambia",
	"Capital": "Lusaka",
	"Continent": "Africa",
	"2022 Population": "20017675",
	"2020 Population": "18927715",
	"2015 Population": "16248230",
	"2010 Population": "13792086",
	"2000 Population": "9891136",
	"1990 Population": "7686401",
	"1980 Population": "5720438",
	"1970 Population": "4281671",
	"Area (km²)": "752612",
	"Density (per km²)": "26.5976",
	"Growth Rate": "1.028",
	"World Population Percentage": "0.25"
}, {
	"Rank": "74",
	"CCA3": "ZWE",
	"Country/Territory": "Zimbabwe",
	"Capital": "Harare",
	"Continent": "Africa",
	"2022 Population": "16320537",
	"2020 Population": "15669666",
	"2015 Population": "14154937",
	"2010 Population": "12839771",
	"2000 Population": "11834676",
	"1990 Population": "10113893",
	"1980 Population": "7049926",
	"1970 Population": "5202918",
	"Area (km²)": "390757",
	"Density (per km²)": "41.7665",
	"Growth Rate": "1.0204",
	"World Population Percentage": "0.2"
}
]

  dataCountry = filterItem(items, 'Country/Territory', 'Zimbabwe')
  dataPopulation = filterPopulation('Population', dataCountry)
  print(dataPopulation)

  

