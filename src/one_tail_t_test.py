# This is the code to perform the t-test which gives a positive result.
import numpy as np
import statistics
import math
# The following array gives the yield per hectare for field_1. The unit for yield is Quintal per hectare
before = [185
,192
,206
,177
,225
,168
,256
,239
,199
,218
,193
,175
,215
,200
,199]

# The following array gives the yield per hectare for field_2. The unit for yield is Quintal per hectare
after = [169
,187
,193
,176
,194
,171
,228
,217
,204
,195
,186
,178
,192
,183
,180]

diff_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range (len(after)):
	diff_arr[i] = after[i] - before[i]

mean_diff = np.mean(diff_arr)
u_diff = 0
std_diff = statistics.stdev(diff_arr)
n = len(before)

t_value = (mean_diff - u_diff) / (std_diff / math.sqrt(n))

critical_value = -1.7613 #(-ve for left one tail t-test)

print("**************************************************************")
print("Mean Difference:                        ",mean_diff)
print("Degrees of Freedom [One-tail t-test]:    14")
print("T_value :                               ",t_value)
print("Critical value:                         ",critical_value)
print("**************************************************************")
if (t_value < critical_value):
	print ("We reject the null hypothesis")
if (t_value > critical_value):
	print ("We accept the null hypothesis")
print("**************************************************************")



#Calculating the mean of the yield of the two fields
'''

t_value = abs((mean_field_1 - mean_field_2)/math.sqrt((variance_field_1/(len(field_1_yield))) + (variance_field_2/(len(field_2_yield)))))

print("***********************************************************************")
print("Operation                  Field_1                   Field_2")
print("***********************************************************************")
print ("Mean:               ",mean_field_1,"\t", mean_field_2)
print ("Standard Deviation: ",std_field_1,"\t", std_field_2)
print ("Variance:           ",variance_field_1,"\t", variance_field_2)
print ("T-Value:            ",t_value)
print("***********************************************************************")
dof = len(field_1_yield)-1

#From the t-table we extract the critical value for p=0.05 and DOF = 14
critical_value = 1.76

if (t_value < critical_value):
	print ("We accept the null hypothesis")
else:
	print ("We reject the null hypothesis")
print("***********************************************************************")
'''