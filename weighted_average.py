def get_weighted_average(scores, gamma):
  weighted_sum = 0
  total_weight = 0
  for i in range(len(scores)):
    weight = gamma ** (len(scores) - i - 1)
    weighted_sum += scores[i] * weight
    total_weight += weight
  return weighted_sum / total_weight if total_weight != 0 else 0

if __name__ == '__main__':
  print("Find a weighted average of happiness scores, weighing recent scores more heavily.")

  scores = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 9, 8, 7, 8, 9, 8, 7, 8, 9]
  print("Test scores (more low scores to emphasize how the higher scores will be more impactful due to recency):", scores)

  weighted_avg = get_weighted_average(scores, 0.9)
  print("Weighted average:", weighted_avg)
  print("Unweighted average:", sum(scores) / len(scores))
