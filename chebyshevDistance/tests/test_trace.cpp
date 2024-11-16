#include "chebyshev_distance.h"
#include <gtest/gtest.h>

TEST(ChebyshevDistanceTests, ChebyshevDistance) {
    std::vector<double> a1 = {1, 2, 3};
    std::vector<double> a2 = {4, 5, 7};

    std::vector<double> b1 = {1, 2, 103, 4};
    std::vector<double> b2 = {4, 5, 106, 36};

    std::vector<double> c1 = {-5, -2, 0};
    std::vector<double> c2 = {2, -15, 6};

    EXPECT_DOUBLE_EQ(2.0, ChebyshevDistance::chebyshevDistance(a1, a2));
    EXPECT_DOUBLE_EQ(0.0, ChebyshevDistance::chebyshevDistance(a1, a1));
    EXPECT_DOUBLE_EQ(32.0, ChebyshevDistance::chebyshevDistance(b1, b2));
    EXPECT_DOUBLE_EQ(13.0, ChebyshevDistance::chebyshevDistance(c1, c2));

    EXPECT_DOUBLE_EQ(-1.0, ChebyshevDistance::chebyshevDistance(a1, b1));

}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}