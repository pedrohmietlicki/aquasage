
from sklearn.preprocessing import MinMaxScaler
from keras import Sequential, Input
from keras.api.layers import LSTM, Dense
import pandas as pd
import numpy as np
import os
os.environ["THEANO_FLAGS"] = "mode=FAST_RUN,device=cpu,floatX=float32"


data = {
    "2024-12-03 00:00": 1.55,
    "2024-12-03 00:15": 1.55,
    "2024-12-03 00:30": 1.54,
    "2024-12-03 00:45": 1.54,
    "2024-12-03 01:00": 1.53,
    "2024-12-03 01:15": 1.52,
    "2024-12-03 01:30": 1.52,
    "2024-12-03 01:45": 1.51,
    "2024-12-03 02:00": 1.51,
    "2024-12-03 02:15": 1.5,
    "2024-12-03 02:30": 1.5,
    "2024-12-03 02:45": 1.5,
    "2024-12-03 03:00": 1.5,
    "2024-12-03 03:15": 1.49,
    "2024-12-03 03:30": 1.49,
    "2024-12-03 03:45": 1.49,
    "2024-12-03 04:00": 1.48,
    "2024-12-03 04:15": 1.48,
    "2024-12-03 04:30": 1.48,
    "2024-12-03 04:45": 1.48,
    "2024-12-03 05:00": 1.48,
    "2024-12-03 05:15": 1.47,
    "2024-12-03 05:30": 1.47,
    "2024-12-03 05:45": 1.47,
    "2024-12-03 06:00": 1.47,
    "2024-12-03 06:15": 1.47,
    "2024-12-03 06:30": 1.48,
    "2024-12-03 06:45": 1.48,
    "2024-12-03 07:00": 1.49,
    "2024-12-03 07:15": 1.5,
    "2024-12-03 07:30": 1.5,
    "2024-12-03 07:45": 1.51,
    "2024-12-03 08:00": 1.51,
    "2024-12-03 08:15": 1.52,
    "2024-12-03 08:30": 1.52,
    "2024-12-03 08:45": 1.52,
    "2024-12-03 09:00": 1.53,
    "2024-12-03 09:15": 1.53,
    "2024-12-03 09:30": 1.53,
    "2024-12-03 09:45": 1.53,
    "2024-12-03 10:00": 1.54,
    "2024-12-03 10:15": 1.54,
    "2024-12-03 10:30": 1.55,
    "2024-12-03 10:45": 1.55,
    "2024-12-03 11:00": 1.55,
    "2024-12-03 11:15": 1.56,
    "2024-12-03 11:30": 1.56,
    "2024-12-03 11:45": 1.56,
    "2024-12-03 12:00": 1.57,
    "2024-12-03 12:15": 1.57,
    "2024-12-03 12:30": 1.58,
    "2024-12-03 12:45": 1.59,
    "2024-12-03 13:00": 1.6,
    "2024-12-03 13:15": 1.6,
    "2024-12-03 13:30": 1.61,
    "2024-12-03 13:45": 1.63,
    "2024-12-03 14:00": 1.64,
    "2024-12-03 14:15": 1.65,
    "2024-12-03 14:30": 1.66,
    "2024-12-03 14:45": 1.67,
    "2024-12-03 15:00": 1.68,
    "2024-12-03 15:15": 1.69,
    "2024-12-03 15:30": 1.7,
    "2024-12-03 15:45": 1.71,
    "2024-12-03 16:00": 1.71,
    "2024-12-03 16:15": 1.72,
    "2024-12-03 16:30": 1.73,
    "2024-12-03 16:45": 1.74,
    "2024-12-03 17:00": 1.75,
    "2024-12-03 17:15": 1.75,
    "2024-12-03 17:30": 1.76,
    "2024-12-03 17:45": 1.77,
    "2024-12-03 18:00": 1.78,
    "2024-12-03 18:15": 1.78,
    "2024-12-03 18:30": 1.8,
    "2024-12-03 18:45": 1.79,
    "2024-12-03 19:00": 1.81,
    "2024-12-03 19:15": 1.81,
    "2024-12-03 19:30": 1.82,
    "2024-12-03 19:45": 1.82,
    "2024-12-03 20:00": 1.83,
    "2024-12-03 20:15": 1.83,
    "2024-12-03 20:30": 1.83,
    "2024-12-03 20:45": 1.84,
    "2024-12-03 21:00": 1.85,
    "2024-12-03 21:15": 1.86,
    "2024-12-03 21:30": 1.87,
    "2024-12-03 21:45": 1.87,
    "2024-12-03 22:00": 1.86,
    "2024-12-03 22:15": 1.86,
    "2024-12-03 22:30": 1.87,
    "2024-12-03 22:45": 1.86,
    "2024-12-03 23:00": 1.85,
    "2024-12-03 23:15": 1.85,
    "2024-12-03 23:30": 1.85,
    "2024-12-03 23:45": 1.84,
    "2024-12-04 00:00": 1.84,
    "2024-12-04 00:15": 1.83,
    "2024-12-04 00:30": 1.83,
    "2024-12-04 00:45": 1.82,
    "2024-12-04 01:00": 1.82,
    "2024-12-04 01:15": 1.82,
    "2024-12-04 01:30": 1.81,
    "2024-12-04 01:45": 1.81,
    "2024-12-04 02:00": 1.8,
    "2024-12-04 02:15": 1.79,
    "2024-12-04 02:30": 1.79,
    "2024-12-04 02:45": 1.79,
    "2024-12-04 03:00": 1.78,
    "2024-12-04 03:15": 1.77,
    "2024-12-04 03:30": 1.77,
    "2024-12-04 03:45": 1.76,
    "2024-12-04 04:00": 1.75,
    "2024-12-04 04:15": 1.75,
    "2024-12-04 04:30": 1.75,
    "2024-12-04 04:45": 1.74,
    "2024-12-04 05:00": 1.73,
    "2024-12-04 05:15": 1.73,
    "2024-12-04 05:30": 1.72,
    "2024-12-04 05:45": 1.72,
    "2024-12-04 06:00": 1.71,
    "2024-12-04 06:15": 1.71,
    "2024-12-04 06:30": 1.7,
    "2024-12-04 06:45": 1.7,
    "2024-12-04 07:00": 1.69,
    "2024-12-04 07:15": 1.69,
    "2024-12-04 07:30": 1.68,
    "2024-12-04 07:45": 1.68,
    "2024-12-04 08:00": 1.68,
    "2024-12-04 08:15": 1.67,
    "2024-12-04 08:30": 1.66,
    "2024-12-04 08:45": 1.65,
    "2024-12-04 09:00": 1.65,
    "2024-12-04 09:15": 1.64,
    "2024-12-04 09:30": 1.64,
    "2024-12-04 09:45": 1.63,
    "2024-12-04 10:00": 1.62,
    "2024-12-04 10:15": 1.62,
    "2024-12-04 10:30": 1.62,
    "2024-12-04 10:45": 1.61,
    "2024-12-04 11:00": 1.61,
    "2024-12-04 11:15": 1.61,
    "2024-12-04 11:30": 1.61,
    "2024-12-04 11:45": 1.61,
    "2024-12-04 12:00": 1.61,
    "2024-12-04 12:15": 1.61,
    "2024-12-04 12:30": 1.61,
    "2024-12-04 12:45": 1.61,
    "2024-12-04 13:00": 1.62,
    "2024-12-04 13:15": 1.63,
    "2024-12-04 13:30": 1.62,
    "2024-12-04 13:45": 1.63,
    "2024-12-04 14:00": 1.63,
    "2024-12-04 14:15": 1.64,
    "2024-12-04 14:30": 1.64,
    "2024-12-04 14:45": 1.64,
    "2024-12-04 15:00": 1.64,
    "2024-12-04 15:15": 1.65,
    "2024-12-04 15:30": 1.65,
    "2024-12-04 15:45": 1.66,
    "2024-12-04 16:00": 1.66,
    "2024-12-04 16:15": 1.67,
    "2024-12-04 16:30": 1.67,
    "2024-12-04 16:45": 1.67,
    "2024-12-04 17:00": 1.67,
    "2024-12-04 17:15": 1.67,
    "2024-12-04 17:30": 1.67,
    "2024-12-04 17:45": 1.67,
    "2024-12-04 18:00": 1.67,
    "2024-12-04 18:15": 1.68,
    "2024-12-04 18:30": 1.68,
    "2024-12-04 18:45": 1.69,
    "2024-12-04 19:00": 1.69,
    "2024-12-04 19:15": 1.7,
    "2024-12-04 19:30": 1.71,
    "2024-12-04 19:45": 1.71,
    "2024-12-04 20:00": 1.71,
    "2024-12-04 20:15": 1.71,
    "2024-12-04 20:30": 1.71,
    "2024-12-04 20:45": 1.72,
    "2024-12-04 21:00": 1.72,
    "2024-12-04 21:15": 1.72,
    "2024-12-04 21:30": 1.71,
    "2024-12-04 21:45": 1.71,
    "2024-12-04 22:00": 1.71,
    "2024-12-04 22:15": 1.7,
    "2024-12-04 22:30": 1.7,
    "2024-12-04 22:45": 1.7,
    "2024-12-04 23:00": 1.69,
    "2024-12-04 23:15": 1.68,
    "2024-12-04 23:30": 1.68,
    "2024-12-04 23:45": 1.67,
    "2024-12-05 00:00": 1.66,
    "2024-12-05 00:15": 1.66,
    "2024-12-05 00:30": 1.65,
    "2024-12-05 00:45": 1.64,
    "2024-12-05 01:00": 1.63,
    "2024-12-05 01:15": 1.63,
    "2024-12-05 01:30": 1.62,
    "2024-12-05 01:45": 1.62,
    "2024-12-05 02:00": 1.61,
    "2024-12-05 02:15": 1.6,
    "2024-12-05 02:30": 1.6,
    "2024-12-05 02:45": 1.59,
    "2024-12-05 03:00": 1.58,
    "2024-12-05 03:15": 1.58,
    "2024-12-05 03:30": 1.57,
    "2024-12-05 03:45": 1.56,
    "2024-12-05 04:00": 1.56,
    "2024-12-05 04:15": 1.55,
    "2024-12-05 04:30": 1.55,
    "2024-12-05 04:45": 1.54,
    "2024-12-05 05:00": 1.53,
    "2024-12-05 05:15": 1.53,
    "2024-12-05 05:30": 1.52,
    "2024-12-05 05:45": 1.52,
    "2024-12-05 06:00": 1.51,
    "2024-12-05 06:15": 1.51,
    "2024-12-05 06:30": 1.5,
    "2024-12-05 06:45": 1.5,
    "2024-12-05 07:00": 1.5,
    "2024-12-05 07:15": 1.5,
    "2024-12-05 07:30": 1.5,
    "2024-12-05 07:45": 1.49,
    "2024-12-05 08:00": 1.5,
    "2024-12-05 08:15": 1.5,
    "2024-12-05 08:30": 1.5,
    "2024-12-05 08:45": 1.5,
    "2024-12-05 09:00": 1.5,
    "2024-12-05 09:15": 1.51,
    "2024-12-05 09:30": 1.51,
    "2024-12-05 09:45": 1.52,
    "2024-12-05 10:00": 1.52,
    "2024-12-05 10:15": 1.53,
    "2024-12-05 10:30": 1.54,
    "2024-12-05 10:45": 1.54,
    "2024-12-05 11:00": 1.54,
    "2024-12-05 11:15": 1.55,
    "2024-12-05 11:30": 1.54,
    "2024-12-05 11:45": 1.54,
    "2024-12-05 12:00": 1.54,
    "2024-12-05 12:15": 1.55,
    "2024-12-05 12:30": 1.56,
    "2024-12-05 12:45": 1.56,
    "2024-12-05 13:00": 1.56,
    "2024-12-05 13:15": 1.57,
    "2024-12-05 13:30": 1.57,
    "2024-12-05 13:45": 1.58,
    "2024-12-05 14:00": 1.58,
    "2024-12-05 14:15": 1.58,
    "2024-12-05 14:30": 1.59,
    "2024-12-05 14:45": 1.59,
    "2024-12-05 15:00": 1.59,
    "2024-12-05 15:15": 1.6,
    "2024-12-05 15:30": 1.6,
    "2024-12-05 15:45": 1.61,
    "2024-12-05 16:00": 1.62,
    "2024-12-05 16:15": 1.63,
    "2024-12-05 16:30": 1.64,
    "2024-12-05 16:45": 1.66,
    "2024-12-05 17:00": 1.67,
    "2024-12-05 17:15": 1.68,
    "2024-12-05 17:30": 1.68,
    "2024-12-05 17:45": 1.68,
    "2024-12-05 18:00": 1.68,
    "2024-12-05 18:15": 1.68,
    "2024-12-05 18:30": 1.67,
    "2024-12-05 18:45": 1.67,
    "2024-12-05 19:00": 1.67,
    "2024-12-05 19:15": 1.66,
    "2024-12-05 19:30": 1.65,
    "2024-12-05 19:45": 1.65,
    "2024-12-05 20:00": 1.65,
    "2024-12-05 20:15": 1.65,
    "2024-12-05 20:30": 1.65,
    "2024-12-05 20:45": 1.65,
    "2024-12-05 21:00": 1.65,
    "2024-12-05 21:15": 1.64,
    "2024-12-05 21:30": 1.63,
    "2024-12-05 21:45": 1.63,
    "2024-12-05 22:00": 1.62,
    "2024-12-05 22:15": 1.62,
    "2024-12-05 23:30": 1.6,
    "2024-12-05 23:45": 1.59,
    "2024-12-06 00:00": 1.59,
    "2024-12-06 00:15": 1.58,
    "2024-12-06 00:30": 1.57,
    "2024-12-06 00:45": 1.57,
    "2024-12-06 01:00": 1.56,
    "2024-12-06 01:15": 1.56,
    "2024-12-06 01:30": 1.55,
    "2024-12-06 01:45": 1.54,
    "2024-12-06 02:00": 1.54,
    "2024-12-06 02:15": 1.53,
    "2024-12-06 02:30": 1.53,
    "2024-12-06 02:45": 1.52,
    "2024-12-06 03:00": 1.52,
    "2024-12-06 03:15": 1.51,
    "2024-12-06 03:30": 1.51,
    "2024-12-06 03:45": 1.51,
    "2024-12-06 04:00": 1.5,
    "2024-12-06 04:15": 1.49,
    "2024-12-06 04:30": 1.49,
    "2024-12-06 04:45": 1.48,
    "2024-12-06 05:00": 1.48,
    "2024-12-06 05:15": 1.47,
    "2024-12-06 05:30": 1.47,
    "2024-12-06 05:45": 1.47,
    "2024-12-06 06:00": 1.47,
    "2024-12-06 06:15": 1.46,
    "2024-12-06 06:30": 1.46,
    "2024-12-06 06:45": 1.46,
    "2024-12-06 07:00": 1.45,
    "2024-12-06 07:15": 1.45,
    "2024-12-06 07:30": 1.44,
    "2024-12-06 07:45": 1.43,
    "2024-12-06 08:00": 1.43,
    "2024-12-06 08:15": 1.43,
    "2024-12-06 08:30": 1.42,
    "2024-12-06 08:45": 1.42,
    "2024-12-06 09:00": 1.41,
    "2024-12-06 09:15": 1.41,
    "2024-12-06 09:30": 1.41,
    "2024-12-06 09:45": 1.4,
    "2024-12-06 10:00": 1.4,
    "2024-12-06 10:15": 1.4,
    "2024-12-06 10:30": 1.41,
    "2024-12-06 10:45": 1.41,
    "2024-12-06 11:00": 1.4,
    "2024-12-06 11:15": 1.4,
    "2024-12-06 11:30": 1.41,
    "2024-12-06 11:45": 1.4,
    "2024-12-06 12:00": 1.4,
    "2024-12-06 12:15": 1.38,
    "2024-12-06 12:30": 1.37,
    "2024-12-06 12:45": 1.36,
    "2024-12-06 13:00": 1.35,
    "2024-12-06 13:15": 1.35,
    "2024-12-06 13:30": 1.34,
    "2024-12-06 13:45": 1.34,
    "2024-12-06 14:00": 1.33,
    "2024-12-06 14:15": 1.33,
    "2024-12-06 14:30": 1.4,
    "2024-12-06 14:45": 1.39,
    "2024-12-06 15:00": 1.35,
    "2024-12-06 15:15": 1.39,
    "2024-12-06 15:30": 1.4,
    "2024-12-06 15:45": 1.38,
    "2024-12-06 16:00": 1.33,
    "2024-12-06 16:15": 1.34,
    "2024-12-06 16:30": 1.35,
    "2024-12-06 16:45": 1.35,
    "2024-12-06 17:00": 1.36,
    "2024-12-06 17:15": 1.38,
    "2024-12-06 17:30": 1.38,
    "2024-12-06 17:45": 1.36,
    "2024-12-06 18:00": 1.35,
    "2024-12-06 18:15": 1.36,
    "2024-12-06 18:30": 1.37,
    "2024-12-06 18:45": 1.37,
    "2024-12-06 19:00": 1.38,
    "2024-12-06 19:15": 1.4,
    "2024-12-06 19:30": 1.41,
    "2024-12-06 19:45": 1.41,
    "2024-12-06 20:00": 1.4,
    "2024-12-06 20:15": 1.4,
    "2024-12-06 20:30": 1.4,
    "2024-12-06 20:45": 1.41,
    "2024-12-06 21:00": 1.44,
    "2024-12-06 21:15": 1.45,
    "2024-12-06 21:30": 1.47,
    "2024-12-06 21:45": 1.49,
    "2024-12-06 22:00": 1.51,
    "2024-12-06 22:15": 1.52,
    "2024-12-06 22:30": 1.53,
    "2024-12-06 22:45": 1.54,
    "2024-12-06 23:00": 1.56,
    "2024-12-06 23:15": 1.57,
    "2024-12-06 23:30": 1.57,
    "2024-12-06 23:45": 1.57,
    "2024-12-07 00:00": 1.59,
    "2024-12-07 00:15": 1.6,
    "2024-12-07 00:30": 1.59,
    "2024-12-07 00:45": 1.61,
    "2024-12-07 01:00": 1.62,
    "2024-12-07 01:15": 1.63,
    "2024-12-07 01:30": 1.65,
    "2024-12-07 01:45": 1.65,
    "2024-12-07 02:00": 1.67,
    "2024-12-07 02:15": 1.67,
    "2024-12-07 02:30": 1.69,
    "2024-12-07 02:45": 1.7,
    "2024-12-07 03:00": 1.71,
    "2024-12-07 03:15": 1.71,
    "2024-12-07 03:30": 1.72,
    "2024-12-07 03:45": 1.73,
    "2024-12-07 04:00": 1.74,
    "2024-12-07 04:15": 1.75,
    "2024-12-07 04:30": 1.76,
    "2024-12-07 04:45": 1.77,
    "2024-12-07 05:00": 1.78,
    "2024-12-07 05:15": 1.78,
    "2024-12-07 05:30": 1.79,
    "2024-12-07 05:45": 1.8,
    "2024-12-07 06:00": 1.8,
    "2024-12-07 06:15": 1.8,
    "2024-12-07 06:30": 1.8,
    "2024-12-07 06:45": 1.79,
    "2024-12-07 07:00": 1.79,
    "2024-12-07 07:15": 1.79,
    "2024-12-07 07:30": 1.79,
    "2024-12-07 07:45": 1.79,
    "2024-12-07 08:00": 1.78,
    "2024-12-07 08:15": 1.78,
    "2024-12-07 08:30": 1.78,
    "2024-12-07 08:45": 1.78,
    "2024-12-07 09:00": 1.78,
    "2024-12-07 09:15": 1.78,
    "2024-12-07 09:30": 1.77,
    "2024-12-07 09:45": 1.77,
    "2024-12-07 10:00": 1.77,
    "2024-12-07 10:15": 1.77,
    "2024-12-07 10:30": 1.77,
    "2024-12-07 10:45": 1.77,
    "2024-12-07 11:00": 1.78,
    "2024-12-07 11:15": 1.78,
    "2024-12-07 11:30": 1.78,
    "2024-12-07 11:45": 1.78,
    "2024-12-07 12:00": 1.77,
    "2024-12-07 12:15": 1.78,
    "2024-12-07 12:30": 1.78,
    "2024-12-07 12:45": 1.77,
    "2024-12-07 13:00": 1.78,
    "2024-12-07 13:15": 1.77,
    "2024-12-07 13:30": 1.77,
    "2024-12-07 13:45": 1.77,
    "2024-12-07 14:00": 1.76,
    "2024-12-07 14:15": 1.76,
    "2024-12-07 14:30": 1.75,
    "2024-12-07 14:45": 1.75,
    "2024-12-07 15:00": 1.75,
    "2024-12-07 15:15": 1.76,
    "2024-12-07 15:30": 1.76,
    "2024-12-07 15:45": 1.76,
    "2024-12-07 16:00": 1.75,
    "2024-12-07 16:15": 1.75,
    "2024-12-07 16:30": 1.75,
    "2024-12-07 16:45": 1.76,
    "2024-12-07 17:00": 1.77,
    "2024-12-07 17:15": 1.78,
    "2024-12-07 17:30": 1.78,
    "2024-12-07 17:45": 1.78,
    "2024-12-07 18:00": 1.8,
    "2024-12-07 18:15": 1.8,
    "2024-12-07 18:30": 1.8,
    "2024-12-07 18:45": 1.81,
    "2024-12-07 19:00": 1.81,
    "2024-12-07 19:15": 1.82,
    "2024-12-07 19:30": 1.83,
    "2024-12-07 19:45": 1.84,
    "2024-12-07 20:00": 1.84,
    "2024-12-07 20:15": 1.84,
    "2024-12-07 20:30": 1.86,
    "2024-12-07 20:45": 1.85,
    "2024-12-07 21:00": 1.86,
    "2024-12-07 21:15": 1.87,
    "2024-12-07 21:30": 1.87,
    "2024-12-07 21:45": 1.87,
    "2024-12-07 22:00": 1.87,
    "2024-12-07 22:15": 1.87,
    "2024-12-07 22:30": 1.87,
    "2024-12-07 22:45": 1.88,
    "2024-12-07 23:00": 1.88,
    "2024-12-07 23:15": 1.89,
    "2024-12-07 23:30": 1.89,
    "2024-12-07 23:45": 1.88,
    "2024-12-08 00:00": 1.88,
    "2024-12-08 00:15": 1.88,
    "2024-12-08 00:30": 1.88,
    "2024-12-08 00:45": 1.88,
    "2024-12-08 01:00": 1.88,
    "2024-12-08 01:15": 1.88,
    "2024-12-08 01:30": 1.88,
    "2024-12-08 01:45": 1.89,
    "2024-12-08 02:00": 1.88,
    "2024-12-08 02:15": 1.89,
    "2024-12-08 02:30": 1.89,
    "2024-12-08 02:45": 1.89,
    "2024-12-08 03:00": 1.89,
    "2024-12-08 03:15": 1.9,
    "2024-12-08 03:30": 1.9,
    "2024-12-08 03:45": 1.9,
    "2024-12-08 04:00": 1.89,
    "2024-12-08 04:15": 1.9,
    "2024-12-08 04:30": 1.89,
    "2024-12-08 04:45": 1.89,
    "2024-12-08 05:00": 1.89,
    "2024-12-08 05:15": 1.89,
    "2024-12-08 05:30": 1.89,
    "2024-12-08 05:45": 1.89,
    "2024-12-08 06:00": 1.9,
    "2024-12-08 06:15": 1.89,
    "2024-12-08 06:30": 1.89,
    "2024-12-08 06:45": 1.9,
    "2024-12-08 07:00": 1.89,
    "2024-12-08 07:15": 1.89,
    "2024-12-08 07:30": 1.89,
    "2024-12-08 07:45": 1.9,
    "2024-12-08 08:00": 1.9,
    "2024-12-08 08:15": 1.89,
    "2024-12-08 08:30": 1.89,
    "2024-12-08 08:45": 1.9,
    "2024-12-08 09:00": 1.89,
    "2024-12-08 09:15": 1.9,
    "2024-12-08 09:30": 1.89,
    "2024-12-08 09:45": 1.89,
    "2024-12-08 10:00": 1.89,
    "2024-12-08 10:15": 1.9,
    "2024-12-08 10:30": 1.9,
    "2024-12-08 10:45": 1.9,
    "2024-12-08 11:00": 1.91,
    "2024-12-08 11:15": 1.9,
    "2024-12-08 11:30": 1.9,
    "2024-12-08 11:45": 1.89,
    "2024-12-08 12:00": 1.89,
    "2024-12-08 12:15": 1.89,
    "2024-12-08 12:30": 1.89,
    "2024-12-08 12:45": 1.88,
    "2024-12-08 13:00": 1.87,
    "2024-12-08 13:15": 1.86,
    "2024-12-08 13:30": 1.86,
    "2024-12-08 13:45": 1.86,
    "2024-12-08 14:00": 1.84,
    "2024-12-08 14:15": 1.84,
    "2024-12-08 14:30": 1.84,
    "2024-12-08 14:45": 1.83,
    "2024-12-08 15:00": 1.84,
    "2024-12-08 15:15": 1.83,
    "2024-12-08 15:30": 1.83,
    "2024-12-08 15:45": 1.83,
    "2024-12-08 16:00": 1.81,
    "2024-12-08 16:15": 1.82,
    "2024-12-08 16:30": 1.82,
    "2024-12-08 16:45": 1.81,
    "2024-12-08 17:00": 1.81,
    "2024-12-08 17:15": 1.81,
    "2024-12-08 17:30": 1.81,
    "2024-12-08 17:45": 1.8,
    "2024-12-08 18:00": 1.8,
    "2024-12-08 18:15": 1.8,
    "2024-12-08 18:30": 1.8,
    "2024-12-08 18:45": 1.79,
    "2024-12-08 19:00": 1.78,
    "2024-12-08 19:15": 1.78,
    "2024-12-08 19:30": 1.78,
    "2024-12-08 19:45": 1.77,
    "2024-12-08 20:00": 1.77,
    "2024-12-08 20:15": 1.76,
    "2024-12-08 20:30": 1.76,
    "2024-12-08 20:45": 1.75,
    "2024-12-08 21:00": 1.75,
    "2024-12-08 21:15": 1.74,
    "2024-12-08 21:30": 1.73,
    "2024-12-08 21:45": 1.73,
    "2024-12-08 22:00": 1.73,
    "2024-12-08 22:15": 1.73,
    "2024-12-08 22:30": 1.73,
    "2024-12-08 22:45": 1.73,
    "2024-12-08 23:00": 1.73,
    "2024-12-08 23:15": 1.73,
    "2024-12-08 23:30": 1.74,
    "2024-12-08 23:45": 1.74,
    "2024-12-09 00:00": 1.74,
    "2024-12-09 00:15": 1.74,
    "2024-12-09 00:30": 1.74,
    "2024-12-09 00:45": 1.75,
    "2024-12-09 01:00": 1.76,
    "2024-12-09 01:15": 1.76,
    "2024-12-09 01:30": 1.77,
    "2024-12-09 01:45": 1.77,
    "2024-12-09 02:00": 1.78,
    "2024-12-09 02:15": 1.78,
    "2024-12-09 02:30": 1.78,
    "2024-12-09 02:45": 1.79,
    "2024-12-09 03:00": 1.79,
    "2024-12-09 03:15": 1.79,
    "2024-12-09 03:30": 1.79,
    "2024-12-09 03:45": 1.79,
    "2024-12-09 04:00": 1.79,
    "2024-12-09 04:15": 1.8,
    "2024-12-09 04:30": 1.79,
    "2024-12-09 04:45": 1.79,
    "2024-12-09 05:00": 1.79,
    "2024-12-09 05:15": 1.79,
    "2024-12-09 05:30": 1.79,
    "2024-12-09 05:45": 1.78,
    "2024-12-09 06:00": 1.78,
    "2024-12-09 06:15": 1.78,
    "2024-12-09 06:30": 1.78,
    "2024-12-09 06:45": 1.78,
    "2024-12-09 07:00": 1.78,
    "2024-12-09 07:15": 1.78,
    "2024-12-09 07:30": 1.78,
    "2024-12-09 07:45": 1.78,
    "2024-12-09 08:00": 1.78,
    "2024-12-09 08:15": 1.78,
    "2024-12-09 08:30": 1.78,
    "2024-12-09 08:45": 1.79,
    "2024-12-09 09:00": 1.79,
    "2024-12-09 09:15": 1.79,
    "2024-12-09 09:30": 1.79,
    "2024-12-09 09:45": 1.79,
    "2024-12-09 10:00": 1.79,
    "2024-12-09 10:15": 1.79,
    "2024-12-09 10:30": 1.79,
    "2024-12-09 10:45": 1.79,
    "2024-12-09 11:00": 1.79,
    "2024-12-09 11:15": 1.78,
    "2024-12-09 11:30": 1.78,
    "2024-12-09 11:45": 1.77,
    "2024-12-09 12:00": 1.78,
    "2024-12-09 12:15": 1.77,
    "2024-12-09 12:30": 1.77,
    "2024-12-09 12:45": 1.78,
    "2024-12-09 13:00": 1.78,
    "2024-12-09 13:15": 1.78,
    "2024-12-09 13:30": 1.78,
    "2024-12-09 13:45": 1.78,
    "2024-12-09 14:00": 1.77,
    "2024-12-09 14:15": 1.77,
    "2024-12-09 14:30": 1.76,
    "2024-12-09 14:45": 1.76,
    "2024-12-09 15:00": 1.77,
    "2024-12-09 15:15": 1.77,
    "2024-12-09 15:30": 1.78,
    "2024-12-09 15:45": 1.78,
    "2024-12-09 16:00": 1.77,
    "2024-12-09 16:15": 1.77,
    "2024-12-09 16:30": 1.78,
    "2024-12-09 16:45": 1.78,
    "2024-12-09 17:00": 1.77,
    "2024-12-09 17:15": 1.77,
    "2024-12-09 17:30": 1.77,
    "2024-12-09 17:45": 1.76,
    "2024-12-09 18:00": 1.77,
    "2024-12-09 18:15": 1.77,
    "2024-12-09 18:30": 1.76,
    "2024-12-09 18:45": 1.76,
    "2024-12-09 19:00": 1.76,
    "2024-12-09 19:15": 1.76,
    "2024-12-09 19:30": 1.75,
    "2024-12-09 19:45": 1.75,
    "2024-12-09 20:00": 1.75,
    "2024-12-09 20:15": 1.74,
    "2024-12-09 20:30": 1.74,
    "2024-12-09 20:45": 1.74,
    "2024-12-09 21:00": 1.74,
    "2024-12-09 21:15": 1.73,
    "2024-12-09 21:30": 1.72,
    "2024-12-09 21:45": 1.71,
    "2024-12-09 22:00": 1.71,
    "2024-12-09 22:15": 1.71,
    "2024-12-09 22:30": 1.71,
    "2024-12-09 22:45": 1.71,
    "2024-12-09 23:00": 1.71,
    "2024-12-09 23:15": 1.7,
    "2024-12-09 23:30": 1.7,
    "2024-12-09 23:45": 1.69,
    "2024-12-10 00:00": 1.69,
    "2024-12-10 00:15": 1.69,
    "2024-12-10 00:30": 1.68,
    "2024-12-10 00:45": 1.68,
    "2024-12-10 01:00": 1.67,
    "2024-12-10 01:15": 1.67,
    "2024-12-10 01:30": 1.66,
    "2024-12-10 01:45": 1.65,
    "2024-12-10 02:00": 1.65,
    "2024-12-10 02:15": 1.65,
    "2024-12-10 02:30": 1.64,
    "2024-12-10 02:45": 1.64,
    "2024-12-10 03:00": 1.64,
    "2024-12-10 03:15": 1.64,
    "2024-12-10 03:30": 1.63,
    "2024-12-10 03:45": 1.63,
    "2024-12-10 04:00": 1.63,
    "2024-12-10 04:15": 1.63,
    "2024-12-10 04:30": 1.62,
    "2024-12-10 04:45": 1.62,
    "2024-12-10 05:00": 1.62,
    "2024-12-10 05:15": 1.61,
    "2024-12-10 05:30": 1.61,
    "2024-12-10 05:45": 1.61,
    "2024-12-10 06:00": 1.61,
    "2024-12-10 06:15": 1.6,
    "2024-12-10 06:30": 1.6,
    "2024-12-10 06:45": 1.6,
    "2024-12-10 07:00": 1.6,
    "2024-12-10 07:15": 1.6,
    "2024-12-10 07:30": 1.6,
    "2024-12-10 07:45": 1.6,
    "2024-12-10 08:00": 1.6,
    "2024-12-10 08:15": 1.61,
    "2024-12-10 08:30": 1.6,
    "2024-12-10 08:45": 1.6,
    "2024-12-10 09:00": 1.6,
    "2024-12-10 09:15": 1.6,
    "2024-12-10 09:30": 1.6,
    "2024-12-10 09:45": 1.61,
    "2024-12-10 10:00": 1.61,
    "2024-12-10 10:15": 1.61,
    "2024-12-10 10:30": 1.62,
    "2024-12-10 10:45": 1.61,
    "2024-12-10 11:00": 1.62,
    "2024-12-10 11:15": 1.63,
    "2024-12-10 11:30": 1.63,
    "2024-12-10 11:45": 1.64,
    "2024-12-10 12:00": 1.64,
    "2024-12-10 12:15": 1.65,
    "2024-12-10 12:30": 1.65,
    "2024-12-10 12:45": 1.66,
    "2024-12-10 13:00": 1.66,
    "2024-12-10 13:15": 1.67,
    "2024-12-10 13:30": 1.67,
    "2024-12-10 13:45": 1.68,
    "2024-12-10 14:00": 1.68,
    "2024-12-10 14:15": 1.68,
    "2024-12-10 14:30": 1.69,
    "2024-12-10 14:45": 1.69,
    "2024-12-10 15:00": 1.69,
    "2024-12-10 15:15": 1.69,
    "2024-12-10 15:30": 1.69,
    "2024-12-10 15:45": 1.7,
    "2024-12-10 16:00": 1.7,
    "2024-12-10 16:15": 1.7
}
river_level = []
for timestamp, value in data.items():
       river_level.append(value)
print(len(river_level))      
dataset = pd.DataFrame(river_level, columns=['Levels'])
scaler  = MinMaxScaler(feature_range=(0, 1))
dataset_scaled = scaler.fit_transform(dataset)

# Função para criar a matriz de dados com timesteps
def create_dataset(data, timesteps=3):
    X, y = [], []
    for i in range(len(data) - timesteps):
        X.append(data[i:i + timesteps, 0])
        y.append(data[i + timesteps, 0])
    return np.array(X), np.array(y)

# Parâmetros
timesteps = 3  # Número de valores anteriores a usar
features = 1   # Número de variáveis independentes

# Cria os dados de treino e teste
train_size = int(len(dataset_scaled) * 0.67)
train_data = dataset_scaled[:train_size]
test_data = dataset_scaled[train_size:]

# Cria os conjuntos de treino e teste

X_train, y_train = create_dataset(train_data, timesteps)
X_test, y_test = create_dataset(test_data, timesteps)
# print(X_train)

# Ajusta o formato para LSTM
X_train = X_train.reshape((X_train.shape[0], timesteps, features))
X_test = X_test.reshape((X_test.shape[0], timesteps, features))

# Define o modelo LSTM
model = Sequential()
model.add(LSTM(units=50, input_shape=(timesteps, features)))
model.add(Dense(1))
model.compile(loss="mean_squared_error", optimizer="adam")

# Treinamento do modelo
model.fit(X_train, y_train, epochs=20, batch_size=1, verbose=2)

# Avaliação do modelo
loss = model.evaluate(X_test, y_test, verbose=0)
print(f"Loss no conjunto de teste: {loss}")

model.save("weights.h5")

# Faz previsões
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)  # Reverte a normalização
print(len(predictions))