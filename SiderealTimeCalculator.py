#Sidereal Time and Julian Date Calculator
#Revision history: Justine Haupt, v1.0 (11/23/17)

#Only valid for dates between 1901 and 2099. Accurate to within 1.1s.

#References:
#http://aa.usno.navy.mil/faq/docs/JD_Formula.php
#http://aa.usno.navy.mil/faq/docs/GAST.php and
class SiderealTime:
    longitude = 0
    date_of_birth = datetime.now()

    # input('Date of birth in format (month-day-year hour:min:second am/pm) ')
    def __init__(self, date_time, longitude):
        self.date_of_birth = datetime.strptime(date_time, '%m-%d-%Y %H:%M')
        self.longitude = longitude
        print(date_of_birth)

    # Longitude of location in question (BMX LAT = 40.869 [40deg 52' 8"], BMX LONG = -72.866 [-72deg 51' 57"], Custer LONG = -72.435)

    # split TD into individual variables for month, day, etc. and convert to floats:
    MM = float(date_of_birth.month)
    DD = float(date_of_birth.day)
    YY = float(date_of_birth.year)
    YY = YY + 2000
    hh = float(date_of_birth.hour)
    mm = float(date_of_birth.minute)
    # convert mm to fractional time:
    mm = mm / 60
    # reformat UTC time as fractional hours:
    UT = hh + mm

    # calculate the Julian date:
    def julian_date(self):
        return (367 * self.YY) - int((7 * (self.YY + int((self.MM + 9) / 12))) / 4) + int((275 * self.MM) / 9) + self.DD + \
               1721013.5 + (self.UT / 24)

    # calculate the Greenwhich mean sidereal time:
    def greenwhich_mean_sidereal_rile(self):
        GMST = 18.697374558 + 24.06570982441908 * (self.julian_date() - 2451545)
        GMST = GMST % 24  # use modulo operator to convert to 24 hours
        GMSTmm = (GMST - int(GMST)) * 60  # convert fraction hours to minutes
        GMSTss = (GMSTmm - int(GMSTmm)) * 60  # convert fractional minutes to seconds
        return int(GMST), int(GMSTmm), int(GMSTss)

    # Convert to the local sidereal time by adding the longitude (in hours) from the GMST.
    # (Hours = Degrees/15, Degrees = Hours*15)
    def local_sidereal_time(self):
        GMST, GMSTMM, GMSTSS = self.greenwhich_mean_sidereal_rile()
        longitude = self.longitude / 15  # Convert longitude to hours
        LST = GMST + longitude  # Fraction LST. If negative we want to add 24...
        if LST < 0:
            LST = LST + 24
        LSTmm = (LST - int(LST)) * 60  # convert fraction hours to minutes
        LSTss = (LSTmm - int(LSTmm)) * 60  # convert fractional minutes to seconds
        return int(LST), int(LSTmm), int(LSTss),
