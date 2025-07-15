//FriendClass.h
#include <string>
using namespace std;
class FriendClass {

public: 
	enum Friends {Max, Julien, Mike, Adam } boy;
private:
	
	string frienddesc[4] = {};
	
	string desc;
	string DescFriend(Friends _f);
public:
	FriendClass() {}
	FriendClass( Friends _boy, string _desc) {
		desc = _desc; boy = _boy;
	}
	void CreateDoc(Friends _f);
	void PullDoc();
	void ReadArray(string &, int index);


};