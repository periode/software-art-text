#pragma once

#include "ofMain.h"
#include "ofxGui.h"
#include "ofxOsc.h"
class ofApp : public ofBaseApp{
    
//track code
    int port_to_listen_to = 2046;
    ofxOscReceiver receiver;
    ofSoundPlayer mysound;
    
    ofVec2f front;
    ofVec2f back;
    ofVec2f Ndirection;
    ofVec3f direction;
    ofVec3f position;
    
   
    float a;
    float b;
    
    
    
//movement
    ofxPanel gui;
    ofxSlider<float> alpha1;
    ofxSlider<float> alpha2;
    ofxSlider<float> distance;
    ofImage image;
    ofMesh mesh;
    ofBoxPrimitive box;
    
    ofEasyCam easyCam;
    
    
    ofCamera cam;
    ofNode node;
    float angle;
    ofLight light;
    bool bOrbit, bRoll;
    float angleH;
    float roll;
    float depth;

//mapping and tracking
    bool manual;
    bool sound;
    
    
    int xpos;
    int ypos;
    int w;
    int h;
    
    vector<float> height;
    vector<ofVec3f> cube_positions;
   
    vector<float> cube_sizesx;
    vector<float> cube_sizesy;
    vector<float> cube_sizesz;
    
    ofVec4f cube_color;
    vector<float> color_bank;
    
    
    
    float intensityThreshold;
    float intensityThreshold1;
    
    float radiusrange;
    ofVec2f landmark1;
    ofVec2f landmark2;
    ofVec2f landmark3;
    ofVec2f landmark4;
    ofVec2f landmark5;
    ofVec2f landmark6;
    
//front
    ofTrueTypeFont myfont;
    
    

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y );
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void mouseEntered(int x, int y);
		void mouseExited(int x, int y);
		void windowResized(int w, int h);
		void dragEvent(ofDragInfo dragInfo);
		void gotMessage(ofMessage msg);
		
};
