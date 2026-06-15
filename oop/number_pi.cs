using System;
class FindingPi {
  static void Main() {
    double pi = 3.141592653589793238;
    
    int rep = 100000;
    
    double total = 0;
    int sign = -1;
    
    for(int i=1; i<rep; i+=2 )
    {
        sign*=-1;
        double term= 1.0*sign*1/i;
        //Console.WriteLine(i+" "+term);
        total += 4*term;
    }
    
    
    
    Console.WriteLine("our value {0} the difference {1}",total, pi - total);
  }
}