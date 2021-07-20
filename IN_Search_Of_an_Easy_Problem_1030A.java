import java.util.*;
public class IN_Search_Of_an_Easy_Problem_1030A 
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int n=0;
		int opinion;
		n=sc.nextInt();
		int flag=0;
		while(n!=0)
		{
			opinion=sc.nextInt();
			if(opinion==1)
			{
				flag=1;
				break;
			}		
			n--;
		}
		if(flag==1)
			System.out.println("HARD");
		else if(flag==0)
			System.out.println("EASY");
	}
}
