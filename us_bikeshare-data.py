import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
 
    
    city = input('Would you like to see data from chicago, new york city or washington?    \n')
    
    # We need to convert the city string into lower case 
    while city.lower() not in ('chicago', 'new york city','washington'):
        print('Please enter a correct city name    \n')
        city = input('Would you like to see data from chicago, new york city or washington?\n')
        
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to see data from? Please choose january, february, march, april, may, june or all         \n')
    
    # We need to convert the city string into lower case 
    while month.lower() not in ( 'january','february','march','april','may','june','all'):
        print('Please enter a correct month    \n')
        month=input('Which month would you like to see data from? Please choose january, february, march, april, may, june or all         \n')
              
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which day of the week would you like to see data from? Please write your response as an integer. Example.     Monday = 1, Tuesday = 2, Wednesday = 3... \n' )
    while day not in ("1", '2', '3', '4', '5', '6', '7'):
        print('Please enter a correct day of week from 1 to 7, Monday to Sunday.\n')
        day= input('Which day of the week would you like to see data from? Please write your response as an integer.\n                   Example: Monday = 1, Tuesday = 2, Wednesday = 3...and so on\n' )
      

    print('-'*40)
    print (city.lower(), month.lower(), day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    city = city.lower()
    month = month.lower()
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    ##print(df.head())
    ##print(df.columns)
     
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    ##print(f"Month column:\n{df['month'].head()}")

    # Day of week, from (1-7) 
    df['day_of_week'] = df['Start Time'].dt.dayofweek + 1
    ##print(f"Day of week:\n{df['day_of_week'].head()}")
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        ##print(f"Filtered df by month {month}: {df.head()}")

    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        #Changed day to integer to do filter
        df = df[df['day_of_week'] == int(day)]

        ##print(f"Filtered df by day of week {day}: {df.head()}")

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    start_time = time.time()
    
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    ##print(f"Month.head() -- {df['month'].head()}")
    ##print(df['month'].value_counts())
    popular_month = df['month'].value_counts().idxmax()
    
    print('\nMonth:')
    print('Most Common month:', popular_month)

    # TO DO: display the most common day of week
    # Mapping dayofweek, +1 is to map 0-6 to 1-7
    df['day_of_week'] = df['Start Time'].dt.dayofweek + 1
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('\nDay of week:')
    print('Most Common day of week:', popular_day_of_week )

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    print("\nHour:")
   

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common used start station is: ', most_common_start_station)
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nThe most common used end station is: ', most_common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    # Groupby returns a series where the labels are the index, so that's why idxmax works
    most_common_start_finish = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\nThe most frequent combination of start station and end station trip are: ', most_common_start_finish )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print ('\nThe total travel time is: ',total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean() 
    print ('\nThe mean travel time is: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df.groupby('User Type').size()

    print('\nThe count for different user types is: ', user_type)
    
    
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
    
        counts_of_gender = df.groupby('Gender').size()
        print('\nThe count of gender is: ', counts_of_gender)
        
    else: 
        print('\nThis city doesn\'t provide Gender in their data')
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
    
        df['Birth Year'] = pd.to_datetime(df['Birth Year'])
        least_recent_date = df['Birth Year'].min()
        recent_date = df['Birth Year'].max()
        most_common_date = df['Birth Year'].mode()[0]
        print('\nThe most recent date of Birth is: ',recent_date)
        print('\nThe most common date of Birth is: ', most_common_date)
    
    else:
        print('\nThis city doesn\'t provide with Birth Year')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
         
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        ## We give the user the option to see five lines of raw data
        show_data = input ('\nWould you like to see five lines of raw data? Enter yes or no\n')
        count = 1
        while show_data.lower() != 'no':
            print(df.iloc[[count, count + 1, count + 2, count + 3, count + 4]] )
            show_data = input ('\nWould you like to see five lines of raw data? Enter yes or no\n')
            count += 5
        
        
        ## We give the user the option to restart 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
      
            
if __name__ == "__main__":
	main()
