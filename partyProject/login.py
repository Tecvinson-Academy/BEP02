import pandas as pd

user_data = pd.read_csv('user_data.csv')  #get user data
user_data.set_index('Email', inplace=True)

def check_password(user_name, entered_password):
    try:
        passw = user_data.loc[user_name,'Password']
        if passw == entered_password:
            return True
        else:
            return False
    except KeyError:
        return False
