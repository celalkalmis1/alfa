using System;
class GuessNumber {
    
    
    static void Main() {
  
  //class  object       constructor 
    Random random = new Random();
    
    int secretNumber = random.Next(1,100); // next kodu bize sayı ataması yapıyor random ise object 
    int ourGuess;
    int moves = 0;
    bool end = true;
    
    while(end)
    {
        Console.Write("Guess the number: ");
        ourGuess = Convert.ToInt32(Console.ReadLine());
        moves+=1;
        
        if(ourGuess > secretNumber )
            Console.WriteLine("Too big!");
        if (ourGuess < secretNumber )
            Console.WriteLine("Too small!");
        
        
        if(ourGuess == secretNumber){
        end = false;
        }
        
    }
    Console.WriteLine("You guessed the numberr in {0} moves", moves);
  }
}


// sonraki ödev biz yazıcaz bilgisayar tahmin edicek.