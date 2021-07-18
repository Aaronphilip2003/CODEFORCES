import java.util.*;
public class Tram_116A 
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int stops=0;
		int current=0;
		int enter=0,exit=0;
		int max=0;
		stops=sc.nextInt();
		while(stops!=0)
		{
			exit=sc.nextInt();
			enter=sc.nextInt();
			current=current+enter-exit;
			if(current>max)
				max=current;
			stops--;
		}
		System.out.println(max);
		
	}

}
