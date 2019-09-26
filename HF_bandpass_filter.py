from butterworth import BP_BUTTERWORTH_FILTER

def main():
    print("Introduce el orden 'N' del filtro: ")
    N = int(input());
    print("Introduce el ancho de banda % 'BW' del filtro: ")
    BW = int(input());
    print("Introduce la frecuencia central 'Fc' del filtro: ")
    fc = int(input());
    print("Introduce la resistencia del sistema 'R0' del filtro: ")
    R0 = float(input());
    
    BP_BUTTERWORTH_FILTER(N, BW/100, fc, R0)

    input()

main()
        
