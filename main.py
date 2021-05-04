import numpy as np
import matplotlib.pyplot as plt

t_zero, B, y = 0, 0.002, 0.5
I, R = 7, 0
t = 8

S_matrix = [0] * t
I_matrix = [0] * t
R_matrix = [0] * t


def EulerMethod():
    delta = 1
    S_matrix[t_zero] = 1000
    I_matrix[t_zero] = I
    R_matrix[t_zero] = R
    for index in range(t_zero, t - 1):
        S_matrix[index + 1] = (
            S_matrix[index] - B * I_matrix[index] * S_matrix[index] * delta
        )
        I_matrix[index + 1] = (
            I_matrix[index]
            + (B * I_matrix[index] * S_matrix[index] - y * R_matrix[index]) * delta
        )
        R_matrix[index + 1] = R_matrix[index] + y * I_matrix[index] * delta
    print(
        "Số người nhiễm bệnh tính tới tuần thứ "
        + str(t)
        + " là I["
        + str(index + 1)
        + "] = "
        + str(I_matrix[index + 1])
    )
    print(
        "Số người khỏi bệnh tính tới tuần thứ "
        + str(t)
        + " là R["
        + str(index + 1)
        + "] = "
        + str(R_matrix[index + 1])
    )
    (i,) = plt.plot([x for x in range(1, t + 1)], I_matrix)
    (r,) = plt.plot([y for y in range(1, t + 1)], R_matrix)
    plt.legend((i, r), ("Nhiễm bệnh", "Khỏi bệnh"))
    plt.title("Số người nhiễm và khỏi bệnh theo thời gian")
    plt.xlabel("Tuần ")
    plt.ylabel("Lượng người")
    plt.show()


EulerMethod()
