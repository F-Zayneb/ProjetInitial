#define pinEnable 12 // Activation du driver/pilote
#define pinStep    3 // Signal de PAS (avancement)
#define pinDir     2 // Direction 


void setup(){
  Serial.begin(9600);
  Serial.println("Test DRV8825");
  
  pinMode( pinEnable, OUTPUT );
  pinMode( pinDir   , OUTPUT );
  pinMode( pinStep  , OUTPUT );
}

void loop(){
  int i = 0;
  
  digitalWrite( pinDir   , HIGH); // Direction avant
  digitalWrite( pinStep  , LOW);  // Initialisation de la broche step
  
  // Avance de 200 pas
  for( i=0; i<360; i+50){
    Serial.println( i );
    digitalWrite( pinStep, HIGH );
    delay(2);
    digitalWrite( pinStep, LOW );
    delay(2);
  } 
  
  // Changer de direction
  digitalWrite( pinDir   , LOW); // Direction avant
  
  // Refaire 200 pas dans l'autre sens
  for( i=0; i<1; i++){
    Serial.println( i );
    //digitalWrite( pinStep, HIGH );
    //delay( 10 );
    digitalWrite( pinStep, LOW );
    delay( 10 );
  } 
  
  // Pas de step et pas d'ordre... 
  //   l'axe du moteur est donc bloqué 
  Serial.println("Axe bloqué + attendre 5 sec");
  delay( 5000 );
  
  // déblocage de l'axe moteur
  Serial.println("Deblocage axe");
  digitalWrite( pinEnable, HIGH ); // logique inversée
  
  // Fin et blocage du programme
  // Presser reset pour recommander
  Serial.println("Fin de programme");
  while( true );
}
