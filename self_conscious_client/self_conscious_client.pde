//Python acts as server

import processing.net.*; 
Client myClient; 
String dataIn; 
 
void setup() { 
  size(200, 200); 
  // Connect to the local machine at port 5204.
  // This example will not run if you haven't
  // previously started a server on this port.
  myClient = new Client(this, "127.0.0.1", 5001); 
} 
 
void draw() { 
  if (myClient.available() > 0) { 
    dataIn = myClient.readString(); 
    println(dataIn);
  } 

} 

void keyPressed(){
  if (key == 'r'){
    myClient.write("success");
  }
}
    
  
