#ifndef GAMECHESSCORE_COMPLEX_H
#define GAMECHESSCORE_COMPLEX_H
#include <cmath>
#include <string>
#include <iostream>
#include <pybind11/embed.h>
#include <pybind11/stl.h>

class Complex {
private:
    float _real;
    float _imag;
public:
    explicit Complex(float real=0, float imag=0): _real{real}, _imag{imag}{}
    [[nodiscard]] float get_real() const {return _real;}
    [[nodiscard]] float get_imag() const {return _imag;}
    void set_real(float real) {_real = real;}
    void set_imag(float imag) {_imag = imag;}
    void print() const;
    [[nodiscard]] Complex conjugate() const;
    [[nodiscard]] float modulus() const;
    Complex add(Complex& other) const;
    Complex subtract(Complex& other) const;
    Complex multiply(Complex& other) const;
    Complex divide(Complex& other) const;
};


#endif //GAMECHESSCORE_COMPLEX_H
