import numpy as np
import pandas as pd


def generate_sample_data():
    # Генерация случайных данных для примера
    # study_id = np.array([x for x in range(100)])
    y_true = np.random.randint(0, 2, size=100)
    y_score = np.random.rand(100)
    return y_true, y_score


test_arr = generate_sample_data()
df = pd.DataFrame(test_arr)
df = df.transpose()
df.to_excel('test_arr.xlsx')
