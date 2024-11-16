CXX=g++
CXXFLAGS=-std=c++14 -O3 -march=native -Wall -I$(SRC_DIR) $(shell python3 -m pybind11 --includes)
PY_LDFLAGS=$(shell python3-config --ldflags) -shared -fPIC
GTEST_FLAGS=-lgtest -lgtest_main -pthread
LDFLAGS=-lopenblas
SRC_DIR=chebyshevDistance/src
TESTS_DIR=chebyshevDistance/tests
PYTHON_DIR=chebyshevDistance/python

all: chebyshevDistance test

ChebyshevDistance: $(PYTHON_DIR)/binding.o $(SRC_DIR)/chebyshev_distance.o
	$(CXX) $^ -o $(PYTHON_DIR)/trace_core`python3-config --extension-suffix` $(PY_LDFLAGS) $(CXXFLAGS)

$(PYTHON_DIR)/binding.o: $(PYTHON_DIR)/binding.cpp $(SRC_DIR)/chebyshev_distance.h
	$(CXX) $(CXXFLAGS) -fPIC -c $< -o $@

$(SRC_DIR)/chebyshev_distance.o: $(SRC_DIR)/chebyshev_distance.cpp $(SRC_DIR)/chebyshev_distance.h
	$(CXX) $(CXXFLAGS) -fPIC -c $< -o $@

test: $(TESTS_DIR)/test_trace.o $(SRC_DIR)/chebyshev_distance.o
	$(CXX) $^ -o $(TESTS_DIR)/test_trace $(GTEST_FLAGS)

$(TESTS_DIR)/test_trace.o: $(TESTS_DIR)/test_trace.cpp $(SRC_DIR)/chebyshev_distance.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

run_tests: test
	./$(TESTS_DIR)/test_trace

clean:
	rm -f $(PYTHON_DIR)/*.o $(SRC_DIR)/*.o $(TESTS_DIR)/*.o $(PYTHON_DIR)/trace_core`python3-config --extension-suffix` $(TESTS_DIR)/test_trace