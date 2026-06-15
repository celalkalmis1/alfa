using System;
class FindingPi {
    
    static double leibnitz(int rep)
   {
    double term = 1;   
    double total = 0;
    int sign = -1;
    
    for(int i=1; i<rep; i+=2 )
    {
        sign*=-1;
        term= 1.0*sign*1/i;
        total += term;
    }    
     
     return 4*total;
   }
    static void Main() {
    double pi = 3.141592653589793238;
    
    Console.WriteLine("our value {0} the difference {1}",leibnitz(1000000), pi - leibnitz(1000000));
  }
}