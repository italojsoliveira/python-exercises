# Write a program that receives a distance value in meters and outputs a message saying its corresponding values in km, hm, dam, dm, cm, and mm.

meter_distance = float(input('Enter the distance in meters: '))

km_distance = meter_distance / 1000

hm_distance = meter_distance / 100

dam_distance = meter_distance / 10

dm_distance = meter_distance * 10

cm_distance = meter_distance * 100

mm_distance = meter_distance * 1000


print('The measure of {} m correspond to \n {} km \n {} hm \n {} dam \n {} dm \n {} cm \n {} mm'.format(meter_distance, km_distance,
                                                                                                        hm_distance, dam_distance, dm_distance, cm_distance, mm_distance))