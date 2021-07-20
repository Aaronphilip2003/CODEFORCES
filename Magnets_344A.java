import java.util.*;
public class Magnets_344A 
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int number,count=1;
		number=sc.nextInt();
		int[] magnets=new int[number];
		for(int i=0;i<number;i++)
		{
			magnets[i]=sc.nextInt();
		}
		for(int i=0;i<number-1;i++)
		{
		    if(magnets[i]!=magnets[i+1])
		        count++;
		}
		System.out.println(count);
		
		
		
	}
}
