# Jones_Final_Project Description 

This program conducts the trip distribution and model split of future trip analysis and creates the final trip table for the calculated results. After studies are conducted on a specific area of interest, this program can be used to calculate the amount of people-trips expected to be generated within each zone of the area of interest. The people-trips are broken down into trip type. The expect mode of transportation of these people-trips are also calculated. From that, a general trip table can be created of the number of vehicle-trips conducted in each zone of the area of analyzation.

Assumptions:
* The only mode of transportation is by car or bus only
* The equation for calculating Home-Based Work, Home-Based Others, and Non-Home Based is kept constant
* The average ocupancy of bus is kept constant
* The utility function and constants are kept constant

Input:
* Production Matrix
* Attraction Matrix
* Travel Time Matrix

Output:
* Trip matrix for HBW, HBO, and NHB
* Trip matrix for HBW, HBO, and NHB per mode of transportation
* Final Trip Table in vehicle-trips
* Peak Hour Trip table
