
import processing.sound.*;
SoundFile brap,blip; 



PShape frogtank;
float randx,randy;
int gs,count;
int grav = 1;
int numO = 100;
int numb = 500;
int bx,by = 25;
float rotZ,rotY;
int keepgoing = 0;
Orb [] orb = new Orb[numO];
Bing []bing = new Bing[numb];

void setup(){
  
  brap = new SoundFile(this, "brap.mp3"); 
  brap.amp(0.1);
  brap.rate(1);
  blip = new SoundFile(this, "blip.mp3"); 
  blip.amp(0.01);
  blip.rate(2);
  
  
  
  
  noStroke();
  size(1000,1000,P3D);
  gs = 0;
  
  frogtank = loadShape("frogtank.obj");
  frogtank.rotateX(PI);
  
  rectMode(CENTER);
  
    games();
    
    
}
void draw(){
  if(millis()%100 <= 10){
    count++;
  }
  randx = noise(count)*1000;
  randy = noise(count)*1000;
  background(0);
  lights();
  ambientLight(100,50,70);
  translate(0,0,0);
  //rect(0,0,width,height);
 keepgoing = 0;
 if(keyPressed){
   if(key == 'w'){rotZ+=10;}
   if(key == 's'){rotZ-=10;}
    if(key == '1'){gs=0;games();}
   if(key == '2'){gs=1; games();}
    if(key == '3'){gs=2; games();}
     if(key == '4'){gs=3; games();}
     if(key == '5'){gs=4; games();}
     if(key == '6'){gs=5; games();}
 }
  if(mousePressed){
    pushMatrix();
    translate(mouseX,mouseY,0);
    fill(200,50,100);
    sphere(50);
    popMatrix();
    for(int i = 0; i < numO; i++){
      orb[i] = new Orb(mouseX,mouseY); 
      
    }
    
    blip.stop();
    blip.removeFromCache();
    //brap.play();
  }
  for(int i = 0; i < numO; i++){
    orb[i].draworb();
    //orb[i].bonk();
  }
  for(int i = 0; i < numb; i++){ 
    bing[i].drawbing();
    bing[i].touched();
  } 
}
class Orb{
  boolean played = false;
  float bouncefall = 1;
  float bouncefly = 1;
  float dir =int(random(-1,1));
  float posY,posX,posZ;
  int size = int(random(20,40));
  int fly = int(random(-50,50));
  float fall = int(random(-50,50));
  int rcol = int(random(100,200));
  int gcol = int(random(50,100));
  int bcol = int(random(100,200));
 
    //float rotx = PI/10 ;
    //float roty = PI/3;
  Orb(int _posX, int _posY){
    posY = _posY;
    posX = _posX;
  }
  void draworb(){
    
   fill(rcol,gcol,bcol);
    //fill(240);
    //frogtank.setFill(color(rcol,gcol,bcol));
    
    pushMatrix();
    translate(posX,posY,rotZ);
    sphere(size);
    //shape(frogtank);
    
    
    //frogtank.rotateY(roty);
    //frogtank.rotateX(rotx);
   
    //circle(posX,posY,size);
    posY+= fall;
    posX+= fly;
    
    fall += grav;
    
      fly += dir;
    
   
    
    fall /= bouncefall;
    fly /= bouncefly;
    popMatrix();
    
    
  }
  void br(){
    if(played == false){
      //blip.play();
      
    }
    played = true;
  }
  void bonk(){
    for(int i = 0; i < numO; i++){
      
      if(orb[i].posX != posX && orb[i].posY != posY && posX <= orb[i].posX + (size) && posX  >= orb[i].posX- (size) && posY <= orb[i].posY + (size) && posY >=  orb[i].posY - size){
        //fly*=-1 + int(random(0,2));
        
        bouncefly+=0.00001;
        fall*=-1 + int(random(0,1));
        bouncefall+=.001;
      }
    }
  }
}

class Bing{
  float posX = width/2; 
  float posY = height/2;
  int size = 50;
  Bing(float _posX, float _posY){
    
    posX = _posX;
    posY = _posY;
  }
  void touched(){
    for(int i = 0; i < numO; i++){
      if(orb[i].posX <= posX + (size-5) && orb[i].posX >= posX - (size-5) && orb[i].posY <= posY + (size) && orb[i].posY >= posY - size){
        //orb[i].fly*=-1 ;
        
        //orb[i].fall*=-1;
        //orb[i].bouncefly+=0.01;
        //orb[i].bouncefall+=.01;
        orb[i].bouncefly+=10;
        orb[i].bouncefall+=10;
        orb[i].br();
        
        //orb[i].rotx=PI*10;
        //orb[i].roty=PI*10;
        
      }
      //if(orb[i].posY <= posY + (size) && orb[i].posY >= posY - size){
      //  orb[i].fly*=-1;
        
      //}
      
    }
  }
  void drawbing(){
    pushMatrix();
    fill(100);
    
    translate(posX,posY,rotZ);
    box(size);
   popMatrix();
    //rect(posX,posY,size,size);  
  }
}
void games(){
  for(int i = 0; i < numO; i++){
      orb[i] = new Orb(0,0);    
    }
  if(gs == 0){
      for(int i = 0; i < numb; i++){
        bing[i] = new Bing(i*50, i*50);  
      }
    }  
    if(gs == 1){
      for(int i = 0; i < numb; i++){
        bing[i] = new Bing(width/2, i*50);
      }
    }
    if(gs == 2){
      for(int i = 0; i < numb; i++){
        bing[i] = new Bing(i*50, height/2);
      }
    }
    if(gs == 3){
      for(int i = 0; i < numb; i++){
        int randx = int(random(0,width));
        int randy = int(random(0,height));
        
        bing[i] = new Bing(int(randx)*5,int(randy)*5);
      }
      
    }
    if(gs == 4){
    
          
      
        for(int i = 0; i < numb; i++){
          
          
          bing[i] = new Bing(int(randx)/2,int(randy)/2);
        }
      
      
    }
    if(gs == 5){
      for(int i = 0; i < numb; i++){
        bing[i] = new Bing(-50,-50);
      }
      
    }
}
