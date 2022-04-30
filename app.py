from flask import Flask,render_template,request
import pickle



mymodel = pickle.load(open("rf_model",'rb'))
print(mymodel.predict([[0,2017,1,15735,2,1.4]]))
deger= ""
app = Flask(__name__)
liste = [' A1', ' A2', ' A3', ' A4', ' A5', ' A6', ' A7', ' A8', ' Q2',
       ' Q3', ' Q5', ' Q7', ' Q8', ' R8', ' RS3', ' RS4', ' RS5', ' RS6',
       ' RS7', ' S3', ' S4', ' S5', ' S8', ' SQ5', ' SQ7', ' TT']
@app.route("/",methods=['POST','GET'])
def index():
    model = request.form.get("model")
    yil = request.form.get("yil")
    transmission = request.form.get("transmission")
    mileage = request.form.get("mileage")
    fuelType = request.form.get("fuelType")
    engineSize = request.form.get("motor")
    if not model or not transmission or not yil or not mileage or not fuelType or not engineSize :
        deger = "yok"
        i=0
    else:
        deger = int(tahmin(int(model),int(yil),int(transmission),int(mileage),int(fuelType),float(engineSize)))
        i = 1
    return render_template("index.html",liste = liste, i=i, deger = deger)

if __name__ == "__main__":
    app.run(debug=True)



def tahmin(model,yil,transmission,mileage,fuelType,engineSize):
    
    deger = float(mymodel.predict([[model,yil,transmission,mileage,fuelType,engineSize]]))

    return deger