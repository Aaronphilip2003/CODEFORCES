import java.io.*;
public class Nearly_Lucky_Number_110A
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		long number=0;
		int count=0;
		boolean flag=true;
		number=Long.parseLong(br.readLine());
		while(number>0)
		{
			long r=number%10;
			if(r==4||r==7)
			{
				count++;
			}
			number=number/10;
		}
		if(count==4||count==7)
			System.out.println("YES");
		else
			System.out.println("NO");
	}
}
