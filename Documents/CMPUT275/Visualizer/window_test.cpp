// C code to illustrate using 
// graphics in linux enviornment
#include<iostream>
#include<stdio.h>
#include<stdlib.h>  
#include <string>
#include<graphics.h> 


using namespace std;

class Node {
public:
    Node(int x, int y, int value) {
        this->x = x;
        this-> y = y;
        this->value = value;
    }

    void drawNode() {
        outtextxy(x+5, y+5, "5");
        circle(x, y, 25);
    }
private:
    int x, y;
    int value;
};


int main()
{
   int gd = DETECT, gm;
  // int x = 320, y = 240, radius;
       
   initgraph(&gd, &gm, NULL);
       
   Node n1(320, 240, 5);
   n1.drawNode();
   //for ( radius = 25; radius <= 125 ; radius = radius + 20)
     // circle(x, y, radius);
       
   getch();
   closegraph();
   return 0;
}

/*
int main() 
{ 
    int gd = DETECT, gm; 
    initgraph(&gd,&gm,NULL);
  
    circle(50, 50, 30); 
  
    delay(500000); 
    closegraph(); 
    return 0; 
} */