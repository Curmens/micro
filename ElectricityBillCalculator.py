#defining variables

Reading1 = input('enter prev meter reading: ')
Reading2 = input('enter current meter reading: ')
Days = input('enter Period of Days: ')
amtOfDays = int(Days)
    

def meterReadings(x, y):
    prev_meterReading = int(x)
    cur_meterReading = int(y)
    meter_diff = cur_meterReading - prev_meterReading
    multiplier = 1.00
    print('Meter Difference Total ' + str(meter_diff))
    return meter_diff

meterValues = meterReadings(Reading1, Reading2)

def bill_Calculation(meterDiff, dayPeriod):
    period = int(dayPeriod)
    service_charge = period
    national_Electrification = 146.82
    streetLight = 146.82

    if period == 31:
        life_line = 51
    elif period == 30:
        life_line = 49
    elif period == 29:
        life_line = 47
    elif period == 28:
        life_line = 45
    else:
         print('--Data not acurate check DATE---')

    EFT = meterDiff - life_line
    calc_EFT = EFT * 0.6542
    calc_lifeline = life_line * 0.3261
    calc_serviceCharge = service_charge * 0.2452
    calc_streetLight = streetLight * 0.0300
    calc_nationalElectrification = national_Electrification * 0.0200


    TOTAL = calc_serviceCharge + calc_lifeline + calc_nationalElectrification + calc_EFT + calc_streetLight
    print('|------------------------------------------------|')
    print('|  LABEL     |     UNIT                          ')
    print('|------------------------------------------------|')
    print('|  LIFE LINE |      {}                           '.format(life_line))
    print('|------------------------------------------------|')
    print('|  EFT       |      {}                           '.format(EFT))
    print('|------------------------------------------------|')
    print('|  SERVICE   |      {}                         '.format(service_charge))
    print('|------------------------------------------------|')
    print('|  NAT-ELEC  |      {}                         '.format(national_Electrification))
    print('|------------------------------------------------|')
    print('|  TOTAL     |      {}                         '.format(TOTAL))


bill_Calculation(meterValues, amtOfDays)

