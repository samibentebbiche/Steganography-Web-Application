import stegano.conversion
import numpy
import stegano.DCT_quantification

def cle_insertion(bits_len,nb_matrix):
    x=int(bits_len/nb_matrix)+1
    return x

#fonction d'insertion
def insertion (array , texte,cle):
    octet= stegano.conversion.octet_to_bit(texte) #elle retourne un tableau qui va contenir tous les bits 
    bloc_height,bloc_width,height,width=array.shape
    nb_bits_par_bloc=cle 
    pos=0
    bit_inserer=0
    nb_bits_a_inserer=len(octet)
    
    array_insertion=numpy.ones((bloc_height,bloc_width,height,width)) #ce tableau va contenir toutes les sous-matrice apres insertion
    for  i in range (bloc_height):
        for  j in range (bloc_width) :
            calcul_matrix=stegano.DCT_quantification.copy(array [i][j])
            
            if i==0 and j==0 :

               print("voici la matrice de calcul ")

               print(calcul_matrix)

            cpt=0
      
            for  k  in range(height) :
                for l in range(width) :
                    if  calcul_matrix[k][l]!=0 and calcul_matrix[k][l]!=1 and calcul_matrix[k][l]!=-1 and bit_inserer<nb_bits_a_inserer and cpt<nb_bits_par_bloc :
                            
                                

                        x=bin(int(calcul_matrix[k][l]))
                        z=x[0:len(x)-1]+str(octet[pos])
                        y=int(z,2)
                        calcul_matrix[k][l]=y
                        pos=pos+1
                        cpt=cpt+1
                        bit_inserer=bit_inserer+1

            if i==0 and j==0:


                print ("voici la matrice de calcul apres insertion \n",calcul_matrix)

                

   
            array_insertion[i][j]=calcul_matrix   
        

      

    return array_insertion   

def extraction (data,cle2,cle1):

    bloc_height,bloc_width,height,width=data.shape
    bits=[]
    nb_bits_par_bloc=cle1
    nb_bits_extrait=0
    nb_bits_a_extraire=cle2

    for  i in range(bloc_height) :
        for j in range(bloc_width) :
            
            matrix_extraction=data[i][j]
            if i ==0 and j==0 :
                print("voici la matrice data ",matrix_extraction)
            
                
            cpt=0
            
            for k in range (height)   :
                for l in  range(width) :
                    if matrix_extraction[k][l]!=0 and matrix_extraction[k][l]!=1  and matrix_extraction[k][l]!=-1 and nb_bits_extrait<nb_bits_a_extraire and cpt<nb_bits_par_bloc  :

                        
                        x=int(matrix_extraction[k][l])
                        y=bin(x)
                        print(y)
                        
                        bits.append(y[len(y)-1])
                        nb_bits_extrait=nb_bits_extrait+1
                        cpt=cpt+1


    return stegano.conversion.bit_to_string(bits)

def case_insertion ():
    cases=numpy.array([[0,4],[0,5],[0,6],[0,7],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[5,0],[5,1],[5,2],[6,0],[6,1],[7,0]])
    return  cases 

def insertion_methode2(array , texte,bit):

    octet= stegano.conversion.octet_to_bit(texte) #elle retourne un tableau qui va contenir tous les bits 
    bloc_height,bloc_width,height,width=array.shape
    msg_chiffrer=xor(octet,bit)
    print(msg_chiffrer)
    pos=0
    bit_inserer=0
    nb_bits_a_inserer=len(octet)
    cases= case_insertion()
    i=0
    j=0

    array_insertion=numpy.ones((bloc_height,bloc_width,height,width))
   

 
    
    for i in range(bloc_height):
        for j in range(bloc_width):

            calcul_matrix =stegano.DCT_quantification.copy(array [i][j])
            if i==0 and j==0:
                print(calcul_matrix)

            k=0
            cpt=0
        
            

            while k<26 and nb_bits_a_inserer>bit_inserer  :
                position=cases[k]
                coef=calcul_matrix[position[0]][position[1]]
                x=bin(int(coef))

                if nb_bits_a_inserer-bit_inserer !=1 :
                    z=x[0:len(x)-2]+str(msg_chiffrer[pos])
                
                    pos=pos+1

                    z=z[0:len(z)]+str(msg_chiffrer[pos])
                    cpt=cpt+2
                    bit_inserer=bit_inserer+2
                    pos=pos+1

                else:
                       
                    z=x[0:len(x)-1]+str(msg_chiffrer[pos])
                    pos=pos+1
                    cpt=cpt+1
                    bit_inserer=bit_inserer+1
                    

               

                y=int(z,2)
                calcul_matrix[position[0]][position[1]]=y
                k=k+1



            array_insertion[i][j]=calcul_matrix   
            if i==0 and j==0 :
                print(calcul_matrix) 

    


    return array_insertion



def extraction_methode2(array,cle2,bit):
    bloc_height,bloc_width,height,width=array.shape
    bits=[]
    
    nb_bits_extrait=0
    nb_bits_a_extraire=cle2
    cases=case_insertion()
    

    for i in range(bloc_height):
        for j in range(bloc_width):
            extraction_matrix=array[i][j]
            cpt=0
            k=0
            if i==0 and j==0 :
                print(extraction_matrix)
            while k<26  and nb_bits_extrait<nb_bits_a_extraire :
                position=cases[k]
                x=int(extraction_matrix[int(position[0])][int(position[1])])
                
                y=bin(x)
               
                if nb_bits_a_extraire-nb_bits_extrait!=1:

                   bits.append(y[len(y)-2])
                   bits.append(y[len(y)-1])
                   nb_bits_extrait=nb_bits_extrait+2
                   cpt=cpt+2

                else:
                    bits.append(y[len(y)-1])
                    nb_bits_extrait=nb_bits_extrait+1
                    cpt=cpt+1

                k=k+1

    stegano.conversion.b(bits)
    print("message avant le déchiffrer")
    print(bits)
    print("message texte avant dechiffrer")
    print(stegano.conversion.bit_to_string(bits))
    msg_dechiffrer=ixor(bits,bit)

    return stegano.conversion.bit_to_string(msg_dechiffrer)           


def xor (array,bit):
    taille = len(array)
    msg_chiffrer=[]
    for i in range(taille):
        if array[i]== bit:
            msg_chiffrer.append('0')

        else:
            msg_chiffrer.append('1') 

    return msg_chiffrer 

def ixor(array,bit):
    taille=len(array)
    msg_dechiffrer=[]
    for i in range(taille):
        if array[i]==bit:
            msg_dechiffrer.append('0')
        
        else:
            msg_dechiffrer.append('1')

    return msg_dechiffrer        







           

    