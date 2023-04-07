
    #include <stdio.h>
   
    int main() {
        float features[] = { 2.2, 3.19, 7.56 };
        int n_feature = 3;
        float result = prediction(features, n_feature);
        printf("The predicted probability is: %f\n", result);
        return 0;
    }

        