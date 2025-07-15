

#include "Weather.h"
#include <iostream>
using namespace std;

weather::weather() { current = Summer; };
void weather::set_season(Season s) { current = s; }
void weather::describe() {
	switch (current) {
	case Summer: cout << "The day is Hot" << endl; break;
	case Winter: cout << "The day is cold" << endl; break;
	case Fall: cout << "There are leaves" << endl; break;
	case Spring: cout << "The trees are flowering" << endl; break;
	}
}
weather::Season weather::Get_Season() { return current; }