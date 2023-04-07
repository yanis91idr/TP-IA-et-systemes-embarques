
    #include <stdio.h>

    float prediction(float *features, int n_feature);

    int main() {
        float features[] = {206, 2, 0};
        int n_feature = 3;
        float result = prediction(features, n_feature);
        printf("Prédiction : %f\n", result);
        return 0;
    }
        