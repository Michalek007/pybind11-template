#include <pybind11/embed.h>
#include <pybind11/stl.h>
#include <vector>

int sum(std::vector<int> vec){
	int sum = 0;
	for (int i = 0;i<vec.size();i++){
		sum += vec[i];
	}
	return sum;
}

int factorial(int n){
	int result = 1;
	for(int i=0;i<n;i++){
		result = result * (result + 1);
	}
	return result;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("sum", &sum, "Function which sums all containing items.");
    m.def("factorial", &factorial, "Factorial.");
}

