import pandas as pd

class Nematode:
    def __init__(self, id, species, dosage, intensity):
        self.id = id
        self.species = species
        self.dosage = dosage
        self.intensity =  intensity

    def __str__(self):
        return f"Nematode: {self.id} , {self.dosage}, {self.species}, {self.intensity}"

    def listData(fileName):
        df = pd.read_excel(fileName)
        data = df.values.tolist()
        dataList = []

        for i in data:
            dataList.append(Nematode(*i))

        return dataList     

    def sortSpecies(dataList, species):
        sortedSpecies = []
        for i in range(len(dataList)):
            if (dataList[i].species == species):
                sortedSpecies.append(dataList[i])
        return sortedSpecies

    def sortDosage(dataList, dosage):
        sorted_dosage = []
        for i in range(len(dataList)):
            if (dataList[i].dosage == dosage):
                sorted_dosage.append(dataList[i])
        return sorted_dosage

    def sortIntensity(dataList, level):
        reverse = True
        if(level == "Low"):
            reverse = False
        dataList.sort(key=lambda x:x.intensity, reverse = reverse)
        return dataList

    def intensityList(dataList):
        intensityList =[]
        for i in range(len(dataList)):
            intensityList.append(dataList[i].intensity)
        
        return intensityList

    def sortIntensityList(dataList, dosage, species):
        sortedIntensity = []
        for i in range(len(dataList)):
            if (dataList[i].species == species) and (dataList[i].dosage == dosage):
                sortedIntensity.append(dataList[i].intensity)
        return sortedIntensity
    
    def infectedNum(dataList):
        copyList = dataList.copy()
        for i in range(len(dataList)):
            if(dataList[i].intensity == 0):
                copyList.remove(dataList[i])
        return len(copyList)

    def infectedList(dataList):
        copyList = dataList.copy()
        for i in range(len(dataList)):
            if(dataList[i].intensity == 0):
                copyList.remove(dataList[i])
        return copyList

    def prevalence(dataList):
        return Nematode.infectedNum(dataList)/len(dataList)
    
    def sumIntense(dataList):
        sum = 0
        infectedList = Nematode.infectedList(dataList)
        for i in range(len(infectedList)):
            sum += infectedList[i].intensity
        return sum

    def meanIntensity(dataList):
        sumIntense = Nematode.sumIntense(dataList)
        infected = Nematode.infectedList(dataList)
        return sumIntense/len(infected)
    
    def relAbundance (dataList):
        sumIntense = Nematode.sumIntense(dataList)
        return sumIntense/len(dataList)
    
        
                

