import java.io.*;
import java.util.*;
public class Vanya_and_Fence_677A 
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		Scanner sc=new Scanner(System.in);
		int n,h;	
		int sum=0;
		n=sc.nextInt();
		h=sc.nextInt();
		int[] a=new int[n];
		for(int i=0;i<n;i++)
		{
			a[i]=sc.nextInt();
		}
		for(int i=0;i<n;i++)
		{
			if(a[i]>h)
			{
				sum+=2;
			}
			else if(a[i]<=h)
				sum+=1;
		}
		System.out.println(sum);
			
		
	}

}
