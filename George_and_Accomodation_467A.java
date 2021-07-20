import java.util.*;
public class George_and_Accomodation_467A
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int rooms=0;
		int count=0;
		rooms=sc.nextInt();
		int[] capacity=new int[100];
		int[] current=new int[100];
		for(int i=0;i<rooms;i++)
		{
			capacity[i]=sc.nextInt();
			current[i]=sc.nextInt();
		}
		for(int i=0;i<rooms;i++)
		{
			if(current[i]-capacity[i]>=2)
				count++;
		}
		System.out.println(count);
	}

}
