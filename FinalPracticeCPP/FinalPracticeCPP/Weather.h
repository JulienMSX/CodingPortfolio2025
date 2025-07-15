

class weather {
public: 
	enum Season { Winter, Spring, Summer, Fall };
private:
	
	Season current;

public:
	weather();
	
	void set_season(Season _s);


	Season Get_Season();

	void describe();
};
