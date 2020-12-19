from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults,PredResults2


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        #sepal_length = float(request.POST.get('sepal_length'))
        #sepal_width = float(request.POST.get('sepal_width'))
        #petal_length = float(request.POST.get('petal_length'))
        #petal_width = float(request.POST.get('petal_width'))

        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cp = int(request.POST.get('cp'))
        trestbps = int(request.POST.get('trestbps'))
        chol = int(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        restecg = int(request.POST.get('restecg'))
        thalach = int(request.POST.get('thalach'))
        exang = int(request.POST.get('exang'))
        oldpeak = int(request.POST.get('oldpeak'))
        slope = int(request.POST.get('slope'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thal'))
        
        # Unpickle model
        model = pd.read_pickle(r"new_model.pickle")
        # Make prediction
        result = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        target = result[0]

        PredResults2.objects.create(age = age,sex=sex,cp=cp,trestbps=trestbps,chol=chol,fbs=fbs,restecg=restecg,thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal,target=target)

        return JsonResponse({'result': target, 'age': age,'sex': sex,'cp': cp,'trestbps': trestbps,'chol': chol,'fbs': fbs,'restecg': restecg,'thalach': thalach,
                            'exang': exang,'oldpeak': oldpeak,'slope': slope,'ca': ca,'thal': thal},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults2.objects.all()}
    return render(request, "results.html", data)
