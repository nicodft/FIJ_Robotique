// définition des pattes connectées aux LEDs
#define LEDS_DIAG_1   0 
#define LEDS_HORIZ    1
#define LEDS_DIAG_2   2
#define LED_CENTRE    3 
// Définition de la patte connectée au détecteur d'inclinaison
#define TILT_SWITCH   4 

// ----- DECLARATION DES VARIABLES -----
int resultat;               // stocke le nombre aléatoire généré
int resultatPrecedent = 0;  // stocke la valeur orécédente de résultat


// ----- DECLARATION DES FONCTIONS -----
void afficheValeur(int valeur);


void setup () {
  //On indique que les LED sont des sorties
  pinMode (LEDS_DIAG_1, OUTPUT);
  pinMode (LEDS_HORIZ, OUTPUT);
  pinMode (LEDS_DIAG_2, OUTPUT);
  pinMode (LED_CENTRE, OUTPUT);
  // On indique que le détecteur d'inclinaison est une entrée.
  pinMode (TILT_SWITCH, INPUT);
  // on initialise le générateur de nombres aléatoires
  randomSeed(analogRead(0));
}



void loop() {	
  // si le dé a été basculé, on démarre la séquence
  if (digitalRead(TILT_SWITCH) == LOW) {
    // on commence par générer 8 nombres aléatoires et on les affiche chacun pendant 200ms
    // pour créer une petite animation avant d'afficher le résultat final
    for (int i=0; i <= 7; i++) {
      resultat = random(1, 7);   // on génère un nombre aléatoire
      // Dans l'animation, on ne veut pas afficher 2 fois de suite le même chiffre
      while (resultat == resultatPrecedent) {
        resultat = random(1, 7);
      }
      // on mémorise la valeur pour la prochaine fois
      resultatPrecedent = resultat;
      // on affiche la valeur pendant 200ms
      afficheValeur(resultat);
      delay(200);
    }
    // on laisse le dernier résultat affiché pendant 10s, puis on éteint le dé
    delay(10000);
    afficheValeur(0); // avec 0 comme paramètre, afficheValeur() éteint toutes les LEDs
  }
}



void afficheValeur(int valeur) {
  if (valeur == 1) {
    digitalWrite (LEDS_DIAG_1, LOW);
    digitalWrite (LEDS_HORIZ, LOW);
    digitalWrite (LEDS_DIAG_2, LOW);
    digitalWrite (LED_CENTRE, HIGH);
  } else if (valeur == 2) {
    digitalWrite (LEDS_DIAG_1, HIGH);
    digitalWrite (LEDS_HORIZ, LOW);
    digitalWrite (LEDS_DIAG_2, LOW);
    digitalWrite (LED_CENTRE, LOW);
  } else if (valeur == 3) {
    digitalWrite (LEDS_DIAG_1, LOW);
    digitalWrite (LEDS_HORIZ, LOW);
    digitalWrite (LEDS_DIAG_2, HIGH);
    digitalWrite (LED_CENTRE, HIGH);
  } else if (valeur == 4) {
    digitalWrite (LEDS_DIAG_1, HIGH);
    digitalWrite (LEDS_HORIZ, LOW);
    digitalWrite (LEDS_DIAG_2, HIGH);
    digitalWrite (LED_CENTRE, LOW);
  } else if (valeur == 5) {
    digitalWrite (LEDS_DIAG_1, HIGH);
    digitalWrite (LEDS_HORIZ, LOW);
    digitalWrite (LEDS_DIAG_2, HIGH);
    digitalWrite (LED_CENTRE, HIGH);
  } else if (valeur == 6) {
    digitalWrite (LEDS_DIAG_1, HIGH);
    digitalWrite (LEDS_HORIZ, HIGH);
    digitalWrite (LEDS_DIAG_2, HIGH);
    digitalWrite (LED_CENTRE, LOW);
  } else {
    digitalWrite (LEDS_DIAG_1, LOW);
    digitalWrite (LEDS_HORIZ, LOW);
    digitalWrite (LEDS_DIAG_2, LOW);
    digitalWrite (LED_CENTRE, LOW);
  } 
}
