import numpy as np
import statistics

#Harris & Benedict
def energyneed_hb(gender, weight, height, age):
  if gender == 'm':
    bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775*age)
  elif gender == 'f':
    bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676*age)
  else:
    print('Incorrect format for gender ')

  return round(bmr)

  #Schofield (men and women 18-30 years old)
def energyneed_scho(gender, weight):
  if gender == 'm':
    bmr = 63 * weight + 2896
  elif gender == 'f':
    bmr = 62 * weight + 2036
  else:
    print('Incorrect format for gender')

  bmr_kcal = bmr * 0.2388

  return round(bmr_kcal)

 #Mifflin St Jeor
def energyneed_miff(gender, weight, height, age):
  if gender == 'm':
    bmr = 10 * weight + 6.25 * height - 5*age + 5
  elif gender == 'f':
    bmr = 10 * weight + 6.25 * height - 5*age - 161
  else:
    print('Incorrect format for gender ')

  return round(bmr)

gender = 'f'
w = 58
h = 167
age = 33
PAL = 1.6

bmr_hb = energyneed_hb(gender, w, h, age)
bmr_scho = energyneed_scho(gender, w)
bmr_miff = energyneed_miff(gender, w, h, age)

print('--------------------BMR------------------')
print('Your BMR according to Harris & Benedict is: ' + str(bmr_hb))
print('Your BMR according to Schofield is: ' + str(bmr_scho))
print('Your BMR according to Mifflin St Jeor is: ' + str(bmr_miff))

bmr_list = [bmr_hb, bmr_scho, bmr_miff]
bmr_mean = round(statistics.mean(bmr_list))

print('Your average BMR is: ' + str(bmr_mean))

print('--------------------TEE at PAL = ' + str(PAL) + ' ------------------')
print('Your TEE according to Harris & Benedict is: ' + str(round(PAL*bmr_hb)))
print('Your TEE according to Schofield is: ' + str(round(PAL*bmr_scho)))
print('Your TEE according to Mifflin St Jeor is: ' + str(round(PAL*bmr_miff)))

TEE_list = [PAL*bmr_hb, PAL*bmr_scho, PAL*bmr_miff]
TEE_mean = round(statistics.mean(TEE_list))

print('Your average TEE is at PAL = ' + str(PAL) + ' is: ' + str(TEE_mean))


print('--------------------TEE at different PALs ------------------')
for PAL_i in np.arange(1.1, 2.1, 0.1):
  print('With BMR ' + str(round(bmr_mean,1)) +' kcal and PAL ' + str(round(PAL_i,1)) + ' your TEE is: ' + str(round(PAL_i*bmr_mean)))
