float prediction(float *features, int n_feature) {
  float result = -8152.937710;
  result += 717.258370 * features[0];
  result += 36824.195974 * features[1];
  result += 101571.840022 * features[2];
  return result;
}
