import java.util.*;
public class Is_your_horseshoe_on_the_other_hoof_228A 
{
	public static void sort(int[]a)
	{
		int temp=0;
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3-i;j++)
			{
				if(a[j]>a[j+1])
                {
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
				
			}
		}
		
	}
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int[] a=new int[4];
		int count=0;
		for(int i=0;i<4;i++)
		{
			a[i]=sc.nextInt();
		}
		sort(a);
		
		for(int i=0;i<3;i++)
		{
			if(a[i]==a[i+1])
				count++;
		}
		System.out.println(count);
		
	}

}
