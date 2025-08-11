

#include <iostream>
#include <fstream>
#include<string>
#include <cstring>
#include "Sphere.h"
#include "Weather.h"
#include "FriendClass.h"
using namespace std;


void funct(float[][2],int);

void incrementingArray(int[], int);

//int read_bookmarks();
void incrementing2DArray(int[][3]);
void pointers();

const int Bk_MK_Len = 50, CAT_LEN = 30, NUM_URLS = 50;

enum Seasons { Summer, Fall, Winter, Spring };
void structpract2();

struct student {
	
	string Name;
	int age;
	double GPA;
	enum Semester { Freshman, Sophmore, Junior, Senior } sem;
	
};



void copyingarray();
void copyingarray() {


	student aryy[3][3] = {
		{{"Alice", 20, 3.5,student::Freshman}, {"Bob", 21, 3.7}, {"Cara", 22, 3.9}},
		{{"Dan", 23, 2.8}, {"Eve", 24, 3.2}, {"Finn", 25, 3.6}},
		{{"Gina", 26, 3.1}, {"Hank", 27, 2.9}, {"Ivy", 28, 4.0}}
	};

	student s = { "dav", 24, 3.1, student::Junior };
	cout << s.sem;

	student copystuary[3][3];
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) *(*(copystuary + i) + j) = *(*(aryy + i) + j);
	}



}
student structpract();

const int arysz = 10;
int main()
{
	string s;
	//cout << s << endl;
	FriendClass myfriend;
	myfriend.CreateDoc(FriendClass::Julien);
	myfriend.PullDoc();
	myfriend.ReadArray(s, 0);
	//cout << s;

	//cout << read_bookmarks();

	pointers();
	structpract();
	//structpract2();
	//FriendClass friends[4];
	string curFriend[4];
	FriendClass friends[4] = {

		{ FriendClass::Max, "Max is the guy." },
		{ FriendClass::Julien, "Julien is cool." },
		{ FriendClass::Mike, "Mike is smart." },
		{ FriendClass::Adam, "Adam is quiet." }
	};

	for (int i = 0; i < 4; i++) {
		
		friends[i].CreateDoc(friends[i].boy);
		
		friends[i].PullDoc();
		friends[i].ReadArray(curFriend[i], i);
		//cout << *curFriend << endl;
	}



	/*weather niceday;

	niceday.set_season(weather::Winter);
	niceday.describe();
	*/

	


	//cout << structpract().GPA;


	string ary[3][2] = {
		{"Hello","Bonjour"},
		{"Goodbye","Au-Revoir"},
		{"dead","mort"}

	};


	
	copyingarray();



	ifstream in;
	ofstream out;

	out = ofstream("someinfo.txt");


	struct al {
		enum alpha { a, b, c, d } val;
		
		int num;
	};
	al arr[3] = { {al::a,1 }, {al::b, 2}, {al::c, 3} };

	cout << arr[1].val;
	


	
	//cout << cum::alpha::a;


	/*ofstream newfile("data.dat");
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			newfile << ary[i][j] << " ";
		}
		newfile << endl;
	}
	newfile.close();
	
	ifstream file("data.dat");
	int arcopy[3][2] = {};
	
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			
			file >> *(*(arcopy + i) + j);
			cout << *(*(arcopy + i) + j);
		}
		cout << endl;


	}

	file.close();*/


	

	Sphere sphere;

	

	cout << "Enter radius: ";
	

	//sphere.set_radius(rad);
	sphere.get_radius();
	cout << sphere.get_area() << endl;
	//ofstream sphereradius("sphereradius.dat");

	//sphereradius.close();
	ifstream sphereradius("sphereradius.dat");
	
	Sphere sph[10];
	float rad[10];
	int j = 0;
	while (j < 10 && sphereradius >> rad[j]) ++j;


	for (int i = 0; i < j; i++) {
		
		sphereradius >> rad[i];
		sph[i].set_radius(rad[i]);
		cout << sph[i].get_radius() << " " << sph[i].get_area() << endl;
	}
	sphereradius.close();
	//int ary[arysz] = { 1,1,1,1,1,1,1,1,1,1 };

	int Ary2D[2][3] = {
		{1,2,3}, {4,5,6}
	};

	//incrementing2DArray(Ary2D);

	//incrementingArray(ary, 10);



	return 0;
}

void funct(float _ary[][2], int count) 
{

}


//void pointers() {
//	int num = 1;
//	int* point = &num;
//	cout << point << " " << *point;
//}









void incrementingArray(int ary[], int arsz) {
	

	for (int * p = ary; p < ary + arsz; p++) cout << ++*p;

}
void incrementing2DArray(int ary[][3]) {
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++) {
			cout << ++ * (*(ary + i) + j);
		}
	}

}

student structpract() {
	const int structarysz = 3;
	student stuary[structarysz] = {
		{"Sen",22,3.9},
		{"Julien", 26, 3.3},
		{"Osak", 22, 4.0}
	};
	ofstream outfile("studentinfo.dat");
	for (student* p = stuary; p < stuary + structarysz; p++) {
		outfile << p->Name << " " << p->age << " " << p->GPA << " " << endl;
	}
	outfile.close();
	ifstream in("studentinfo.dat");
	student copystu[structarysz];



	student higpa = {};
	for (student* q = copystu; q < copystu + structarysz; q++) {
		in >> q->Name >> q->age >> q->GPA;

		if (q->GPA > higpa.GPA) higpa = *q;
		
	}in.close();
	return higpa;

}



void Season(Seasons _season) {

	double avgTemp[arysz] = { 0,10,20,30,40,50,60,70,80,90 };
	switch (_season) {
	case Summer:
		cout << avgTemp[8];
	case Fall:
		cout << avgTemp[4];
	case Winter:
		cout << avgTemp[2];
	case Spring:
		cout << avgTemp[6];
	}

	
}




//int read_bookmarks() {//char[][BK_MK_LEN], char[][CAT_LEN]){
//
//
//
//	char cats[NUM_URLS][CAT_LEN], bkmks[NUM_URLS][Bk_MK_Len];
//	ifstream bookmarks("bookmarks.dat");
//
//	int i = 0;
//	while (i < NUM_URLS &&
//		bookmarks.getline(bkmks[i], Bk_MK_Len) &&
//		bookmarks.getline(cats[i], CAT_LEN)) {
//
//		i++;
//	}
//	return i;
//
//}



void pointers() {
	double ary[8];
	/*double* ary[8];
	double (*a)[8];
	double* funct();
	double (*funct)();
	double funct();*/

	//cout << &ary[0];	
	int ara[] = { 1,2,3,4,5,6,7,8,9,10 };
	int *ip1, *ip2;
	ip1 = ara;
	short a[32] = {};

	for (short* p = a, i = 0; i < 32; p++, i++) {
		
		*p = i * i;
		//cout << *p << endl;
	}

	

}

