import java.util.*;
public class Drinks_200B 
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int n=0;
		n=sc.nextInt();
		double[] perc=new double[n];
		double sum=0.0;
		for(int i=0;i<n;i++)
		{
			perc[i]=sc.nextInt();
			perc[i]=perc[i]/100.0;
			sum+=perc[i];
		}
		System.out.println((sum/n)*100);
			
		
		
	}

}
