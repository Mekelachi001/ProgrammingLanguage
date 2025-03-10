# Program to translate Lingwar Code to Cpp Program
# Started Date: 1/17:2025
# End Date: Working
# Author : Chijioke Mekelachi
# School : Ignatus Ajuru University 

import sys
import os


# Main Program

def main():
    # print(sys.argv[1])
    file_name = sys.argv[1]

    # File Name Creation
    global run 
    run = (f"{file_name[:len(file_name)-4]}.cpp")

    # Writing to the New created File
    # The Cpp file
    compiled = open(f"{file_name[:len(file_name)-4]}.cpp",'w')

    # For Line counting sake
    x = 0

    # Reading line by line
    # Line by Line convertion To  C++
    with open(file_name,"r") as codeFile:
        for line in codeFile:
            # print(type(line))
            # print(line)
            x=x+1
            # print(line)

            # Implemantation of comment
            if line[0] == '@':
                continue
            
            # Implimentation of blank space
            elif line == "\n":
                continue
            
            elif "#ADD" in line[0:5]:
                if "I/O" in line[4:10]:
                    compiled.write("#include<iostream>\n")
                elif "MATH" in line[4:12]:
                    compiled.write("#include<cmath>\n")
                
            # Implimentation of the Start Key Word
            elif "START" in line[0:7].upper():
                compiled.write("int main(){\n")

            #inplimatation of int datatype 
            elif "int" in line[0:3]:
                compiled.write(f"\tint{line[3:len(line)-1]};\n")
            
            #inplimatation of STRING datatype 
            elif "str" in line[0:3].upper():
                compiled.write(f"\tstd::string {line[3:len(line)-1]};\n")
            
            #inplimatation of FLOAT datatype 

            elif "float" in line[0:6].upper():
                compiled.write(f"\tdouble {line[6:len(line)-1]};\n")
            
            # Implimentation of Char datatype
            elif "char" in line[0:4].upper():
                compiled.write(f"\tchar {line[4:len(line)-1]};\n")


            ########### Pointer datatype ############

            elif "INT*" in line[0:4]:
                compiled.write(f"\t*int {line[4:len(line)-1]};\n")
            
            #inplimatation of FLOAT datatype 

            elif "FLOAT*" in line[0:7]:
                compiled.write(f"\tdouble *{line[7:len(line)-1]};\n")
            
            # Implimentation of Char datatype
            elif "CHAR*" in line[0:5]:
                compiled.write(f"\tchar *{line[5:len(line)-1]};\n")

            

            ################ End of Pointer Datatype #####################
            
            # Implimentation of the write Keyword
            elif "WRITE" in line:
                if line[len(line)-1] == ';':
                    compiled.write(f"\tstd::cout<<{line[6:len(line)-1]}<<std::endl;\n")
                else:
                    compiled.write(f"\tstd::cout<<{line[6:len(line)-1]};\n")
                # print(line[6:])
            elif "READ" in line:
                for x in range(len(line)):
                    if line[x] == ',':
                        break
                # var = input(line[5:x])
                compiled.write(f"\tstd::cout<<{line[5:x]};\n")
                compiled.write(f"\tstd::cin>>{line[x+1:]}")


            # Implimentation of Arrays
            elif "ARY" in line[0:3]:
                # Define Array Types
                if "ARYINT" in line[0:6]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+5] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    # compiled.write(f"\tint {line[x+7:g]}[{line[g+1:len(line)-1]}];\n")
                    compiled.write(f"\tint {line[6:]}")
                # Floating point array
                elif "ARYFLOAT" in line[0:8]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+8] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    compiled.write(f"\tdouble {line[x+9:g]}[{line[g+1:len(line)-1]}];\n")
                
                # Character Array
                elif "ARYCHAR" in line[0:7]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+7] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    compiled.write(f"\tchar {line[x+8:g]}[{line[g+1:len(line)-1]}];\n")
                
                
                # Array Of String 

                if "ARYSTR" in line[0:6]:
                    # Integer Array
                    for x in range(len(line)-1):
                        if line[x+5] != "":
                            break
                    for g in range(len(line)-1):
                        if line[g] == ",":
                            break
                    compiled.write(f"\tstd::string {line[x+7:g]}[{line[g+1:len(line)-1]}];\n")
            

            #FOR [NAME OF VARIABLE] ([BEGIN],[END])
            #   STATEMENT
            #   ENDFOR
            ####################################### For Loop ##############################################
            elif "FOR" in line[0:3]:
                for r in range(len(line) - 1):
                    if line[r+3] != " ":
                        break 


                for g in range(len(line) -1):
                    if line[g] == "(":
                        break

                
                for x in range(len(line) - 1):
                    if line[x] == ",":
                        break

                
                for k in range(len(line) - 1):
                    if line[k] == ")":
                        break
            
                compiled.write(f"\tfor(int {line[r+3:g-1]} = {line[g+1:x]} ; {line[r+3:g-1]} < {line[x+1:k]} ;{line[r+3:g-1]}++)\n")
                compiled.write("\t{\n") 

            # End froloop statement 
            elif "ENDFOR" in line[0:7]:
                compiled.write("\t}\n")  

            ################################### End for loop ###############################
            ########################## CAlling Functions #################################
            elif "CALLFUNC" in line[0:9]:
                o = 0
                for x in range(len(line) - 1):
                    if line[x] == "(":
                        break 
                    
                for g in range(len(line)-1):
                    if line[g] == ")":
                        break

                for a in range(len(line)-1):
                    if line[a] == '[':
                        break
                
                for b in range(len(line) - 1):
                    if line[b] == "]":
                        break
                for c in range(len(line) - 2):
                    if line[c] == "=":
                        break 
                for d in range(len(line) - 1):
                    if line[d] == ">":
                        o = 10
                        break
                
                match(o):
                    case 10:
                        name = line[a+1:b]
                        compiled.write(f"\t{line[c+2:len(line)-1]} = {name}({line[x+1:g]});\n")
                    case 0:
                        name = line[a+1:b]
                        compiled.write(f"\t{name}({line[x+1:g]});\n")
                    
                    case _:
                        raise SyntaxError ("Invalis syntax")
            

            ################################# Edn calling function #########################3

            ################################### Start If StateMent ###########################
            elif "IF" in line[0:3]:
                for x in range(len(line) - 1):
                    if line[x] == "(":
                        break 
                for g in range(len(line)-1):
                    if line[g] == ")":
                        break
                compiled.write(f"\tif {line[x:g+1]}\n")
                compiled.write("\t{\n")
            # Aritimatic Operation s

            elif "ENDIF" in line[0:6]:
                compiled.write("\t}\n")

            ################### End of If Statement ###################


            ######################### ELIF STATEMENT ####################
            elif "ELSEIF" in line[0:8]:
                for x in range(len(line) - 1):
                    if line[x] == "(":
                        break 
                for g in range(len(line)-1):
                    if line[g] == ")":
                        break
                compiled.write("\t}")
                compiled.write(f"else if {line[x:g+1]}\n")
                compiled.write("\t{\n")
            elif "ELSE" in line.strip():
                compiled.write("\t}else{")
            
            elif "ENDIF" in line[0:6]:
                compiled.write("\t}\n")
            ######################## Return Key Word #########################
            elif "RETURN" in line[0:7]:
                for x in range(len(line) - 1):
                    if line[x] == ";":
                        break
                for a in range(len(line)-1):
                    if line[a] == '[':
                        break
                
                for b in range(len(line) - 1):
                    if line[b] == "]":
                        break
                compiled.write(f"\treturn {line[a+1:b]};\n")

            ######################## END ELIF STATEMENT ################
            # Aritimatic Operation s


            elif any(op in line for op in ("+", "-", "/", "*","=")):
                compiled.write(f"\t{line}")
            
            ########################### FUNCTION S AND FUNCTION TYPE #############################
            # Syntax FUNC [TYPE] NAME ([Type] [name])


                        
                    
            elif "FUNC" in line[0:5]:
                for x in range(len(line) - 1):
                    if line[x] == "(":
                        break 
                    
                for g in range(len(line)-1):
                    if line[g] == ")":
                        break

                for a in range(len(line)-1):
                    if line[a] == '[':
                        break
                
                for b in range(len(line) - 1):
                    if line[b] == "]":
                        break
                
                type_data = line[a+1:b]
                # print(type_data)
                name = line[b+1:x]
                # print(name)

                match (type_data):
                    case "int":
                        compiled.write(f"\nint {name} ({line[x+1:g]})\n")
                        compiled.write("{\n")
                    case "float":
                        compiled.write(f"float {name} ({line[x+1:g]})\n")
                        compiled.write("}\n")
                    case "str":
                        compiled.write(f"std::string {name} ({line[x+1:g]})\n")
                        compiled.write("}\n")
                    case "char":
                        compiled.write(f"char {name} ({line[x+1:g]})\n")
                        compiled.write("}\n")
                    case _:
                        raise SyntaxError ("No such function type")

            elif "ENDFUNC" in line[0:8]:
                compiled.write("}\n")
            

            ########################### Calling a function ###########################
            
            
            ######################### END OF FUNCTION SEGMANT #######################

            # Implimetation of End startement 
            elif "END" in line[:3]:
                compiled.write("\treturn 0;\n")
                compiled.write("}\n")
                compiled.write("// This Is the OutPut Code From The Lingwar Program")
            # else:
            #     print(f"Syntax Error at line {x}"))
if __name__ == '__main__':
    main()
    # start = sys.argv[2]
    # if start == "on":
    #     os.system(f" g++ {run} -o {run[:4]}")
    #     # os.system(f"rm {run}")
    #     os.system(f"./{run[:4]}")
    # elif statr == "off":
    #     os.system(f" g++ {run} -o {run[:4]}")
    #     os.system(f"rm {run}")
    #     os.system(f"./{run[:4]}")
    # else:
    #     os.system(f" g++ {run} -o {run[:4]}")
    #     # os.system(f"rm {run}")
    #     os.system(f"./{run[:4]}")
    