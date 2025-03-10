#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void translateLingwarToCpp(const std::string &fileName) {
    // Derived C++ file name
    std::string outputFileName = fileName.substr(0, fileName.find_last_of('.')) + ".cpp";

    std::ifstream codeFile(fileName);
    std::ofstream compiled(outputFileName);

    if (!codeFile.is_open()) {
        std::cerr << "Error: Cannot open input file: " << fileName << std::endl;
        return;
    }

    if (!compiled.is_open()) {
        std::cerr << "Error: Cannot create output file: " << outputFileName << std::endl;
        return;
    }
    std::string line;
    while (std::getline(codeFile, line)) {
        // Skip comments
        if (line.empty() || line[0] == '@') {
            continue;
        }

        // Handle blank lines
        if (line == "\n") {
            continue;
        }

        // Handle include directives
        if (line.find("#ADD") == 0) {
            if (line.find("I/O") != std::string::npos) {
                compiled << "#include<iostream>\n";
            } else if (line.find("MATH") != std::string::npos) {
                compiled << "#include<cmath>\n";
            }
        }
        // Handle start keyword
        else if (line.find("START") != std::string::npos) {
            compiled << "int main() {\n";
        }
        // Handle int datatype
        else if (line.find("INT") == 0) {
            compiled << "\tint " << line.substr(3) << ";\n";
        }
        // Handle string datatype
        else if (line.find("STR") == 0) {
            compiled << "\tstd::string " << line.substr(3) << ";\n";
        }
        // Handle float datatype
        else if (line.find("FLOAT") == 0) {
            compiled << "\tdouble " << line.substr(6) << ";\n";
        }
        // Handle char datatype
        else if (line.find("CHAR") == 0) {
            compiled << "\tchar " << line.substr(4) << ";\n";
        }
        // Handle pointers
        else if (line.find("INT*") == 0) {
            compiled << "\tint* " << line.substr(4) << ";\n";
        }
        else if (line.find("FLOAT*") == 0) {
            compiled << "\tdouble* " << line.substr(7) << ";\n";
        }
        else if (line.find("CHAR*") == 0) {
            compiled << "\tchar* " << line.substr(5) << ";\n";
        }
        // Handle write keyword
        else if (line.find("WRITE") != std::string::npos) {
            size_t pos = line.find("WRITE");
            std::string toWrite = line.substr(pos + 5);
            compiled << "\tstd::cout << " << toWrite << " << std::endl;\n";
        }
        // Handle read keyword
        else if (line.find("READ") != std::string::npos) {
            size_t pos = line.find(",");
            std::string prompt = line.substr(5, pos - 5);
            std::string variable = line.substr(pos + 1);
            compiled << "\tstd::cout << \"" << prompt << "\";\n";
            compiled << "\tstd::cin >> " << variable << ";\n";
        }
        // Handle arrays
        else if (line.find("ARY") == 0) {
            if (line.find("ARYINT") == 0) {
                size_t pos = line.find(",");
                std::string arrayName = line.substr(6, pos - 6);
                std::string arraySize = line.substr(pos + 1);
                compiled << "\tint " << arrayName << "[" << arraySize << "];\n";
            } else if (line.find("ARYFLOAT") == 0) {
                size_t pos = line.find(",");
                std::string arrayName = line.substr(8, pos - 8);
                std::string arraySize = line.substr(pos + 1);
                compiled << "\tdouble " << arrayName << "[" << arraySize << "];\n";
            } else if (line.find("ARYCHAR") == 0) {
                size_t pos = line.find(",");
                std::string arrayName = line.substr(7, pos - 7);
                std::string arraySize = line.substr(pos + 1);
                compiled << "\tchar " << arrayName << "[" << arraySize << "];\n";
            } else if (line.find("ARYSTR") == 0) {
                size_t pos = line.find(",");
                std::string arrayName = line.substr(6, pos - 6);
                std::string arraySize = line.substr(pos + 1);
                compiled << "\tstd::string " << arrayName << "[" << arraySize << "];\n";
            }
        }
        // Handle arithmetic and assignment operations
        else if (line.find_first_of("+-=*/") != std::string::npos) {
            compiled << "\t" << line << "\n";
        }
        // elif "FOR" in line[0:3]:
        //         for r in range(len(line) - 1):
        //             if line[r+3] != " ":
        //                 break 


        //         for g in range(len(line) -1):
        //             if line[g] == "(":
        //                 break

                
        //         for x in range(len(line) - 1):
        //             if line[x] == ",":
        //                 break

                
        //         for k in range(len(line) - 1):
        //             if line[k] == ")":
        //                 break
            
        //         compiled.write(f"\tfor(int {line[r+3:g-1]} = {line[g+1:x]} ; {line[r+3:g-1]} < {line[x+1:k]} ;{line[r+3:g-1]}++)\n")
        //         compiled.write("\t{\n")
        
        // Handle end keyword
        else if (line.find("END") == 0) {
            compiled << "\treturn 0;\n";
            compiled << "}\n";
        }
    }

    codeFile.close();
    compiled.close();

    std::cout << "Translation completed. Output file: " << outputFileName << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <input_file>" << std::endl;
        return 1;
    }

    translateLingwarToCpp(argv[1]);

    return 0;
}
