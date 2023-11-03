int trig=14;
int echo=15;
int trig2=13;
int echo2=12;
long distance;
#include <PubSubClient.h>
#include <WiFi.h>
#include <Servo.h>
Servo myservo;
#define ssid "RM306-RESIDENCE"
#define password "InTeRnEt"
#define mqtt_server "mqtt.eclipseprojects.io"
WiFiClient espClient;
PubSubClient Mclient(espClient);////creating an object in pubsub client

int timeh;

    // to subscribe data.........we will have to draw the callback funtion so that it can work as a communication channel

     // Creating MQTT callback
void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  
  
    //converting the message received in bytes to char 
    for (int i = 0; i < length; i++) {
      Serial.print((char)message[i]);
      messageTemp += (char)message[i];
      Serial.println(messageTemp);
    }
    Serial.println();
  
    // Feel free to add more if statements to control more GPIOs with MQTT
  
    // If a message is received on the topic home/office/esp1/gpio2, you check if the message is either 1 or 0. Turns the ESP GPIO according to the message
    if(topic=="phone"){
        
        if(messageTemp == "open"){
          myservo.write(180);
          Serial.print("Open");
        }
        else if(messageTemp == "close"){
          myservo.write(0);
          Serial.print("closed");
        }
    }
}

void reconnect() {
  // Loop until we're reconnected
  while (!Mclient.connected()) {
  Serial.print("Attempting MQTT connection...");
  // Attempt to connect to a specific id which is esp8266client
   
  if (Mclient.connect("ESPG32")) {
    Serial.println("connected");  
    // Subscribe or resubscribe to a topic
    // You can subscribe to more topics (to control more LEDs in this example)
    Mclient.subscribe("phone");//pump is the topic which then the client will be able to publish to in the callback looop
   
  } else {
    Serial.print("failed, rc=");
    Serial.print(Mclient.state());
    Serial.println(" try again in 5 seconds");
    // Wait 5 seconds before retrying
    delay(5000);
  }
  }
  }
  

void setup() {
  // put your setup code here, to run once:
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(trig2,OUTPUT);
  pinMode(echo2,INPUT);
  Serial.begin(9600);
  myservo.attach(16);
  WiFi.mode(WIFI_STA);//to intiate it as a listener butcomes automatic so this line of code is not very much useful
  delay(10);
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);

   //wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
  //Serial.println("IP address: " + WiFi.localIP().toString());//viewing ip address

  Mclient.setServer(mqtt_server, 1883);//creating mqtt
  Mclient.setCallback(callback);//for the client to publish

  

//to reconnect whenever not connected
  if (!Mclient.connected()) {
    reconnect();
  }
  if(!Mclient.loop())
    Mclient.connect("ESPG32");
  
}


int calculate_distance(int trigpin,int echopin){
  digitalWrite(trigpin,LOW);
  delay(100);
  digitalWrite(trigpin,HIGH);
  delay(100);
  digitalWrite(trigpin,LOW);
  
  timeh=pulseIn(echopin,HIGH);
  distance=timeh *0.0343/2;
  return distance;
}

void loop() {
  // put your main code here, to run repeatedly:
  int distance_1 = calculate_distance(trig,echo);
  Serial.println(distance_1);
  delay(500);
  if (distance_1 <= 100){
    myservo.write(180);
  }
  else{
    myservo.write(0);
  }
  int distance_2=calculate_distance(trig2,echo2);
  Serial.println(distance_2);
  delay(500);

   // put your main code here, to run repeatedly:

  int percentage = distance_2/ 194;
  int final_percentage = percentage *100;

  ///publishing data.....the first tpart in the arguement is the topic subscribe in string format while the second part is the message in string format
  char per[8];
  dtostrf(final_percentage, 4, 2, per);
  Mclient.publish("keith", per);
  delay(1000);
 }
