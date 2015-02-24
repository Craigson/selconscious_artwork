//Python acts as server

//code for processing to run as client
import processing.net.*; 
Client myClient; 
String dataIn; 
boolean firstContact;

//code for Seiffert's spherical spiral
float r; //radius of sphere
float a; //
FloatList xVals;
FloatList yVals;
FloatList zVals;

void setup() { 
  size(200, 200); 
  xVals = new FloatList();
  yVals = new FloatList();
  zVals = new FloatList();

  // Connect to the local machine at port 5001.
  // This example will not run if you haven't
  // previously started a server on this port.
  myClient = new Client(this, "127.0.0.1", 5001);
} 

void draw() { 
    if (myClient.available() > 0) {
      println("receiving data");
      dataIn = myClient.readString();
      float values [] = float(split(dataIn, ','));
      if (values.length == 3) {
        xVals.append(values[0]);
        yVals.append(values[1]);
        zVals.append(values[2]);
      }
      myClient.write('A');
    }
  }


  void keyPressed() {
    if (key == 'r') {
      myClient.write("A");
    }
    if (key =='p') {
      println(xVals);
    }
  }
