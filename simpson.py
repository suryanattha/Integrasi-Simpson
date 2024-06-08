import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Implementasi Metode Integrasi Simpson 1/3
def simpson_1_3(f, a, b, N):
    if N % 2 == 1:
        N += 1  # N harus genap
    h = (b - a) / N
    integral = f(a) + f(b)
    
    for i in range(1, N):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    integral *= h / 3
    return integral

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# List untuk menyimpan hasil
results = []

# Perhitungan untuk setiap nilai N
for N in N_values:
    start_time = time.time()
    pi_approx = simpson_1_3(f, 0, 1, N)
    end_time = time.time()
    
    # Hitung galat RMS
    rms_error = np.sqrt((pi_approx - pi_ref) ** 2)
    elapsed_time = end_time - start_time
    
    # Simpan hasil
    results.append((N, pi_approx, rms_error, elapsed_time))

# Tampilkan hasil
for result in results:
    N, pi_approx, rms_error, elapsed_time = result
    print(f"N = {N}: Pi Approx = {pi_approx}, RMS Error = {rms_error}, Time = {elapsed_time:.6f} seconds")
