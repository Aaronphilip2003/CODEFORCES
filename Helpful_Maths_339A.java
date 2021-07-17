import java.io.*;
import java.util.*;
public class Helpful_Maths_339A
{
	public static void main(String args[])throws IOException
	{	
		Scanner sc=new Scanner(System.in);
		String s=sc.next();
		int[] numbers=new int[(s.length()/2)+1];
		int count=0;
		
		for(char ch:s.toCharArray())
		{
			if(ch!='+')
			{
				numbers[count]=Character.getNumericValue(ch);
				count++;
			}
		}
			Arrays.sort(numbers);
			for(int i=0;i<numbers.length-1;i++)
				System.out.print(numbers[i]+"+");
			System.out.print(numbers[numbers.length-1]);
		
	}

}
