import java.util.*;
public class Soldier_and_bananas_546A 
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int bananacost=0,initialmoney=0,numbanana=0;
		int added=0;
		int finalcost=0;
		bananacost=sc.nextInt();
		initialmoney=sc.nextInt();
		numbanana=sc.nextInt();
		int total=0;
		
		for(int i=0;i<=numbanana;i++)
		{
			total=total+i*bananacost;
		}
		if(total-initialmoney>0)
			System.out.println(total-initialmoney);
		else
			System.out.println("0");
	}

}
