#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
	ofBackground(255);
	ofSetColor(150, 0, 0);
	ofDrawRectangle(300,100,100,100);
	ofSetColor(255);
	ofDrawRectangle(310, 110, 80, 80);

	ofSetColor(0, 0, 150);
	ofDrawRectangle(800, 800, 100, 100);
	ofSetColor(255);
	ofDrawRectangle(810, 810, 80, 80);

	ofSetColor(0, 150, 0);
	ofDrawRectangle(1200, 100, 100, 100);
	ofSetColor(255);
	ofDrawRectangle(1210, 110, 80, 80);

	ofSetColor(0);
	ofDrawRectangle(1600, ofGetHeight()/2, 100, 100);
	ofSetColor(255);
	ofDrawRectangle(1610, ofGetHeight() / 2 + 10, 80, 80);
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

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
