import joblib
import numpy as np
import os

def generate_c_code(model, output_file):
    coef = model.coef_
    code = "#include <stdio.h>\n\nfloat prediction(float *features, int n_features) {\n"
    code += "\tfloat coef[] = {"
    for c in coef:
        code += str(c) + ", "
    code = code[:-2] + "};\n"
    code += "\tfloat intercept = " + str(model.intercept_) + ";\n"
    code += "\tfloat result = intercept;\n"
    code += "\tfor (int i = 0; i < n_features; i++) {\n"
    code += "\t\tresult += features[i] * coef[i];\n"
    code += "\t}\n"
    code += "\treturn result;\n}"
    
    with open(output_file, 'w') as f:
        f.write(code)

def main():
    # Load the saved linear regression model
    model = joblib.load('model.joblib')
    
    # Generate C code for the model
    generate_c_code(model, 'model.c')
    
    # Compile the C code
    os.system('gcc -o model model.c')
    
    # Define a sample input
    input_data = np.array([2.3, 4.5, 1.2])
    
    # Call the generated function
    os.system('./model ' + ' '.join([str(f) for f in input_data]))
    
if __name__ == '__main__':
    main()
