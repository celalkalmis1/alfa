
using System;
class If_Instructions {
    
    /*static int add(int a, int b)
    {
        return a+b;
    }*/
    
    static string divide(int a, int b)
    {
        if(b == 0)
        {
        return "You can't divide by 0 !!!" ;}
        
        else 
        {
            return (a/b).ToString();
        }
        
    }
    
    
    
    
  static void Main() { 
    
    Console.WriteLine(divide(20,2));
    
    
  }
}