import pickle
import numpy as np
import pandas as pd
from keras.models import load_model


def convertTo1dArray(arr):
    retList = []
    for i in range(len(arr)):
        retList.append(arr[i][0])
    return retList


def roundList(arr):
    return [round(num) for num in arr]


data = pd.read_csv('rainfall_in_india_1901-2015.csv')
linear_model = pickle.load(open('linearModel.sav', 'rb'))
cnnStateModel = load_model('CNN_model.h5')

data2 = pd.read_csv('district_wise_rainfall_normal.csv')
linear_district = pickle.load(open('Linear_District.sav', 'rb'))
cnnDistrictModel = load_model('CNN_District.h5')


def stateLinearPredict(state, year):
    temp = data[['SUBDIVISION', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[data['YEAR'] == year]

    data1 = np.asarray(temp[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                             'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[temp['SUBDIVISION'] == state])

    X_year = None
    y_year = None
    for i in range(data1.shape[1] - 3):
        if X_year is None:
            X_year = data1[:, i:i + 3]
            y_year = data1[:, i + 3]
        else:
            X_year = np.concatenate((X_year, data1[:, i:i + 3]), axis=0)
            y_year = np.concatenate((y_year, data1[:, i + 3]), axis=0)

    y_year_pred = linear_model.predict(X_year)
    return roundList(y_year_pred.tolist()), roundList(y_year.tolist())


#print(stateLinearPredict('TELANGANA',2015))

def stateCNNPredict(state, year):
    temp = data[['SUBDIVISION', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[data['YEAR'] == year]

    data1 = np.asarray(temp[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                             'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[temp['SUBDIVISION'] == state])

    X_year = None
    y_year = None
    for i in range(data1.shape[1] - 3):
        if X_year is None:
            X_year = data1[:, i:i + 3]
            y_year = data1[:, i + 3]
        else:
            X_year = np.concatenate((X_year, data1[:, i:i + 3]), axis=0)
            y_year = np.concatenate((y_year, data1[:, i + 3]), axis=0)

    y_year_pred = cnnStateModel.predict(np.expand_dims(X_year, axis=2))
    return roundList(convertTo1dArray(y_year_pred.tolist())), roundList(y_year.tolist())


#print(stateCNNPredict('TELANGANA',2015))

def districtpredict(district, state):
    temp = data2[['DISTRICT', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[
        data2['STATE_UT_NAME'] == state]
    hyd = np.asarray(temp[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[
                         temp['DISTRICT'] == district])
    X_year = None
    y_year = None
    for i in range(hyd.shape[1] - 3):
        if X_year is None:
            X_year = hyd[:, i:i + 3]
            y_year = hyd[:, i + 3]
        else:
            X_year = np.concatenate((X_year, hyd[:, i:i + 3]), axis=0)
            y_year = np.concatenate((y_year, hyd[:, i + 3]), axis=0)

    y_year_pred = linear_district.predict(X_year)
    return roundList(y_year_pred.tolist()), roundList(y_year.tolist())


#print(districtpredict('HYDERABAD','ANDHRA PRADESH'))

def districtCNNPredict(district, state):
    temp = data2[['DISTRICT', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[
        data2['STATE_UT_NAME'] == state]
    hyd = np.asarray(temp[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].loc[
                         temp['DISTRICT'] == district])
    X_year = None
    y_year = None
    for i in range(hyd.shape[1] - 3):
        if X_year is None:
            X_year = hyd[:, i:i + 3]
            y_year = hyd[:, i + 3]
        else:
            X_year = np.concatenate((X_year, hyd[:, i:i + 3]), axis=0)
            y_year = np.concatenate((y_year, hyd[:, i + 3]), axis=0)

    y_year_pred = cnnDistrictModel.predict(np.expand_dims(X_year, axis=2))
    return roundList(convertTo1dArray(y_year_pred.tolist())), roundList(y_year.tolist())

#print(districtCNNPredict('HYDERABAD','ANDHRA PRADESH'))



