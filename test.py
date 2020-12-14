from source import futureTripAnalysis

productionMatrix = np.array([[5549, 13888, 5991],[7317, 18998, 7825],[6150, 16355, 6533],[8359, 23587, 9682],[4708, 11773, 5053]])
attractionMatrix = np.array([[5048, 10409, 6179],[11443, 23688, 14142],[10433, 17385, 10273],[7236, 19356, 11282],[2861, 8155, 4961]])
travelTimeMatrix = np.array([[7,9.14,18.08,20.16,33.56],[9.21,5,6.68,11.23,24.63],[18.74,6.74,15,13.56,30.96],[20.56,11.56,13.7,12,24.34],[32.22,23.22,29.42,22.64,10]])
""" The given matrices used in prior project """

HBW_tripmatriX, HBO_tripmatriX, NHB_tripmatriX = TripMatrixcreator(travelTimeMatrix, productionMatrix, attractionMatrix, 1)

Bus_travelTimesaving = np.array([[0.09,0.08,0.14,0.30,0.27],[0.07,0.19,0.17,0.13,0.09],[0.22,0.30,0.26,0.20,0.24],[0.13,0.09,0.30,0.19,0.16],[0.22,0.18,0.27,0.29,0.21]])
Bus_travelTimeMatrix = (1 - Bus_travelTimesaving) * travelTimeMatrix
""" A function for creating the travel time matrix for bus. This is usually found and calculated beforehand."""

HBW_tripAutoMatriX, HBW_tripBusMatriX, HBO_tripAutoMatriX, HBO_tripBusMatriX, NHB_tripAutoMatriX, NHB_tripBusMatriX = ModelSplit(HBW_tripmatriX, HBO_tripmatriX, NHB_tripmatriX, travelTimeMatrix, Bus_travelTimeMatrix)

finalTrip,finalPeakTrip = TripTablecreator(HBW_tripAutoMatriX, HBW_tripBusMatriX, HBO_tripAutoMatriX, HBO_tripBusMatriX, NHB_tripAutoMatriX, NHB_tripBusMatriX, 1.1, 1.15, 1.25, 35, 0.4)
print(finalTrip)
print(finalPeakTrip)
