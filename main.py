#Формула Харріса-Бенедикта для розрахунку базового обміну речовин (БОР)
#Harris-Benedict formula for calculating basal metabolic rate (BMR)


#Для чоловіків:
#БОР = 88,362 + (13,397 x вага у кілограмах) + (4,799 x висота в сантиметрах) - (5,677 x вік у роках)
#For men:
#BOR = 88.362 + (13.397 x weight in kilograms) + (4.799 x height in centimeters) - (5.677 x age in years)

#Для жінок:
#БОР = 447,593 + (9,247 x вага у кілограмах) + (3,098 x висота в сантиметрах) - (4,330 x вік у роках)
#For women:
#BOR = 447.593 + (9.247 x weight in kilograms) + (3.098 x height in centimeters) - (4.330 x age in years)


def get_numeric_input(numeric):
    """function of checking input numbers"""
    while True:
        try:
            value = float(input(numeric))
            if value > 0:
                return value
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_bmr(gender, age, weight, height):
    """function to calculate basal metabolism"""
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        bmr = None
    return bmr


def user_info():
    """function to get user data"""
    while True:
        gender = input('What gender are you? Male or female: ').lower()
        if gender in ('male', 'female'):
            break
        else:
            print("Invalid input. Please provide 'male' or 'female' as gender.")

    age = get_numeric_input('How old are you? ')
    weight = get_numeric_input('What is your weight in kilograms? ')
    height = get_numeric_input('What is your height in centimeters? ')

    bmr_result = calculate_bmr(gender, age, weight, height)

    if bmr_result is not None:
        print("Your Basal Metabolic Rate (BMR) is:", bmr_result)
    else:
        print("Invalid input. Please provide 'male' or 'female' as gender.")

    return bmr_result


def calculate_activity(bmr_result):
    """a function to count the level of user activity"""

    activity_levels = {
        'none': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'heavy': 1.725,
        'extreme': 1.9
    }

    while True:

        activity_level_choice = input('What is your activity level (none, light, moderate, heavy, or extreme): ').lower()

        if activity_level_choice in activity_levels:

            activity_level = activity_levels[activity_level_choice] * bmr_result

            return activity_level
        else:
            print("Invalid input. Please choose from 'none', 'light', 'moderate', 'heavy', or 'extreme'.")


def gain_or_lose(activity_level):
    """function to determine the user's goal"""
    while True:
        goals = input('Do you want to lose, maintain, or gain weight: ').lower()

        if goals in ('lose', 'maintain', 'gain'):
            break
        else:
            print("Invalid input. Please choose from 'lose', 'maintain', or 'gain'.")

    if goals == 'lose':
        calories = activity_level - 500
    elif goals == 'maintain':
        calories = activity_level
    elif goals == 'gain':
        while True:
            gain = input('Gain 1 or 2 kilograms per week? Enter 1 or 2: ')
            if gain in ('1', '2'):
                break
            else:
                print("Invalid input. Please choose '1' or '2'.")
        calories = activity_level + int(gain) * 500

    print('In order to', goals, 'weight, your daily caloric goals should be', float(calories), '!')


gain_or_lose(calculate_activity(user_info()))




