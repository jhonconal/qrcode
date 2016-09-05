# -*- coding: utf-8 -*-

from mylibs import data, ECC, structure, matrix, draw

supported_chars = r'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ·,.:;+-*/\~!@#$%^&`[]()?_{}|'

# ver: Version (from 1 to 40)
# ecl: Error Correction Level (L,M,Q,H)
# get a qrcode picture of 3*3 pixels per module
def get_qrcode(ver, ecl, str, save_place):
    # ver == 0: default that is depending on str and ecl
    if ver not in range(41):
        print('WARNING: Version Error! Please choose a version from 1 to 40!')
    if ecl not in 'LMQH':
        print('WARNING: Level Error! Please choose one of L,M,Q,H!')
    if any(i not in supported_chars for i in str):
        print('WARNING: Input Error! Please read the README file for the supported characters!!')
    else:
        # Data Coding
        ver, data_codewords = data.encode(ver, ecl, str)

        # Error Correction Coding
        ecc = ECC.encode(ver, ecl, data_codewords)
        
        # Structure final bits
        final_bits = structure.structure_final_bits(ver, ecl, data_codewords, ecc)
        
        # Get the QR Matrix
        qrmatrix = matrix.get_qrmatrix(ver, ecl, final_bits)
            
        # Draw the picture and Save it, then return the absolute path
        return ver, draw.draw_qrcode(save_place, qrmatrix)
