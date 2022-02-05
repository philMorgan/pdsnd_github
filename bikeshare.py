import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

print()
"""functions"""

def city_menu():
    """Defines the city menu"""
    print('-'*5 +'City Menu' + '-'*5 )
    print('[1] Chicago')
    print('[2] New York')
    print('[3] Washington')
    print('[0] Exit the program.')

def month_menu():
    """Defines the month menu"""
    print('-'*5 +'Month Menu' + '-'*5 )
    print('[0] No month filter')
    print('[1] January')
    print('[2] February')
    print('[3] March')
    print('[4] April')
    print('[5] May')
    print('[6] June')

def day_menu():
    """Defines the day menu"""
    print('-'*5 +'Day Menu' + '-'*5 )
    print('[0] No day filter')
    print('[1] Sunday')
    print('[2] Monday')
    print('[3] Tuesday')
    print('[4] Wednesday')
    print('[5] Thursday')
    print('[6] Friday')
    print('[7] Saturday')

def city_param():
    """
    Asks user to specify a city to filter the data

    Dependencies:
        city_menu()

    Returns:
        (str) city - global variable, name of the city to analyze
    """
    global city
    city_menu()

    while True:
        try:
            city_option = int(input("Enter the number representing your city: "))
            if city_option == 0:
                city = 'quit'
                break
            elif city_option == 1:
                city = 'chicago'
                break
            elif city_option == 2:
                city = 'new york'
                break
            elif city_option == 3:
                city = 'washington'
                break
            else:
                print("Not a valid option")
        except:
            print("You didn't enter a number.")
            #city_option = 0

    if city_option == 0:
        print("Thanks for using this program - Time to quit")
        #city = 'quit'
    else:
        print("\n Applying filter for - {} \n".format(city.title()))

    return city

def month_param(city):
    """
    Asks user to specify a month to filter the data

    Dependencies:
        month_menu()

    Returns:
        (str) month - global variable, name of the month to filter by, or "all" to apply no month filter
    """
    global month
    month=''
    if city != 'quit':
        month_menu()

        while True:
            try:
                month_option = int(input("Enter the number representing the month to filter by: "))
                if month_option == 0:
                    month = 'all'
                    break
                elif month_option == 1:
                    month = 'january'
                    break
                elif month_option == 2:
                    month = 'february'
                    break
                elif month_option == 3:
                    month = 'march'
                    break
                elif month_option == 4:
                    month = 'april'
                    break
                elif month_option == 5:
                    month = 'may'
                    break
                elif month_option == 6:
                    month = 'june'
                    break
                else:
                    print("Not a valid option! ")
                    #month_option = 0
            except:
                print("You didn't enter a number. ")
                #month_option = 0



        print("\n Applying filter for - \n{}, {} \n".format(city.title(),month.title()))


        return month

def day_param(city):
    """
    Asks user to specify a day to filter the data

    Dependencies:
        day_menu()

    Returns:
        (str) day - global variable, name of the month to filter by, or "all" to apply no month filter
    """
    global day
    day=''
    if city != 'quit':
        day_menu()

        while True:
            try:
                day_option = int(input("Enter the number representing the day to filter by: "))
                if day_option == 0:
                    day = 'all'
                    break
                elif day_option == 1:
                    day = 'sunday'
                    break
                elif day_option == 2:
                    day = 'monday'
                    break
                elif day_option == 3:
                    day = 'tuesday'
                    break
                elif day_option == 4:
                    day = 'wednesday'
                    break
                elif day_option == 5:
                    day = 'thursday'
                    break
                elif day_option == 6:
                    day = 'friday'
                    break
                elif day_option == 7:
                    day = 'saturday'
                    break
                else:
                    print("Not a valid option! ")

            except:
                print("You didn't enter a number. ")




        print("\n Applying filter for - \n{}, {}, {} \n".format(city.title(),month.title(), day.title()))


        return day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    # if the program hasn't been told to exit
    if city != 'quit':
        # load data file into a dataframe
        df = pd.read_csv(CITY_DATA[city])

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month, day of week, hour from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour


        # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1

        # filter by month to create the new dataframe
            df = df[df['month'] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

        return df

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hey! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_param()
    month_param(city)
    day_param(city)

    print('-'*40)
    return city, month, day

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].dropna(axis=0).mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    #month = months.index(month) + 1
    print('Most Common Month:', months[popular_month-1].title())

    # TO DO: display the most common day of week
    popular_dow = df['day_of_week'].dropna(axis=0).mode()[0]
    print('Most Common day:', popular_dow)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].dropna(axis=0).mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].dropna(axis=0).mode()[0]
    print('Most Common Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].dropna(axis=0).mode()[0]
    print('Most Common End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']=df['Start Station'] + ' | ' + df['End Station']
    popular_trip = df['Trip'].dropna(axis=0).mode()[0]
    print('Most Common Trip (Start Station and End Station ): ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].dropna(axis=0).sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].dropna(axis=0).mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: \n {} \n'.format((df['User Type'].value_counts())))

    # TO DO: Display counts of gender
    if city in ['chicago','new york']:
        print('Counts of gender: \n {} \n'.format((df['Gender'].value_counts())))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city in ['chicago','new york']:
        early_yob = int(df['Birth Year'].dropna(axis=0).min())
        latest_yob = int(df['Birth Year'].dropna(axis=0).max())
        mode_yob = int(df['Birth Year'].dropna(axis=0).mode()[0])
        print('Earliest, most recent, and most common year of of birth are {}, {} and {} respectively'.format(early_yob, latest_yob, mode_yob))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """for displaying raw data in increments of 5 rows"""
    start = 0
    end = 5
    total_rows = len(df['Start Time'])
    while True:
        raw=input('\nWould you like to view 5 lines of raw data? Enter "y" or "n".\n')
        if raw == 'n':
            break
        elif end > total_rows:
           print(df.iloc[start:])
           break
        else:
            #raw_df = df[start,end]
            print(df.iloc[start:end])
            start += 5
            end += 5

def main():
    while True:
        #city, month, day = get_filters()
        get_filters()
        if city != 'quit':
            df = load_data(city, month, day)
            #print(df['Trip'])
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            raw_data(df)




        break


if __name__ == "__main__":
	main()
