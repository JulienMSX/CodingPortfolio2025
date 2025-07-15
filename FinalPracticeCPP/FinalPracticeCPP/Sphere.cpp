#define _USE_MATH_DEFINES
#include "Sphere.h"
#include <math.h>



void Sphere::set_radius(float r) {
	radius = r;
}



float Sphere::get_radius() { return radius; }

float Sphere::get_area() {return 4 * M_PI * (radius * radius); }