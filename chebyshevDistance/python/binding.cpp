#include "chebyshev_distance.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(trace_core, m) {
    m.doc() = R"doc(Python binding for Chebyshev Distance)doc";

    py::class_<ChebyshevDistance>(m, "ChebyshevDistance")
        .def_static("chebyshevDistance", &ChebyshevDistance::chebyshevDistance, R"doc(
            Compute Chebyshev Distance using pure C++.

            Parametrs:
                v1 : first vector 
                v2 : second vector 

            Returns:
                float
                    Chebyshev distance between vectors

        )doc");

}