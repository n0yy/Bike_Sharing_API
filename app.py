from flask import Flask, request, render_template
from predict import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def get_predict():
    """
        Example for body:
            {
                "year": 1, -> 0/1 = 2011/2012
                "temp": 40 -> max 41
                "atemp": 41 -> max 50,
                "casual": 2108,
                "registered": 2104
            }   
    """
    data = request.get_json()
    # Normalized
    temp = data["temp"] / 41
    atemp = data["atemp"] / 50
    
    pred = predict(yr=data["year"], temp=temp, atemp=atemp, 
                   casual=data["casual"], registered=data["registered"])
    return {
        "predicted": pred
    }

if __name__ == "__main__":
    app.run()
