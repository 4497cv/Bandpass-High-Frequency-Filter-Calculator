from butterworth import BP_BUTTERWORTH_FILTER
from chebyshev_3db import BP_CHEBYSHEV_3DB_FILTER
from chebyshev_0_5db import BP_CHEBYSHEV_0_5_DB_FILTER

butterworth = 1
chebyshev_0_5db = 2
chebyshev_3db = 3

def main():
    valid = 0
    
    while(valid == 0):
            print("Elige una opción (1,2,3):")
            print("1. Butterworth ")
            print("2. Chebyshev 0.5 dB")
            print("2. Chebyshev 3.0 dB")
            select = int(input());

            if(butterworth == select):
                    print("Introduce el orden 'N' del filtro (4,6,8):")
                    N = int(input());
                    print("Introduce el ancho de banda % 'BW %' del filtro: ")
                    BW = int(input());
                    print("Introduce la frecuencia central 'f0' del filtro: ")
                    fc = int(input());
                    print("Introduce la resistencia del sistema 'R0' del filtro: ")
                    R0 = float(input());
                    BP_BUTTERWORTH_FILTER(N, BW/100, fc, R0)
                    valid = 1
            elif(chebyshev_0_5db == select):
                    print("Introduce el orden 'N' del filtro (4,6,8):")
                    N = int(input());
                    print("Introduce el ancho de banda % 'BW %' del filtro: ")
                    BW = int(input());
                    print("Introduce la frecuencia central 'f0' del filtro: ")
                    fc = int(input());
                    print("Introduce la resistencia del sistema 'R0' del filtro: ")
                    R0 = float(input());
                    BP_CHEBYSHEV_0_5_DB_FILTER(N, BW/100, fc, R0)
                    valid = 1
            elif(chebyshev_3db == select):
                    print("Introduce el orden 'N' del filtro (4,6,8):")
                    N = int(input());
                    print("Introduce el ancho de banda % 'BW %' del filtro: ")
                    BW = int(input());
                    print("Introduce la frecuencia central 'f0' del filtro: ")
                    fc = int(input());
                    print("Introduce la resistencia del sistema 'R0' del filtro: ")
                    R0 = float(input());
                    BP_CHEBYSHEV_3DB_FILTER(N, BW/100, fc, R0)
                    valid = 1
            else:
                    print("INDICE INVALIDO")
    
    print("presione cualquier tecla para salir")
    input()

main()
        
