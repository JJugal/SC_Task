void setup()
{
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
  Serial.begin(115200);
  Serial.setTimeout(100);
  
  }
  char a;
  int i=0,j=0,m=0;
void loop()
{
  
  if( Serial.available() > 0)

 {
  a=Serial.read();
  if( a=='g')
  {m=1;
   if(j==0)
   j=50;   
  }  
  else if ( a=='s')
  {digitalWrite(13,LOW);
   m=0;
  }
  
  else if ( a=='i')
  j=j+50;
 
  else if ( a=='d')
  j=j-50;
 }
if(j<=0)
{j=50;  
}

if(m==1)
{
  if(j==0)
  digitalWrite(13,LOW);
  else 
  {digitalWrite(13,HIGH);
  delay(j);
  digitalWrite(13,LOW);
  delay(j); }
}
else 
i=i+1;
if(i>1000)
i=0;
Serial.println(i);
delay(10);
}
