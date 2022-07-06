file = "assemblerInput.txt"
filehandle = open("assemblerInput.txt","r")
with filehandle:
    for line in filehandle:
        tokenized_line = line.split()

        if tokenized_line[0].upper() =="LM":
            r=int(tokenized_line[1][1])
            hex = tokenized_line[2]
            hex_list = hex.split("x")
            v=int(hex_list[(1)])                            
            b=[2,r,v>>4,v&0xF]                            
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l,]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="ST":
            r=int(tokenized_line[1][1])
            hex = tokenized_line[2]
            hex_list = hex.split("x")                   
            v=int(hex_list[(1)])                          
            b=[3,r,v>>4,v&0xF]
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')


        #elif tokenized_line[0].upper()=="CMPR":
        #    r=int(tokenized_line[1][1])
        #    v=int(tokenized_line[2][1])                                            
        #    b=[4,r,v>>4,v&0xF]                     
        #    i=bin(b[0])
        #    j=bin(b[1])
        #    k=bin(b[2])
        #    l=bin(b[3])
        #    m=[i,j,k,l]
        #    print(m)



        #elif tokenized_line[0].upper()=="CMPI":
        #    r=int(tokenized_line[1][1])
        #    v=int(tokenized_line[2])                                            
        #    b=[5,r,v>>4,v&0xF]                   
        #    i=bin(b[0])
        #    j=bin(b[1])
        #    k=bin(b[2])
        #    l=bin(b[3])
        #    m=[i,j,k,l]
        #    print(m)


        #if we want to use this style then

       # elif tokenized_line[0].upper()=="BEQ":
        #    r=int(tokenized_line[1][1])                                           
        #    b=[6,r]                     
        #    i=bin(b[0])
        #    j=bin(b[1])
         #   m=[i,j]
         #   print(m)

       # elif tokenized_line[0].upper()=="BNE":
        #    r=int(tokenized_line[1][1])                                           
        #    b=[7,r]                     
         #   i=bin(b[0])
         #   j=bin(b[1])
          #  m=[i,j]
           # print(m)



        elif tokenized_line[0].upper()=="BEQ":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3][1])                                           
            b=[6,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="BGT":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3][1])                                           
            b=[7,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="BLT":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3][1])                                           
            b=[8,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="B":
            r=int(tokenized_line[1][1])                                          
            b=[9,r]                
            i=bin(b[0])
            j=bin(b[1])
            m=[i,j]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="ADDI":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3])                                           
            b=[10,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="ADD":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3][1])                                           
            b=[11,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="SUBI":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3])                                           
            b=[12,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="SUB":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3][1])                                           
            b=[13,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="SL":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3])                                           
            b=[14,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="SR":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3])                                           
            b=[15,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="AND":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3][1])                                           
            b=[0,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="OR":
            r=int(tokenized_line[1][1])
            v=int(tokenized_line[2][1]) 
            x=int(tokenized_line[3][1])                                           
            b=[1,r,v,x]                     
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')

        elif tokenized_line[0].upper()=="END":                                           
            b=[4]                     
            i=bin(b[0])
            m=[i]
            print(m)

            lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')

                f.write('\n')