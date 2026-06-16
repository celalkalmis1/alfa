using System;
using System.Linq;
using System.Collections.Generic;

// LINQ Query Syntax examples

public class Program
{
	public static void Main()
	{
		// Student collection
		List<Student> students = new List<Student>() { 
		        new Student() { Name = "Zbych", Marks = 13, Faculty = "Informatics"} ,
				new Student() { Name = "John", Marks = 11, Faculty = "Informatics"} ,
				new Student() { Name = "Ala", Marks = 12, Faculty = "Mathematics" } ,
				new Student() { Name = "Ola", Marks = 9, Faculty = "Informatics" } ,
				new Student() { Name = "Ela", Marks = 4, Faculty = "Mathematics"} ,
				new Student() { Name = "Ula", Marks = 10, Faculty = "Informatics" }, 
				new Student() { Name = "Rick", Marks = 12, Faculty = "Medicine" },
				new Student() { Name = "Henek", Marks = 10, Faculty = "Mathematics" },
				new Student() { Name = "Basia", Marks = 14, Faculty = "Medicine" },
				new Student() { Name = "Anna", Marks = 11, Faculty = "Mathematics" },
				new Student() { Name = "Fred", Marks = 5, Faculty = "Informatics" },
				new Student() { Name = "Beata", Marks = 9, Faculty = "Psychology" }
			
			};
		
	
		var result = from s in students
							  where s.Marks < 9 
							  select s;
		Console.WriteLine("(Ex 1.) Candidates that can not be enrolled (too few scores):");
						  
		foreach(Student stud in result){			
			Console.WriteLine(stud.Name + " - " + stud.Marks + " - " + stud.Faculty );
		
		}
		
		 var   result1 = from s in students
							  where s.Marks > 9 && s.Faculty == "Informatics" 
							  orderby s.Name 
							  select s;
		
		Console.WriteLine("----------------------------------------");
		Console.WriteLine("(Ex 2.) Candidates enrolled to Infromatics:");					  
		foreach(Student stud1 in result1){			
			Console.WriteLine(stud1.Name + " - " + stud1.Marks + " - " + stud1.Faculty );
		}
		
		
		Console.WriteLine("----------------------------------------");
		var avgMarks = students.Average(s => s.Marks);	
		Console.WriteLine("(Ex 3.) Average for all Candidates is {0}. ", avgMarks);	
		
		Console.WriteLine("----------------------------------------");
		Console.WriteLine("(Ex 4.) Candidates by faculties:");
		//-----------------------------------
		
		var result2 = from s in students
		            //where s.Marks > 11
		            //orderby s.Name
		            //orderby avgMarks
		            orderby s.Marks descending
                    select s;

		//iterate each group        
		foreach (var s in result2)
		{
		    
		    Console.WriteLine("{0} \t {1} \t Faculty: {2}", s.Name, s.Marks, s.Faculty);
		
		}
		
	    
	    Console.WriteLine("----------------------------------------");
		Console.WriteLine("(Ex 5.) Average for all faculties:");
		
	    var result3 = 
    	    from s in students 
    	    group s by s.Faculty into groups 
    	    select new 
    	    { 
    	        Faculty = groups.Key, 
    	        AverageMarks = groups.Average(s => s.Marks), 
    	    };
    	    
	        
	        foreach (var faculty in result3)
	         {
	             Console.WriteLine("{0} \t  {1}", faculty.Faculty, faculty.AverageMarks);
	         }
	    
	    
	
		//-----------------------------------
	
	}
}

public class Student{

	public int ID { get; set; }
	public string Name { get; set; }
	public int Marks { get; set; }
	public string Faculty { get; set; }
	
}



