/*
  Ce programme fait clignoter 5 LEDs :
   - 3 LEDs formant un feu de signalisation pour voitures
   - 2 LEDs formant un feu de signalisation pour piéton
  
  Il exécute une séquence semblable à celle des feux de signalisation d'un passage pour piétons.
*/


// La macro #define nous permet d'associer un nom au numéro des pattes connectées aux LEDs
// LEDs du feu voiture
#define VOITURE_ROUGE  2
#define VOITURE_ORANGE 3
#define VOITURE_VERTE  4
// LEDs du feu piéton
#define PIETON_ROUGE   5
#define PIETON_VERTE   6


/* La fonction setup() est exécutée une seule fois au début du programme (quand on alimente l'Arduino
 * ou qu'on appuie sur son bouton reset
 */
void setup() {
  // Configuration des pattes connectées aux LEDs en sorties
  pinMode(VOITURE_ROUGE, OUTPUT);
  pinMode(VOITURE_ORANGE, OUTPUT);
  pinMode(VOITURE_VERTE, OUTPUT);
  pinMode(PIETON_ROUGE, OUTPUT);
  pinMode(PIETON_VERTE, OUTPUT);
  // Définition de la situation initiale : les deux feux sont au rouge
  digitalWrite(VOITURE_ROUGE, HIGH);
  digitalWrite(PIETON_ROUGE, HIGH);
  delay(2000);
}


/* La séquence des feux est découpée en 5 phases :
 *  Situation initiale : les deux feux sont au rouge
 *  Phase 1 : le feu piéton passe au vert, le feu voiture reste au rouge
 *  Phase 2 : le feu piéton passe au rouge, le feu voiture reste au rouge
 *  Phase 3 : le feu voiture passe au vert, le feu piéton reste au rouge
 *  Phase 4 : le feu voiture passe à l'orange, le feu piéton reste au rouge
 *  Phase 5 : le feu voiture passe au rouge, le feu piéton reste au rouge
 *  La phase 5 est identique à la situation initiale, on a donc bien une séquence en boucle
 */
void loop() {
  // Phase 1
  digitalWrite(PIETON_ROUGE, LOW);
  digitalWrite(PIETON_VERTE, HIGH);
  delay(4000);
  // Phase 2
  digitalWrite(PIETON_VERTE, LOW);
  digitalWrite(PIETON_ROUGE, HIGH);
  delay(2000);
  // Phase 3
  digitalWrite(VOITURE_ROUGE, LOW);
  digitalWrite(VOITURE_VERTE, HIGH);
  delay(4000);
  // Phase 4
  digitalWrite(VOITURE_VERTE, LOW);
  digitalWrite(VOITURE_ORANGE, HIGH);
  delay(2000);
  // Phase 5
  digitalWrite(VOITURE_ORANGE, LOW);
  digitalWrite(VOITURE_ROUGE, HIGH);
  delay(4000);
}
