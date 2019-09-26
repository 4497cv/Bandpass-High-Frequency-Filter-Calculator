from openpyxl import load_workbook
import math
wb = load_workbook(filename = 'BANDPASS.xlsx')
sheet_ranges = wb['Sheet1']

def N2_BW(order, w0, BW, system_impedance):
    g1 = sheet_ranges['B17'].value
    g2 = sheet_ranges['C17'].value
    print("Filtro Butterworth, N = %i, fuente en serie" % order)
    print(" ")
    print("1. Especificaciones del filtro ")
    print("BW = %f " % BW)
    print("r0 = %f ohm" % system_impedance)
    print("wo = 2*pi*f = %f rad/s" % w0)
    print(" ")
    print("2. Prototipo de filtro pasabajas")
    print(" ")
    print(" _______R_______________L___________  ")
    print("|               |                   | ")
    print("VDC             C                   RL")
    print("|               |                   | ")
    print("|_______________|___________________| ")
    print("                |                     ")
    print("               GND                    ")
    print(" ")
    print("g1 = C1 = %f" % g1)
    print("g2 = L1 = %f" % g2)
    print(" ")
    print("3. Escalamiento ")
    print(" ")
    print(" _______R_______________C___________  ")
    print("|               |                   | ")
    print("VDC             L                   RL")
    print("|               |                   | ")
    print("|_______________|___________________| ")
    print("                |                     ")
    print("               GND                    ")
    print(" ")
    print("g1 = L1 = %f" % g1)
    print("g2 = C1 = %f" % g2)
    print(" ")
    print("4. Conversión ")
    
    C1,L1 = LP_inductor_denormalization(system_impedance, w0, g1, BW)
    C2,L2 = LP_capacitor_denormalization(system_impedance, w0, g2, BW)
    print(" _______R__________________L2__C2____  ")
    print("|               |  |                 |  ")
    print("VDC             C1  L1               RL ")
    print("|               |  |                 |  ")
    print("|_______________|__|_________________|  ")
    print("                |                       ")
    print("               GND                      ")
    print(" ")
    print("C1 = %f nF" % (float(C1*1000000000)))
    print("L1 = %f uH" % (float(L1*1000000)))
    print(" ")
    print("C2 = %f uF" % (float(C2*1000000)))
    print("L2 = %f uH" % (float(L2*1000000)))
    print(" ")
  

def N3_BW(order, w0, BW, system_impedance):
    g1 = sheet_ranges['B18'].value
    g2 = sheet_ranges['C18'].value
    g3 = sheet_ranges['D18'].value
    
    print("Filtro Butterworth, N = %i, fuente en serie" % order)
    print(" ")      
    print("1. Especificaciones del filtro ")
    print("BW = %f " % BW)
    print("r0 = %f ohm" % system_impedance)
    print("wo = 2*pi*f = %f rad/s" % w0)
    print(" ")  
    print("2. Prototipo de filtro pasabajas")
    print(" ")  
    print(" _______R_______________L1___________  ")
    print("|               |              |     | ")
    print("VDC             C1             C2   RL")
    print("|               |              |     | ")
    print("|_______________|______________|_____| ")
    print("                |                      ")
    print("               GND                     ")
    print(" ")  
    print("g1 = C1 = %f" % g1)
    print("g2 = L1 = %f" % g2)
    print("g3 = C2 = %f" % g3)
    print(" ")  
    print("3. Escalamiento ")
    print(" ")
    print(" _______R_______________C1___________  ")
    print("|               |              |     | ")
    print("VDC             L1             L2   RL")
    print("|               |              |     | ")
    print("|_______________|______________|_____| ")
    print("                |                      ")
    print("               GND                     ")
    print(" ") 
    print("g1 = L1 = %f" % g1)
    print("g2 = C1 = %f" % g2)
    print("g3 = L1 = %f" % g3)
    print(" ")  
    print("4. Conversión ")
    print(" ")
    
    C1,L1 = LP_inductor_denormalization(system_impedance, w0, g1, BW)
    C2,L2 = LP_capacitor_denormalization(system_impedance, w0, g2, BW)
    C3,L3 = LP_inductor_denormalization(system_impedance, w0, g3, BW)
         
    print(" _______R__________________L2__C2_________________   ")
    print("|               |  |                    |   |     |  ")
    print("VDC             C1  L1                  C3  L3    RL ")
    print("|               |  |                    |   |     |  ")
    print("|_______________|__|____________________|___|_____|  ")
    print("                            |                        ")
    print("                           GND                       ")  
    print(" ")
    print("C1 = %f nF" % (float(C1*1000000000)))
    print("L1 = %f uH" % (float(L1*1000000)))
    print(" ")  
    print("C2 = %f nF" % (float(C2*1000000000)))
    print("L2 = %f uH" % (float(L2*1000000)))
    print(" ")  
    print("C3 = %f nF" % (float(C3*1000000000)))
    print("L3 = %f uH" % (float(L3*1000000)))
    
def N4_BW(order, w0, BW, system_impedance):
    g1 = sheet_ranges['B19'].value
    g2 = sheet_ranges['C19'].value
    g3 = sheet_ranges['D19'].value
    g4 = sheet_ranges['E19'].value
    
    print("Filtro Butterworth, N = %i, fuente en serie" % order)
    print(" ")      
    print("1. Especificaciones del filtro ")
    print("BW = %f " % BW)
    print("r0 = %f ohm" % system_impedance)
    print("wo = 2*pi*f = %f rad/s" % w0)
    print(" ")  
    print("2. Prototipo de filtro pasabajas")
    print(" ")  
    print(" _______R_______________L2___________L4___  ")
    print("|               |              |          | ")
    print("VDC             C1             C3        RL ")
    print("|               |              |          | ")
    print("|_______________|______________|__________| ")
    print("                     |                      ")
    print("                    GND                     ")
    print(" ")  
    print("g1 = C1 = %f" % g1)
    print("g2 = L2 = %f" % g2)
    print("g3 = C3 = %f" % g3)
    print("g4 = L4 = %f" % g4)
    print(" ")  
    print("3. Escalamiento ")
    print(" ")
    print(" _______R_______________C2___________C4___  ")
    print("|               |              |          | ")
    print("VDC             L1             L3        RL ")
    print("|               |              |          | ")
    print("|_______________|______________|__________| ")
    print("                     |                      ")
    print("                    GND                     ")
    print(" ") 
    print("g1 = L1 = %f" % g1)
    print("g2 = L3 = %f" % g2)
    print("g3 = C2 = %f" % g3)
    print("g3 = C4 = %f" % g4)
    print(" ")  
    print("4. Conversión ")
    print(" ")
    
    C1,L1 = LP_inductor_denormalization(system_impedance, w0, g1, BW)
    C2,L2 = LP_capacitor_denormalization(system_impedance, w0, g2, BW)
    C3,L3 = LP_inductor_denormalization(system_impedance, w0, g1, BW)
    C4,L4 = LP_capacitor_denormalization(system_impedance, w0, g3, BW)
         
    print(" _______R__________________L2__C2____________________L4___C4________   ")
    print("|               |  |                    |   |                       |  ")
    print("VDC             C1  L1                  C3  L3                     RL  ")
    print("|               |  |                    |   |                       |  ")
    print("|_______________|__|____________________|___|_______________________|  ")
    print("                            |                                          ")
    print("                           GND                                         ")  
    print(" ")
    print("C1 = %f nF" % (float(C1*1000000000)))
    print("L1 = %f uH" % (float(L1*1000000)))
    print(" ")  
    print("C2 = %f nF" % (float(C2*1000000000)))
    print("L2 = %f uH" % (float(L2*1000000)))
    print(" ")  
    print("C3 = %f nF" % (float(C3*1000000000)))
    print("L3 = %f uH" % (float(L3*1000000)))


def LP_inductor_denormalization(r0, w0, gk, BW):
    C = 1/(r0*w0*gk*BW)
    L = (r0*gk*BW)/(w0)
    return C, L

def LP_capacitor_denormalization(r0, w0, gk, BW):
    C = (gk*BW)/(r0*w0)
    L = (r0)/(gk*BW*w0)
    return C, L

def BP_CHEBYSHEV_3DB_FILTER(order, BW, center_freq, system_impedance):
    w0 = 2*math.pi*center_freq
    
    if(4 == order):
        N2_BW(order, w0, BW, system_impedance)
    elif(6 == order):
        N3_BW(order, w0, BW, system_impedance)
    elif(8 == order):
        N4_BW(order, w0, BW, system_impedance)
    else:
        print("invalid order (N)")

        
