# the second in-class coding file from October 3


def calculate_days (years, months, days):
    """

    :param years:
    :param months:
    :param days:
    :return:
    """
    age = 365 * years + 30 * months + days
#    age += (years//4) #add the appropriate number of days to account for leap years
    age += add_leap_years(years)  #function call from one function to another
    return age

def add_leap_years(years):
    """

    :param years:
    :return:
    """
    return years//4


if __name__ == "__main__":
    yrs = int(input("How many years old are you"))
    mos = int(input("How many months since your birthday"))
    ds = int(input("How many days"))
    age = calculate_days(yrs,mos,ds)
#    age = calculate_days(ds,yrs,mos)
    print ("You are ", age, "days old")

#    calculate_days(yrs,mos,3) = 5 * yrs #this is what you cannot do

