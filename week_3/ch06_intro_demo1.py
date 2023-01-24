# module
import math as m

# print(math.sin(math.pi/2))
# print(math.sin(math.radians(90)))
print(m.sin(m.pi/2))

# math module
# func
# constant

print(
    # m.pi, m.e, type(m.inf),
    m.sin(m.pi), m.pow.__doc__, m.sqrt(2), m.log(m.e), m.log10(10)
)

# more real world examples (my experience in engineering)


# scientific computing
import numpy as np
arr = np.linspace(1,10,100)
print(arr.std())

# visualization plot
import matplotlib.pyplot as plt
# plt.plot(arr, np.sin(arr))
# plt.show()
# plt.savefig("name.tiff", dpi = 600)

# data science
import pandas as pd
df = pd.read_csv("../week_0/namelist.csv")
# print(df)

# things I want to mention
# many types of import

from math import sin
from math import *  # do not use
# cos = "passcode"
# print(cos(1))

