/*
  Feu tricolore

  Ce programme fait clignoter 3 LEDs en une séquence semblable à celle d'un feu de signalisation.
  
  Il introduit également la macro #define qui est utilisée pour donner un nom nom aux pattes utilisées
  pour commander les LEDs
*/


/*
 * La macro #define nous permet d'associer un nom au numéro des pattes connectées aux LEDs
 */
#define LED_ROUGE  2
#define LED_ORANGE 3
#define LED_VERTE  4



/* La fonction setup() est exécutée une seule fois au début du programme (quand on alimente l'Arduino
 * ou qu'on appuie sur son bouton reset
 */
void setup() {
  // Configuration des pattes connectées aux LEDs en sorties
  pinMode(LED_ROUGE, OUTPUT);
  pinMode(LED_ORANGE, OUTPUT);
  pinMode(LED_VERTE, OUTPUT);
}



/* La fonction loop() est exécutée en boucle, après la fonction setup()
 * Elle sera exécutée tant que l'Arduino est alimentée et qu'on n'appuie pas le bouton reset
 */
void loop() {
  // Phase rouge : on vient de la phase orange, il faut donc éteindre la LED orange et allumer la LED rouge
  digitalWrite(LED_ORANGE, LOW);
  digitalWrite(LED_ROUGE, HIGH);
  delay(2000);

  // Phase verte : on vient de la phase rouge, il faut donc éteindre la LED rougz et allumer la LED verte
  digitalWrite(LED_ROUGE, LOW);
  digitalWrite(LED_VERTE, HIGH);
  delay(2000);
 
  // Phase orange : on vient de la phase verte, il faut donc éteindre la LED verte et allumer la LED orange
  digitalWrite(LED_VERTE, LOW);
  digitalWrite(LED_ORANGE, HIGH);
  delay(1000);
}
