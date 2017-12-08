#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

//set tracking
    receiver.setup(port_to_listen_to);
    
//set background
    ofBackground(255);
    
//set boxes
    
    for (int x=0; x<50; x++) {
        for (int y=0; y<50; y++) {
            ofVec3f cube_pos(ofRandom(0, ofGetWidth()), ofRandom(0, ofGetHeight()));
                
            cube_positions.push_back(cube_pos);
            
            float cube_sizex=ofRandom(0, 20);
            float cube_sizey=ofRandom(0, 20);
            float cube_sizez=ofRandom(0, 20);
            
            cube_sizesx.push_back(cube_sizex);
            cube_sizesy.push_back(cube_sizey);
            cube_sizesz.push_back(cube_sizez);

                
            float randomColor=ofRandom(30,240);
                
            color_bank.push_back(randomColor);
               
            
        }
    }
    

    
//set camera
    
    bOrbit = bRoll = false;
    angleH = roll = 90.f;
    depth = 1000.f;
    
    cam.orbit(angleH, 0 , depth);
    cam.roll(roll);
    cam.setGlobalPosition(0,0,0);
    
    
   
    
//mapping
    manual=false;
    
    radiusrange=100;
    landmark1.set(189,180);
    landmark2.set(250,260);
    landmark3.set(359,356);
    landmark4.set(400,300);
    landmark5.set(310,250);
    landmark6.set(430,200);
    
//front
    myfont.loadFont("Arial Black.ttf", 64);

    
}

//--------------------------------------------------------------
void ofApp::update(){
////tracking
    if(receiver.hasWaitingMessages()){
        ofxOscMessage msg;
        receiver.getNextMessage(&msg);
        

        if ( msg.getAddress() == "/position/front") {
            front.x = (msg.getArgAsFloat( 0 ));
            front.y = (msg.getArgAsFloat( 1 ));
            
           
        }

        if ( msg.getAddress() == "/position/back" ) {
            back.x = (msg.getArgAsFloat( 0 ));
            back.y = (msg.getArgAsFloat( 1 ));
        }

    }
   
    
    if (manual==false){

        position.interpolate(front, 0.5);
        
        direction.set(front.x-back.x,front.y-back.y,0);
        
        cam.setGlobalPosition(position[0],position[1],0);
        
//        cam.setOrientation(direction);
        
        ofLog()<<ofToString(cam.getGlobalPosition());


    }
    


}

//--------------------------------------------------------------
void ofApp::draw(){
    
    cam.begin();
  
    

    for(int i = 0; i < cube_positions.size(); i++){
        ofSetColor(color_bank[i],95);
        box.set(cube_sizesx[i],cube_sizesy[i],cube_sizesz[i]);
        box.setPosition(cube_positions[i]);
        box.draw();
//        ofDrawBox(cube_positions[i], 10);
    }
    
    ofSetColor(255, 0, 0);
    ofDrawCircle(position, 10);
    ofDrawSphere(landmark1.x,landmark1.y, 10);
    ofDrawSphere(landmark2.x,landmark2.y, 10);
    ofDrawSphere(landmark3.x,landmark3.y, 10);
    ofDrawSphere(landmark4.x,landmark4.y, 10);
    ofDrawSphere(landmark5.x,landmark5.y, 10);
    ofDrawSphere(landmark6.x,landmark6.y, 10);
    

    
    

    
    cam.end();
    
   
    

   
    

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if (key == 'm') {
        manual=true;
    }
    if (key == 'a') {
        manual=false;
    }
    if (key == OF_KEY_LEFT) {
        cam.move(0,-5,0);
    }
    else if (key == OF_KEY_RIGHT) {
        cam.move(0,5,0);
    }
    else if (key == OF_KEY_UP) {
        cam.move(-5,0,0);
        
    }
    else if (key == OF_KEY_DOWN) {
        cam.move(5,0,0);
        
    }
    
    else if (key == 'r') {
        cam.pan(10);
        
    }
    else if (key == 'l') {
        cam.pan(-10);
        
    }
    else if(key == '1'){
        mysound.load("dumbo american F.mp3");
        mysound.play();
    }
    else if(key == '2'){
        mysound.load("brooklyn bridge chinese F.mp3");
        mysound.play();
    }
    else if(key == '3'){
        mysound.load("greenwood american F.mp3");
        mysound.play();
    }
    else if(key == '4'){
        mysound.load("prospect time chinese voice.mp3");
        mysound.play();
    }
    else if(key == '5'){
        mysound.load("wailliamsburg.mp3");
        mysound.play();
    }
    else if(key == '6'){
        mysound.load("subway.mp3");
        mysound.play();
    }
    else if(key == 'b'){
        ofBackground(0);
        ofSetColor(255);
        myfont.drawString("NYC Subway", 1000,1000);
        
    }
    else if(key == 'w'){
        ofBackground(255);
       
    }
   
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
