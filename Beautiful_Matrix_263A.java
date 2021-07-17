import java.util.*;
public class Beautiful_Matrix_263A 
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int i=3;//desired row
		int j=3;//desired column
		int row1=0;//original location of row containing 1
		int column1=0;//original location of column containing 1
		for(int p=1;p<=5;p++)
		{
			String s=sc.nextLine().replace(" ", "");
			if(s.contains("1"))
			{
				row1=p;
				column1=s.indexOf("1")+1;
				break;
			}													
		}
		System.out.println(Math.abs(j-column1)+Math.abs(i-row1));
		
		
		
	}

}
