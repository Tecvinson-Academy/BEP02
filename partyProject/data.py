import pandas as pd

pd.set_option('display.max_columns', 10)
packages = pd.read_csv('party_packages.csv')
orders_data = pd.read_csv('orders.csv')

def get_packages():
    return packages.columns.to_list()

def get_package_items(package_name):
    return packages[package_name].to_list()

def get_package_details(package):
    return packages[package].to_list()

def get_oders(user):
    filt = (orders_data['Email'] == user)
    orders = orders_data[filt]
    return orders[['Order_Date','Delivery_Date', 'Delivery_Address', 'Package', 'No_of_people', 'Status']].to_numpy().tolist()

def get_profile(user):
    user_data = pd.read_csv('user_data.csv', index_col='Email')
    current_user = user_data.loc[user].to_list()
    return current_user


def update_profile(user):
    print(user)

    # user_orders = orders[filt]
    # print(user_orders)
    # return orders.to_numpy().tolist()

    # print(orders.columns)
    # return orders_data.columns


    # orders_data.drop(columns=['Name', 'Surname'], inplace=True)
    # orders_data.to_csv('orders.csv', index=False)

    # orders_list = orders.to_numpy().tolist()

    # for row in orders_list:
    #     print(row)
# get_oders()
# def get_user_order():
#     print(orders_data.columns)
# print(get_oders('johndoe@mail.com'))