#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup() {
	Beat.loadSound("george_poem.mp3");

	fftSmooth = new float[8192];
	for (int i = 0; i<8192; i++) {
		fftSmooth[i] = 0;
	}

	bands = 64;
	Beat.setLoop(true);
	Beat.setVolume(.5);

	Beat.play();

}

//--------------------------------------------------------------
void ofApp::update() {
	ofSoundUpdate();
	float * value = ofSoundGetSpectrum(bands);
	for (int i = 0; i<bands; i++) {
		fftSmooth[i] *= 0.79f;
		if (fftSmooth[i] < value[i]) {
			fftSmooth[i] = value[i];
		}
	}
}

//--------------------------------------------------------------
void ofApp::draw() {
	if (isSaving) {
		ofBeginSaveScreenAsPDF("print-" + ofToString(ofGetElapsedTimeMicros()) + ".pdf");
	}
	ofBackground(0);
	for (int i = 0; i < 5; i++) {
		ofSetColor(173, 255, 47);
		ofPushMatrix();
		ofTranslate(ofGetWidth() / 2 + i*10, ofGetHeight() / 2 +i*10);
		ofNoFill();
		ofBeginShape();
		for (int i = 0; i < 512; i++) {
			ofVertex(i * 20, 100 * -(fftSmooth[i] * 10));

		}
		ofEndShape();
		ofPopMatrix();
	}
	for (int i = 0; i < 5; i++) {
		ofPushMatrix();
		ofTranslate(ofGetWidth() / 2 + i * 10, ofGetHeight() / 2 + i * 10);
		ofRotate(180);
		ofNoFill();
		ofSetColor(0, 255, 127);
		ofBeginShape();
		for (int i = 0; i < 512; i++) {
			ofVertex(i * 20, 100 * -(fftSmooth[i] * 10));
		}
		ofEndShape();
		ofPopMatrix();
	}
	for (int i = 0; i < 5; i++) {
		ofPushMatrix();
		ofTranslate(ofGetWidth() / 2 + i * 10, ofGetHeight() / 2 + i * 10);
		ofRotate(90);
		ofNoFill();
		ofSetColor(0, 100, 0);
		ofBeginShape();
		for (int i = 0; i < 512; i++) {
			ofVertex(i * 20, 100 * -(fftSmooth[i] * 10));

		}
		ofEndShape();
		ofPopMatrix();
	}
	for (int i = 0; i < 5; i++) {
		ofPushMatrix();
		ofTranslate(ofGetWidth() / 2 + i * 10, ofGetHeight() / 2 + i * 10);
		ofRotate(270);
		ofNoFill();
		ofSetColor(0, 255, 0);
		ofBeginShape();
		for (int i = 0; i < 512; i++) {
			ofVertex(i * 20, 100 * -(fftSmooth[i] * 10));

		}
		ofEndShape();
		ofPopMatrix();
	}
	if (isSaving) {
		ofEndSaveScreenAsPDF();
		isSaving = false;
	}

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key) {
	switch (key) {
	case '1':
		Beat.play();
		break;
	case '2':
		Beat.stop();
		break;
	}
	if (key == 's') {
		isSaving = true;
	}
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key) {

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y) {

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button) {

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button) {

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button) {

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h) {

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg) {

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo) {

}