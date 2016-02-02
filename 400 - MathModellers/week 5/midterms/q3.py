import numpy as np

birthrate = np.array([.0341,.0173,.0187,.0135,.0099])
deathrate = np.array([.0115,.0073,.0058,.0083,.0102])

populations = np.array([[365,2038,284,222,460], \
                        [476,2495,362,252,484], \
                        [627,2977,442,277,496], \
                        [801,3438,522,313,514], \
                        [1017,3827,591,344,522]])

births = np.around(birthrate*populations)
deaths = np.around(deathrate*populations)

birthsByYear = np.sum(births,axis=1)
deathsByYear = np.sum(deaths,axis=1)

#now make it pretty for display
years = np.array([1970,1980,1990,2000,2010])
pretty = np.vstack([years,birthsByYear,deathsByYear])
pretty = np.transpose(pretty)
print(pretty)