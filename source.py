import numpy as np

class: futureTripAnalysis:

    """ The future trip analysis is seperated into 3 parts to give the user flexibility in determining which analysis is
    of focus. Trip Distribution creates matrices based on trip type. Model Split aids in analyzing the type of mode of
    transportation expected to be use and its demand. The trip table provides an overall analyzation of the number of vehicles
    expected to be use."""

    def TripDistribution(traveltimeMatrix, productionmatrix, attractionmatrix, kij):
        HBW_frictionFactor = traveltimeMatrix * -0.9982 + 101.88
        HBO_frictionFactor = traveltimeMatrix * -0.8684 + 88.633
        NHB_frictionFactor = traveltimeMatrix *  -0.5818 + 59.384
        """ Above is the equation for obtaining the friction factor for the different types of trips as a function of time.
        This is needed in solving for the trip Matrix using the equation Pi * (AjFijKij) / sum(AjFijKij). """

        HBW_AjFijKij = HBW_frictionFactor * attractionMatrix[:,0] * kij
        HBO_AjFijKij = HBO_frictionFactor * attractionMatrix[:,1] * kij
        NHB_AjFijKij = NHB_frictionFactor * attractionMatrix[:,2] * kij
         """ Above is used for solving for AjFiJKij part of the equation """

        HBW_sumAjFijKij = np.sum(HBW_AjFijKij,axis=1)
        HBO_sumAjFijKij = np.sum(HBO_AjFijKij,axis=1)
        NHB_sumAjFijKij = np.sum(NHB_AjFijKij,axis=1)
        """ Above is used for solving the sum of the AjFijKij"""

        HBW_tripMatrix = HBW_AjFijKij.transpose() * productionMatrix[:,0] / HBW_sumAjFijKij
        HBW_tripMatrix = HBW_tripMatrix.round().transpose()
        HBO_tripMatrix = HBO_AjFijKij.transpose() * productionMatrix[:,1] / HBO_sumAjFijKij
        HBO_tripMatrix = HBO_tripMatrix.round().transpose()
        NHB_tripMatrix = NHB_AjFijKij.transpose() * productionMatrix[:,2] / NHB_sumAjFijKij
        NHB_tripMatrix = NHB_tripMatrix.round().transpose()
        """ Above is the final calculation for the trip matrix of the three types of trips """

        return HBW_tripMatrix, HBO_tripMatrix, NHB_tripMatrix
        """ The result is 3 matrices of the person-trip of each zone for each trip type """

    def ModelSplit(HBW_TripMatrix, HBO_TripMatrix, NHB_TripMatrix, Auto_travelTime, Bus_travelTime):

        Auto_Ta, Bus_Ta = [5, 10]
        Auto_Tw, Bus_Tw = [0, 10]
        Auto_C, Bus_C = [250, 225]
        Auto_aK, Bus_aK = [-0.01, -0.07]
        """ Above is the constant for determining which mode of transportation people will prefer. The Ta stands for access time,
        tw stands for wait time, C stands for cost per trip, aK is a callibration constant. The time is calculated in minutes
        and the cost in cents. These values can be changed via user input, however in effort to ensure the code is comprehendable
        without too many variables these constants are assumed to be kept constant """

        Auto_uFactor = -0.03 * Auto_travelTime + Auto_aK - 0.05*Auto_Ta - 0.04*Auto_Tw - 0.014*Auto_C
        Bus_uFactor = -0.03 * Bus_travelTime + Bus_aK - 0.05*Bus_Ta - 0.04*Bus_Tw - 0.014*Bus_C
        """ Above is used for finding the factor of utility for the auto and bus mode of transportation. This is done
        using the utility function. """

        Auto_Prob = np.exp(Auto_uFactor) / (np.exp(Auto_uFactor) + np.exp(Bus_uFactor))
        Bus_Prob = np.exp(Bus_uFactor) / (np.exp(Auto_uFactor) + np.exp(Bus_uFactor))
        """ Above is used for finding the probability of people choosing auto or bus for each zone """

        HBW_tripAutoMatrix = Auto_Prob * HBW_TripMatrix
        HBW_tripAutoMatrix = HBW_tripAutoMatrix.round()
        HBW_tripBusMatrix = Bus_Prob * HBW_TripMatrix
        HBW_tripBusMatrix = HBW_tripBusMatrix.round()
        HBO_tripAutoMatrix = Auto_Prob * HBO_TripMatrix
        HBO_tripAutoMatrix = HBO_tripAutoMatrix.round()
        HBO_tripBusMatrix = Bus_Prob * HBO_TripMatrix
        HBO_tripBusMatrix = HBO_tripBusMatrix.round()
        NHB_tripAutoMatrix = Auto_Prob * NHB_TripMatrix
        NHB_tripAutoMatrix = NHB_tripAutoMatrix.round()
        NHB_tripBusMatrix = Bus_Prob * NHB_TripMatrix
        NHB_tripBusMatrix = NHB_tripBusMatrix.round()
        """ Above is used for finding the final model split analysis for each trip type """

        return HBW_tripAutoMatrix, HBW_tripBusMatrix, HBO_tripAutoMatrix, HBO_tripBusMatrix, NHB_tripAutoMatrix, NHB_tripBusMatrix
        """ The function results in 6 matrices, a person-trip matrix for bus and for auto for each trip type """

    def TripTablecreator(HBW_tripAutoMatrix, HBW_tripBusMatrix, HBO_tripAutoMatrix, HBO_tripBusMatrix, NHB_tripAutoMatrix, NHB_tripBusMatrix, HBW_Auto_averageOcupancy, HBO_Auto_averageOcupancy, NHB_Auto_averageOcupancy, Bus_averageOcupancy, peakHourFactor):

        HBW_tripTable = HBW_tripAutoMatrix / HBW_Auto_averageOcupancy + HBW_tripBusMatrix / Bus_averageOcupancy
        HBW_tripTable = np.floor(HBW_tripTable)
        HBO_tripTable = HBO_tripAutoMatrix / HBO_Auto_averageOcupancy + HBO_tripBusMatrix / Bus_averageOcupancy
        HBO_tripTable = np.floor(HBO_tripTable)
        NHB_tripTable = NHB_tripAutoMatrix / NHB_Auto_averageOcupancy + NHB_tripBusMatrix / Bus_averageOcupancy
        NHB_tripTable = np.floor(NHB_tripTable)
        """ Above is used for finding the number of vehicles expected to be used for each type of trip """

        TripTable = HBW_tripTable + HBO_tripTable + NHB_tripTable
        """ Above is the total vehicles expectancy """

        peakHourTripTable = TripTable * peakHourFactor
        peakHourTripTable = peakHourTripTable.round()
        """ Above is used for finding the expected demand during the peak hour or peak of unit of measurement """"

        return TripTable, peakHourTripTable
        """ The function results in a general total trip table and a peak time trip table """
