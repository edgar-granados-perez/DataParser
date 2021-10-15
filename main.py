import nematode
import scipy.stats as stats
import data

def main():
    nematode_instances = nematode.Nematode.listData("LR_data.xlsx")

    sf_data = nematode.Nematode.sortSpecies(nematode_instances, "SF")
    hb_data = nematode.Nematode.sortSpecies(nematode_instances, "HB")

    sf_low_dos = nematode.Nematode.sortDosage(sf_data, "Low")
    hb_low_dos = nematode.Nematode.sortDosage(hb_data, "Low")

    sf_med_dos = nematode.Nematode.sortDosage(sf_data, "Medium")
    hb_med_dos = nematode.Nematode.sortDosage(hb_data, "Medium")

    sf_high_dos = nematode.Nematode.sortDosage(sf_data, "High")
    hb_high_dos = nematode.Nematode.sortDosage(hb_data, "High")
    
    sf_intensity = nematode.Nematode.intensityList(sf_data)
    hb_intensity = nematode.Nematode.intensityList(hb_data)

    sf_low_int = nematode.Nematode.sortIntensityList(nematode_instances, "Low", "SF")
    hb_low_int = nematode.Nematode.sortIntensityList(nematode_instances, "Low", "HB")

    sf_med_int = nematode.Nematode.sortIntensityList(nematode_instances, "Medium", "SF")
    hb_med_int = nematode.Nematode.sortIntensityList(nematode_instances, "Medium", "HB")

    sf_high_int = nematode.Nematode.sortIntensityList(nematode_instances, "High", "SF")
    hb_high_int = nematode.Nematode.sortIntensityList(nematode_instances, "High", "HB")


    print("mean Intensity of overall sf")
    print(nematode.Nematode.meanIntensity(sf_data))
    
    print("mean Intensity of SF(low, med, high)")
    print(f"{nematode.Nematode.meanIntensity(sf_low_dos)}, {nematode.Nematode.meanIntensity(sf_med_dos)}, {nematode.Nematode.meanIntensity(sf_high_dos)}")
    
    print("Relative Abundance for SF")
    print(nematode.Nematode.relAbundance(sf_data))

    print("\n")
    print("mean Intensity of overall hb")
    print(nematode.Nematode.meanIntensity(hb_data))

    print("mean Intensity of HB(low, med, high)")
    print(f"{nematode.Nematode.meanIntensity(hb_low_dos)},{nematode.Nematode.meanIntensity(hb_med_dos)}, {nematode.Nematode.meanIntensity(hb_high_dos)}")
    
    print("Relative Abundance for HB")
    print(nematode.Nematode.relAbundance(hb_data))
    
    print("\n")
    print("prevalence of sf")
    print(nematode.Nematode.prevalence(sf_data))

    print("prevalence of hb")
    print(nematode.Nematode.prevalence(hb_data))
    print("\n")
    print("overall ttest")
    print(stats.ttest_ind(sf_intensity,hb_intensity))
    
    print("ttest by high")
    print(stats.ttest_ind(sf_high_int, hb_high_int))
    
    print("ttest by medium")
    print(stats.ttest_ind(sf_med_int, hb_med_int))
    
    print("ttest by low")
    print(stats.ttest_ind(sf_low_int, hb_low_int))

if __name__ == "__main__":
    main()