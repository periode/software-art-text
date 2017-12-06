// - Super Fast Blur v1.1 by Mario Klingemann <http://incubator.quasimondo.com>
// - BlobDetection library


//blobDetection
import blobDetection.*;

//ps3eyep5
import com.thomasdiewald.ps3eye.PS3EyeP5;

//oscp5
import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress myRemoteLocation;


PS3EyeP5 cam;

BlobDetection theBlobDetection;
PImage img;
boolean newFrame=false;

float timer = 500;
float start_time;

// ==================================================
// setup()
// ==================================================
void setup()
{
  start_time = millis();
  // Size of applet
  size(640, 480);
  // Capture
  cam = PS3EyeP5.getDevice(this);

  if (cam == null) {
    System.out.println("No PS3Eye connected. Good Bye!");
    exit();
    return;
  } 

  cam.start();
  cam.waitAvailable(false); 

  // BlobDetection
  // img which will be sent to detection (a smaller copy of the cam frame);
  img = new PImage(cam.getFrame().width, cam.getFrame().height); 
  theBlobDetection = new BlobDetection(img.width, img.height);
  theBlobDetection.setPosDiscrimination(true);
  theBlobDetection.setThreshold(0.2f); // will detect bright areas whose luminosity > 0.2f;


  oscP5 = new OscP5(this, 2047);
  myRemoteLocation = new NetAddress("127.0.0.1", 2046);
}

//// ==================================================


// ==================================================
// draw()
// ==================================================
void draw()
{

  if (millis() - start_time > timer) {


    if (cam.isAvailable()) {
      image(cam.getFrame(), 0, 0);
      img.copy(cam.getFrame(), 0, 0, cam.getFrame().width, cam.getFrame().height, 0, 0, img.width, img.height);
      fastblur(img, 2);
      theBlobDetection.computeBlobs(img.pixels);
      drawBlobsAndEdges(false, false);

      if (theBlobDetection.getBlobNb() > 1) {
        Blob a = theBlobDetection.getBlob(0);
        Blob b  = theBlobDetection.getBlob(1);

        PVector front;
        PVector back;
        if (a.w + a.h > b.w + b.h) {
          back = new PVector(a.x*width, a.y*height);
          front = new PVector(b.x*width, b.y*height);
        } else {
          front = new PVector(a.x*width, a.y*height);
          back = new PVector(b.x*width, b.y*height);
        }



        sendPositions(front, back); 
        start_time = millis();

        fill(255);
        stroke(255);
        line(back.x, back.y, front.x, front.y);
        ellipse(back.x, back.y, 10, 10);
      }
    } else {
    }
  }
}

void sendPositions(PVector f, PVector b) {
  OscMessage myMessage = new OscMessage("/position/front");

  myMessage.add(f.x); /* add an int to the osc message */
  myMessage.add(f.y); /* add a float to the osc message */


  /* send the message */
  oscP5.send(myMessage, myRemoteLocation);  

  myMessage = new OscMessage("/position/back");

  myMessage.add(b.x); /* add an int to the osc message */
  myMessage.add(b.y); /* add a float to the osc message */


  /* send the message */
  oscP5.send(myMessage, myRemoteLocation);
}

// ==================================================
// drawBlobsAndEdges()
// ==================================================
void drawBlobsAndEdges(boolean drawBlobs, boolean drawEdges)
{
  noFill();
  Blob b;
  EdgeVertex eA, eB;
  for (int n=0; n<theBlobDetection.getBlobNb(); n++)
  {
    b=theBlobDetection.getBlob(n);
    if (b!=null)
    {
      // Edges
      if (drawEdges)
      {
        strokeWeight(3);
        stroke(0, 255, 0);
        for (int m=0; m<b.getEdgeNb(); m++)
        {
          eA = b.getEdgeVertexA(m);
          eB = b.getEdgeVertexB(m);
          if (eA !=null && eB !=null)
            line(
              eA.x*width, eA.y*height, 
              eB.x*width, eB.y*height
              );
        }
      }

      // Blobs
      if (drawBlobs)
      {
        strokeWeight(1);
        stroke(255, 0, 0);
        rect(
          b.xMin*width, b.yMin*height, 
          b.w*width, b.h*height
          );
      }
    }
  }
}

// ==================================================
// Super Fast Blur v1.1
// by Mario Klingemann 
// <http://incubator.quasimondo.com>
// ==================================================
void fastblur(PImage img, int radius)
{
  if (radius<1) {
    return;
  }
  int w=img.width;
  int h=img.height;
  int wm=w-1;
  int hm=h-1;
  int wh=w*h;
  int div=radius+radius+1;
  int r[]=new int[wh];
  int g[]=new int[wh];
  int b[]=new int[wh];
  int rsum, gsum, bsum, x, y, i, p, p1, p2, yp, yi, yw;
  int vmin[] = new int[max(w, h)];
  int vmax[] = new int[max(w, h)];
  int[] pix=img.pixels;
  int dv[]=new int[256*div];
  for (i=0; i<256*div; i++) {
    dv[i]=(i/div);
  }

  yw=yi=0;

  for (y=0; y<h; y++) {
    rsum=gsum=bsum=0;
    for (i=-radius; i<=radius; i++) {
      p=pix[yi+min(wm, max(i, 0))];
      rsum+=(p & 0xff0000)>>16;
      gsum+=(p & 0x00ff00)>>8;
      bsum+= p & 0x0000ff;
    }
    for (x=0; x<w; x++) {

      r[yi]=dv[rsum];
      g[yi]=dv[gsum];
      b[yi]=dv[bsum];

      if (y==0) {
        vmin[x]=min(x+radius+1, wm);
        vmax[x]=max(x-radius, 0);
      }
      p1=pix[yw+vmin[x]];
      p2=pix[yw+vmax[x]];

      rsum+=((p1 & 0xff0000)-(p2 & 0xff0000))>>16;
      gsum+=((p1 & 0x00ff00)-(p2 & 0x00ff00))>>8;
      bsum+= (p1 & 0x0000ff)-(p2 & 0x0000ff);
      yi++;
    }
    yw+=w;
  }

  for (x=0; x<w; x++) {
    rsum=gsum=bsum=0;
    yp=-radius*w;
    for (i=-radius; i<=radius; i++) {
      yi=max(0, yp)+x;
      rsum+=r[yi];
      gsum+=g[yi];
      bsum+=b[yi];
      yp+=w;
    }
    yi=x;
    for (y=0; y<h; y++) {
      pix[yi]=0xff000000 | (dv[rsum]<<16) | (dv[gsum]<<8) | dv[bsum];
      if (x==0) {
        vmin[y]=min(y+radius+1, hm)*w;
        vmax[y]=max(y-radius, 0)*w;
      }
      p1=x+vmin[y];
      p2=x+vmax[y];

      rsum+=r[p1]-r[p2];
      gsum+=g[p1]-g[p2];
      bsum+=b[p1]-b[p2];

      yi+=w;
    }
  }
}