#include "chebyshev_distance.h"
#include <vector>
#include <cmath>

double ChebyshevDistance::chebyshevDistance(const std::vector<double>& v1, const std::vector<double>& v2) {
    double max_diff = 0.0;
    if (v1.size() != v2.size()) {
        return -1;
    }
    for (size_t i = 0; i < v1.size(); ++i) {
        double diff = std::abs(v1[i] - v2[i]);
        if (diff > max_diff) {
            max_diff = diff;
        }
    }
    return max_diff;
}