# This is the code to perform the t-test which gives a positive result.
import numpy as np
import statistics
import math
# The following array gives the yield per hectare for field_1. The unit for yield is Quintal per hectare
field_1_yield = [15.2
,15.3
,16.0
,15.8
,15.6
,14.9
,15.0
,15.4
,15.6
,15.7
,15.5
,15.2
,15.5
,15.1
,15.3
,15.0]

# The following array gives the yield per hectare for field_2. The unit for yield is Quintal per hectare
field_2_yield = [15.6
,15.9
,15.2
,16.6
,15.2
,15.8
,15.8
,16.2
,15.6
,15.6
,15.8
,15.5
,15.5
,15.5
,14.9
,15.9]

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
print("Operation                  Field_1                   Field_2")
print("***********************************************************************")
print ("Mean:               ",mean_field_1,"\t", mean_field_2)
print ("Standard Deviation: ",std_field_1,"\t", std_field_2)
print ("Variance:           ",variance_field_1,"\t", variance_field_2)
print ("T-Value:            ",t_value)
print("***********************************************************************")
dof = len(field_1_yield)+len(field_2_yield)-2

#From the t-table we extract the critical value for p=0.05 and DOF = 30
critical_value = 2.04

if (t_value < critical_value):
	print ("We accept the null hypothesis")
else:
	print ("We reject the null hypothesis")
print("***********************************************************************")