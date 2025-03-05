import joblib
def get_metrics():
    svm = joblib.load(r"D:\ModelViz\backend\pkl_files\metrics_svm.pkl")
    nb = joblib.load(r"D:\ModelViz\backend\pkl_files\metrics_nb.pkl")
    lstm = joblib.load(r"D:\ModelViz\backend\pkl_files\metrics_lstm.pkl")
   
    metrics = {
        "naive bayes": {
            "accuracy": nb["accuracy"],
            "precision": nb["precision"],
            "recall": nb["recall"],
            "f1": nb["f1"],
        },
        "logistic regression": {
            "accuracy": 0.95,
            "precision": 0.9923,
            "recall": 0.9090,
            "f1": 0.9923
        },
        "svm": {
            "accuracy": svm["accuracy"],
            "precision": svm["precision"],
            "recall": svm["recall"],
            "f1": svm["f1"],
        },
        "lstm": {
            "accuracy": lstm["accuracy"],
            "precision": lstm["precision"],
            "recall": lstm["recall"],
            "f1": lstm["f1"],
        },
        "hybrid" :{
            "accuracy": 0.9848,
            "precision": 1,
            "recall": 0.9058,
            "f1": 0.9505,
        }
    }

    return metrics
