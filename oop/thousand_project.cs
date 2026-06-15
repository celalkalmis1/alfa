
using System;
class thousand_project {
  static void Main() {
    int toplam = 0;
    
    for(int i=0 ; i < 1000 ; i++)
    {
        if (i %3 == 0 || i %5 == 0){ // because we use "or" operator so it didn't repated 15.
            toplam += i;
        }
    }
    
    
    Console.WriteLine("Sonuç: {0} ",toplam);
  }
}