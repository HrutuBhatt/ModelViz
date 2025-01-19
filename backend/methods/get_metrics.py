import joblib
def get_metrics():
    svm = joblib.load(r"D:\ModelViz\backend\pkl_files\metrics_svm.pkl")
    nb = joblib.load(r"D:\ModelViz\backend\pkl_files\metrics_nb.pkl")
    lstm = joblib.load(r"D:\ModelViz\backend\pkl_files\metrics_lstm.pkl")
   
    metrics = {
        "svm": {
            "accuracy": svm["accuracy"],
            "precision": svm["precision"],
            "recall": svm["recall"],
            "f1": svm["f1"],
        },
        "nb": {
            "accuracy": nb["accuracy"],
            "precision": nb["precision"],
            "recall": nb["recall"],
            "f1": nb["f1"],
        },
        "lstm": {
            "accuracy": lstm["accuracy"],
            "precision": lstm["precision"],
            "recall": lstm["recall"],
            "f1": lstm["f1"],
        },
    }

    return metrics
    # acc_svm = svm["accuracy"]
    # prec_svm = svm["precision"]
    # rec_svm = svm["recall"]
    # f1_svm = svm["f1"]

    # acc_nb = nb["accuracy"]
    # prec_nb = nb["precision"]
    # rec_nb = nb["recall"]
    # f1_nb = nb["f1"]

    # acc_lstm = lstm["accuracy"]
    # prec_lstm = lstm["precision"]
    # rec_lstm = lstm["recall"]
    # f1_lstm = lstm["f1"]