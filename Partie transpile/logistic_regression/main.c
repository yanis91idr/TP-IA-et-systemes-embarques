
		#include <stdio.h>

		float exp_approx(float x, int n_term) {
			float result = 1.0;
			float term = 1.0;

			for (int i = 1; i <= n_term; i++) {
				term *= x / i;
				result += term;
			}
			
			return result;
		}
		float sigmoid(float x) {
			return 1.0/(exp_approx(-x,10) + 1.0);
		}

		int main() {
			float features[] = { 2.2, 3.19, 7.56, 8.42 };
			int n_feature = 4;
			float result = prediction(features, n_feature);
			printf("The predicted probability is: %f\n", result);
			return 0;
		}

			