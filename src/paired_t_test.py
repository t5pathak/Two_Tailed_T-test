# This is the code to perform the t-test which gives a positive result.
import numpy as np
import statistics
import math
# The following array gives the yield per hectare for field_1. The unit for yield is Quintal per hectare
field_1_yield = [53
,56
,55
,48
,39
,45
,48
,43
,51
,54]

# The following array gives the yield per hectare for field_2. The unit for yield is Quintal per hectare
field_2_yield = [73
,65
,71
,65
,63
,70
,65
,68
,63
,71]

#Calculating the mean of the yield of the two fields
mean_field_1 = np.mean(field_1_yield)
mean_field_2 = np.mean(field_2_yield)

#std_field_1 = np.std(field_1_yield)
std_field_1 = statistics.stdev(field_1_yield)
std_field_2 = statistics.stdev(field_2_yield)

variance_field_1 = pow(std_field_1,2)
variance_field_2 = pow(std_field_2,2)

t_value = abs((mean_field_1 - mean_field_2)/math.sqrt((variance_field_1/(len(field_1_yield))) + (variance_field_2/(len(field_2_yield)))))

print("***********************************************************************")
print("Operation                  Age_5                   Age_15")
print("***********************************************************************")
print ("Mean:               ",mean_field_1,"\t\t\t", mean_field_2)
print ("Standard Deviation: ",std_field_1,"\t", std_field_2)
print ("T-Value:            ",t_value)
print("***********************************************************************")
dof = len(field_1_yield)-1

#From the t-table we extract the critical value for p=0.05 and DOF = 30
critical_value = 1.8331

if (t_value < critical_value):
	print ("We accept the null hypothesis")
else:
	print ("We reject the null hypothesis")
print("***********************************************************************")