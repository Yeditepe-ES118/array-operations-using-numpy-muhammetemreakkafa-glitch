import numpy as np

def stat():
    data = np.loadtxt('populations.txt', skiprows=1)

    hare = data[:, 1]

    min_year_hare = data[np.argmin(hare), 0]

    lynx_avg = np.mean(data[:, 2])

    # 5. madde: satır toplamı
    row_sum = np.sum(data[:, 1:], axis=1)

    # data + yeni sütun
    new_data = np.column_stack((data, row_sum))

    # 6. madde: carrot < 40000 → 0
    new_data[new_data[:, 3] < 40000, 3] = 0

    return data, hare, min_year_hare, lynx_avg, new_data





    

