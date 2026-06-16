using System;
class FindingPi {
    
    static double euler(int rep)
   {
    double term = 1;   
    double total = 0;
    
    for(int i=1; i<rep; i++ )
    {
        term= 1.0*1/(i*i);
        total += term;
    }    
     return Math.Sqrt(total * 6);
   }
    static void Main() {
    double pi = 3.141592653589793238;
    
    Console.WriteLine("our value {0} the difference {1}",euler(100), pi - euler(100));
  }
}