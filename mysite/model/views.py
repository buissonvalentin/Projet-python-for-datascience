from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pickle
import pandas as pd
from rest_framework.parsers import JSONParser
from django.http                    import HttpResponse
from django.http                    import JsonResponse
from os import listdir

import dataset
import pandas as pd 


def logistic_regression(request):
    if request.method == "GET":
        df = create_dataset(request)
        loaded_model = pickle.load(open("logistic_regression.dat", "rb"))
        pred = loaded_model.predict(df)[0]
        return JsonResponse({"pred" : int(pred)}  , status=200)

def xgboost(request):
    if request.method == "GET":
        df = create_dataset(request)
        loaded_model = pickle.load(open("xgboost.dat", "rb"))
        pred = loaded_model.predict(df)[0]
        return JsonResponse({"pred" : int(pred)}  , status=200)

def random(request):
    if request.method == "GET":
        df = create_dataset(request)
        loaded_model = pickle.load(open("random_forest.dat", "rb"))
        pred = loaded_model.predict(df)[0]
        return JsonResponse({"pred" : int(pred)}  , status=200)

def create_dataset(request):
    features = dataset.get_features()
    features.remove("label")
    data =[[float(request.GET.get(f, 0)) for f in features]]
    df = pd.DataFrame(data, columns = features)
    return df