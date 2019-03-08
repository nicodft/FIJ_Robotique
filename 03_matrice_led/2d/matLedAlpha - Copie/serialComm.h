
#define MAX_SIZE  50

class SerialComm {
  private:
  uint8_t _tmpData[MAX_SIZE];
  bool _newData;
  int16_t _length;


  public:
  uint8_t _data[MAX_SIZE];
  /** Object creator */
  SerialComm(void);

  /** Initialisation de la communication série */
  void begin(void);

  /** Renvoie 
   *   - True si un nouveau message est disponible
       - False sinon */
  bool newData(void);

  /** Renvoie la longueur du dernier message reçu, en octet.
   *  Si aucun message n'a encore été reçu, elle renvoie 0
   */
  int16_t length(void);  

  /** Renvoie une donnée du message
     - le paramètre définit le numéro de la donnée à renvoyer
     - Il peut varier de 0 à length-1 (où length est la longueur du message)
     - La fonction renvoie la donnée correspondante, comprise entre 0 et 255
     - Si le paramètre ne respecte pas cet intervalle, la fonction renvoie -1,
      valeur impossible pour une donnée*/
  int getData(int dataNb);
}

