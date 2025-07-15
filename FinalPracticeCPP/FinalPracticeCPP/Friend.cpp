//Friend.cpp


#include "FriendClass.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;





string FriendClass::DescFriend(Friends _f) {
	switch (_f) {
	case Max: return "Wow what a niceguy.\n"; 
	case Julien:return "Wow what a belgian.\n"; 
	case Mike: return "Wow what an Italian puerto rican.\n"; 
	case Adam:return "Wow what a fella.\n"; 
	}
	
}
void FriendClass::CreateDoc(Friends _f) {
	ofstream out("myfriends.dat");
	out << DescFriend(_f) << endl;
	out.close();
}
void FriendClass::PullDoc() {
	ifstream in("myfriends.dat");
	for (int i = 0; i < 4; i++) getline(in, frienddesc[i]);
	
	/*for (string* p = frienddesc; p < frienddesc + 4; p++) {
		in >> *p;
	}*/
	in.close();
}
void FriendClass::ReadArray(string& s, int index) {
	s = frienddesc[index];
}