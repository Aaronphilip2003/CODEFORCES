import java.io.*;
import java.util.*;
class Remove_Duplicates
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		Scanner sc=new Scanner(System.in);
		int size=0,temp=0,counter=0,k=0;
		size=Integer.parseInt(br.readLine());
		int a[]=new int[size];
		int b[]=new int[size];
		int c[]=new int[size];
		for(int i=0;i<size;i++)
		{
			a[i]=sc.nextInt();
		}
		for(int i=0;i<size;i++)
		{
			b[i]=a[i];
		}
		for(int i=1;i<size;i++)
		{
			temp=a[i];
			int j=i-1;
			while(j>=0&&a[j]>temp)
			{
				a[j+1]=a[j];
				j--;
			}
			a[j+1]=temp;
		}
		// for(int i=0;i<size;i++)
		// {
		// 	System.out.println(a[i]);
		// }
		//Now the array is Sorted 
		// Now we'll compare adjacent elements
		for(int i=0;i<size-1;i++)
		{
			if(a[i]!=a[i+1])
			{
				c[k++]=a[i];
			}
		}
			c[k++]=b[size-1];
		for(int i=0;i<k;i++)
		{
			System.out.println(c[i]);
		}		
	}
}